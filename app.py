import base64
import os
import tempfile

import fitz
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader


# =========================================================
# CONFIG
# =========================================================

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    st.error("GROQ_API_KEY not found.")
    st.stop()

client = Groq(api_key=API_KEY)

VISION_MODEL = "qwen/qwen3.8-27b"


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Multimodal PDF RAG",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Settings")

screen_layout = st.sidebar.selectbox(
    "🖥️ Screen Layout",
    [
        "Wide screen",
        "Fit to screen"
    ]
)

answer_mode = st.sidebar.selectbox(
    "🧠 Answer Mode",
    [
        "PDF + General Knowledge",
        "PDF Only"
    ]
)


# =========================================================
# SCREEN LAYOUT
# =========================================================

if screen_layout == "Fit to screen":

    st.markdown(
        """
        <style>
        .block-container {
            max-width: 900px;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TITLE
# =========================================================

st.title("📄 Multimodal PDF RAG")

st.write(
    "Upload a PDF and ask questions about its "
    "text, tables, charts, graphs, diagrams and images."
)


# =========================================================
# PDF UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📤 Upload your PDF",
    type=["pdf"]
)


# =========================================================
# PROCESS PDF
# =========================================================

if uploaded_file:

    # -----------------------------------------------------
    # SAVE PDF
    # -----------------------------------------------------

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_file.getvalue()
            )

            pdf_path = temp_file.name

    except Exception as e:

        st.error(
            f"Could not save PDF: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # EXTRACT TEXT
    # -----------------------------------------------------

    try:

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

    except Exception as e:

        st.error(
            f"Could not load PDF: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # CONVERT PDF PAGES TO IMAGES
    # -----------------------------------------------------

    try:

        pdf = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(pdf):

            matrix = fitz.Matrix(
                1.5,
                1.5
            )

            pixmap = page.get_pixmap(
                matrix=matrix,
                alpha=False
            )

            image_bytes = pixmap.tobytes(
                "png"
            )

            pages.append(
                {
                    "page_number": page_number + 1,
                    "image": image_bytes,
                    "text": documents[
                        page_number
                    ].page_content
                }
            )

        pdf.close()

    except Exception as e:

        st.error(
            f"Could not process PDF pages: {e}"
        )

        st.stop()


    st.success(
        f"PDF loaded successfully — {len(pages)} pages"
    )


    # =====================================================
    # QUESTION FORM
    # =====================================================

    with st.form("question_form"):

        question = st.text_input(
            "❓ Ask anything about your PDF",
            placeholder="Type your question and press Enter..."
        )

        ask = st.form_submit_button(
            "🔍 Ask"
        )


    # =====================================================
    # QUESTION PROCESSING
    # =====================================================

    if ask:

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

            st.stop()


        with st.spinner(
            "Searching the PDF and analyzing relevant content..."
        ):

            # -------------------------------------------------
            # FIND RELEVANT PAGES
            # -------------------------------------------------

            question_words = set(
                question.lower().split()
            )

            scored_pages = []

            for page in pages:

                page_text = page["text"].lower()

                score = sum(
                    1
                    for word in question_words
                    if len(word) > 2
                    and word in page_text
                )

                scored_pages.append(
                    (
                        score,
                        page
                    )
                )


            scored_pages.sort(
                key=lambda x: x[0],
                reverse=True
            )


            relevant_pages = [
                page
                for score, page in scored_pages
                if score > 0
            ]


            # If no text match is found,
            # allow visual inspection.

            if not relevant_pages:

                relevant_pages = pages


            # Keep Vision request manageable.

            relevant_pages = relevant_pages[:3]


            # -------------------------------------------------
            # ANSWER MODE
            # -------------------------------------------------

            if answer_mode == "PDF Only":

                knowledge_instruction = """
Use ONLY information available in the PDF.

If the answer cannot be found in the PDF,
say:

"Information not found in the PDF."

Do not use outside knowledge.
Do not invent information.
"""

            else:

                knowledge_instruction = """
Use information from the PDF whenever available.

You may also use your general pretrained knowledge
when the required information is not available
in the PDF.

Clearly distinguish general knowledge from
information found in the PDF when necessary.

Do not invent information.
"""


            # -------------------------------------------------
            # VISION PROMPT
            # -------------------------------------------------

            content = [
                {
                    "type": "text",
                    "text": f"""
You are answering a question about a PDF.

The PDF may contain:

- normal text
- tables
- charts
- graphs
- diagrams
- images

Carefully inspect BOTH:

1. Extracted PDF text
2. Visual content of the provided PDF pages

{knowledge_instruction}

User question:

{question}

Give a clear and direct answer.

If the answer depends on a chart, table, graph,
diagram or image, carefully inspect the visual
content.

Do not guess values that cannot be read.
"""
                }
            ]


            # -------------------------------------------------
            # ADD RELEVANT PAGES
            # -------------------------------------------------

            for page in relevant_pages:

                base64_image = base64.b64encode(
                    page["image"]
                ).decode("utf-8")


                # Add extracted text

                content.append(
                    {
                        "type": "text",
                        "text": f"""
========================
PDF PAGE {page['page_number']}
========================

Extracted text:

{page['text'][:5000]}
"""
                    }
                )


                # Add page image

                content.append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/png;base64,{base64_image}"
                        }
                    }
                )


            # =================================================
            # GROQ VISION MODEL
            # =================================================

            try:

                response = client.chat.completions.create(
                    model=VISION_MODEL,
                    max_completion_tokens=500,
                    reasoning_effort="none",
                    messages=[
                        {
                            "role": "user",
                            "content": content
                        }
                    ]
                )

                answer = (
                    response
                    .choices[0]
                    .message
                    .content
                )

            except Exception as e:

                st.error(
                    f"AI response error: {e}"
                )

                st.stop()


        # =================================================
        # ANSWER
        # =================================================

        st.subheader("🤖 Answer")

        st.write(answer)


        # =================================================
        # SOURCES
        # =================================================

        st.subheader("📚 Sources")

        for page in relevant_pages:

            st.write(
                f"📄 Page {page['page_number']}"
            )


else:

    st.info(
        "📤 Upload a PDF to start asking questions."
    )