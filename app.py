# #               < learning PypdfLoader >              #
# # import streamlit as st
# # import tempfile

# # from langchain_community.document_loaders import PyPDFLoader


# # st.set_page_config(
# #     page_title="PDF Reader",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF Reader App")

# # st.write("Upload a PDF to read its content.")


# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success("PDF uploaded successfully!")

# #     # Step 1: Create temporary PDF file
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name

# #     st.write("Temporary file created successfully.")

# #     # Step 2: Load PDF using PyPDFLoader
# #     loader = PyPDFLoader(pdf_path)

# #     documents = loader.load()

# #     # Step 3: Display total pages
# #     st.write("Total pages:", len(documents))

# #     # Step 4: Display extracted text
# #     if documents:

# #         st.subheader("Extracted Text")

# #         st.write(
# #             documents[0].page_content[:1000]
# #         )

# # else:

# #     st.info("Please upload a PDF file.")





# #                         < Text chunking >                         #

# # import streamlit as st
# # import tempfile

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma


# # st.set_page_config(
# #     page_title="PDF Chunking",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF Chunking App")

# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success("PDF uploaded successfully!")

# #     # Step 1: Create a temporary PDF file
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name

# #     # Step 2: Load PDF
# #     loader = PyPDFLoader(pdf_path)

# #     documents = loader.load()

# #     st.write("Total pages:", len(documents))

# #     # Step 3: Create text splitter
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     # Step 4: Split PDF text into chunks
# #     chunks = splitter.split_documents(documents)

# #     st.write("Total chunks:", len(chunks))

# #     # Step 5: Display first chunk
# #     if chunks:

# #         st.subheader("First Chunk")

# #         st.write(chunks[0].page_content)

# #         st.write("Chunk metadata:")
# #         st.write(chunks[0].metadata)

# # else:

# #     st.info("Please upload a PDF file.")







# #               < Create vector store >              #


# # import streamlit as st
# # import tempfile

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma


# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG App")

# # st.write("Upload a PDF to create chunks and store them in Chroma.")


# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success("PDF uploaded successfully!")

# #     # Step 1: Create a temporary PDF file
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name

# #     st.write("Temporary file created successfully.")

# #     # Step 2: Load PDF using PyPDFLoader
# #     loader = PyPDFLoader(pdf_path)

# #     documents = loader.load()

# #     st.write("Total pages:", len(documents))

# #     # Step 3: Create text splitter
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     # Step 4: Split PDF into chunks
# #     chunks = splitter.split_documents(documents)

# #     st.write("Total chunks:", len(chunks))

# #     # Step 5: Display first chunk
# #     if chunks:

# #         st.subheader("First Chunk")

# #         st.write(
# #             chunks[0].page_content
# #         )

# #         st.write("Chunk metadata:")

# #         st.write(
# #             chunks[0].metadata
# #         )

# #     # Step 6: Create embedding model
# #     with st.spinner("Creating embeddings..."):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )

# #     # Step 7: Store chunks and embeddings in Chroma
# #     with st.spinner("Storing chunks in Chroma..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name="streamlit_pdf_rag"
# #         )

# #     st.success(
# # #         "Chunks stored in Chroma successfully!"
# # #     )

# # # else:

# # #     st.info("Please upload a PDF file.")


# # #           < Retriever ka complete final code >          #

# # import streamlit as st
# # import tempfile

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma


# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG App")

# # st.write(
# #     "Upload a PDF and retrieve relevant text chunks."
# # )


# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success("PDF uploaded successfully!")

# #     # Step 1: Create a temporary PDF file
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name

# #     st.write("Temporary file created successfully.")

# #     # Step 2: Load PDF using PyPDFLoader
# #     loader = PyPDFLoader(pdf_path)

# #     documents = loader.load()

# #     st.write("Total pages:", len(documents))

# #     # Step 3: Create text splitter
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     # Step 4: Split PDF into chunks
# #     chunks = splitter.split_documents(documents)

# #     st.write("Total chunks:", len(chunks))

# #     # Step 5: Display first chunk
# #     if chunks:

# #         st.subheader("First Chunk")

# #         st.write(
# #             chunks[0].page_content
# #         )

# #         st.write("Chunk metadata:")

# #         st.write(
# #             chunks[0].metadata
# #         )

# #     # Step 6: Create embedding model
# #     with st.spinner("Creating embeddings..."):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )

# #     # Step 7: Store chunks and embeddings in Chroma
# #     with st.spinner("Storing chunks in Chroma..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name="streamlit_pdf_rag"
# #         )

# #     st.success(
# #         "Chunks stored in Chroma successfully!"
# #     )

# #     # Step 8: Create retriever
# #     retriever = vector_store.as_retriever(
# #         search_kwargs={"k": 3}
# #     )

# #     # Step 9: Ask a question
# #     question = st.text_input(
# #         "Ask a question about your PDF"
# #     )

# #     if question:

# #         # Step 10: Retrieve relevant chunks
# #         relevant_chunks = retriever.invoke(
# #             question
# #         )

# #         st.subheader("Retrieved Chunks")

# #         st.write(
# #             "Number of retrieved chunks:",
# #             len(relevant_chunks)
# #         )

# #         # Step 11: Display retrieved chunks
# #         for i, chunk in enumerate(
# #             relevant_chunks,
# #             start=1
# #         ):

# #             st.write(f"### Chunk {i}")

# #             st.write(
# #                 chunk.page_content
# #             )

# #             st.write(
# #                 "Metadata:",
# #                 chunk.metadata
# #             )

# # else:

# #     st.info("Please upload a PDF file.")



# #     #           < Retriever + Prompt + LLM → Final Answer >         #




# # import streamlit as st
# # import tempfile

# # from pathlib import Path
# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma

# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser


# # # Load environment variables
# # project_folder = Path(__file__).resolve().parent

# # load_dotenv(
# #     project_folder / ".env"
# # )


# # # Streamlit page configuration
# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )


# # st.title("📄 PDF RAG App")

# # st.write(
# #     "Upload a PDF and ask questions about it."
# # )


# # # PDF upload
# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success(
# #         "PDF uploaded successfully!"
# #     )

# #     # Step 1: Create temporary PDF file
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name


# #     # Step 2: Load PDF
# #     loader = PyPDFLoader(
# #         pdf_path
# #     )

# #     documents = loader.load()


# #     # Step 3: Split documents into chunks
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = splitter.split_documents(
# #         documents
# #     )


# #     # Step 4: Create embeddings
# #     with st.spinner(
# #         "Creating embeddings..."
# #     ):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )


# #     # Step 5: Store chunks in Chroma
# #     with st.spinner(
# #         "Storing chunks in Chroma..."
# #     ):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name="streamlit_pdf_rag"
# #         )


# #     # Step 6: Create retriever
# #     retriever = vector_store.as_retriever(
# #         search_kwargs={
# #             "k": 3
# #         }
# #     )


# #     # Step 7: Create LLM
# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )


# #     # Step 8: Create prompt template
# #     prompt = PromptTemplate.from_template(
# #         """
# #         Answer the question using only the
# #         provided context.

# #         If the answer is not available in the
# #         context, say:

# #         "The information is not available
# #         in the provided document."

# #         Do not use outside knowledge.

# #         Context:
# #         {context}

# #         Question:
# #         {question}

# #         Answer:
# #         """
# #     )


# #     # Step 9: Create RAG chain
# #     rag_chain = (
# #         prompt
# #         | llm
# #         | StrOutputParser()
# #     )


# #     # Step 10: Ask a question
# #     question = st.text_input(
# #         "Ask a question about your PDF"
# #     )


# #     if question:

# #         with st.spinner(
# #             "Searching and generating answer..."
# #         ):

# #             # Retrieve relevant chunks
# #             relevant_chunks = retriever.invoke(
# #                 question
# #             )


# #             # Combine retrieved chunks
# #             context = "\n\n".join(
# #                 chunk.page_content
# #                 for chunk in relevant_chunks
# #             )


# #             # Generate final answer
# #             response = rag_chain.invoke(
# #                 {
# #                     "context": context,
# #                     "question": question
# #                 }
# #             )


# #         # Display final answer
# #         st.subheader("Answer")

# #         st.write(response)


# # else:

# #     st.info(
# #         "Please upload a PDF file."
# #     )


# #               <source citation >             #        #
    

# # import streamlit as st
# # import tempfile

# # from pathlib import Path
# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma

# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser


# # # ==========================================
# # # 1. Load environment variables
# # # ==========================================

# # project_folder = Path(__file__).resolve().parent

# # load_dotenv(
# #     project_folder / ".env"
# # )


# # # ==========================================
# # # 2. Streamlit page configuration
# # # ==========================================

# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG App")

# # st.write(
# #     "Upload a PDF and ask questions about it."
# # )


# # # ==========================================
# # # 3. PDF upload
# # # ==========================================

# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success(
# #         "PDF uploaded successfully!"
# #     )


# #     # ==========================================
# #     # 4. Create temporary PDF file
# #     # ==========================================

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name


# #     # ==========================================
# #     # 5. Load PDF
# #     # ==========================================

# #     with st.spinner(
# #         "Loading PDF..."
# #     ):

# #         loader = PyPDFLoader(
# #             pdf_path
# #         )

# #         documents = loader.load()


# #     st.write(
# #         "Total pages:",
# #         len(documents)
# #     )


# #     # ==========================================
# #     # 6. Split documents into chunks
# #     # ==========================================

# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = splitter.split_documents(
# #         documents
# #     )


# #     st.write(
# #         "Total chunks:",
# #         len(chunks)
# #     )


# #     # ==========================================
# #     # 7. Create embeddings
# #     # ==========================================

# #     with st.spinner(
# #         "Creating embeddings..."
# #     ):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )


# #     # ==========================================
# #     # 8. Store chunks in ChromaDB
# #     # ==========================================

# #     with st.spinner(
# #         "Storing chunks in ChromaDB..."
# #     ):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name="streamlit_pdf_rag"
# #         )


# #     st.success(
# #         "PDF processed successfully!"
# #     )


# #     # ==========================================
# #     # 9. Create retriever
# #     # ==========================================

# #     retriever = vector_store.as_retriever(
# #         search_kwargs={
# #             "k": 3
# #         }
# #     )


# #     # ==========================================
# #     # 10. Create Groq LLM
# #     # ==========================================

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )


# #     # ==========================================
# #     # 11. Create prompt template
# #     # ==========================================

# #     prompt = PromptTemplate.from_template(
# #         """
# #         You are a document question-answering assistant.

# #         Answer the question ONLY using the
# #         provided context.

# #         Important rules:

# #         1. Do not use your own knowledge.
# #         2. Do not make assumptions.
# #         3. If the context does not clearly contain
# #            the answer, respond with:

# #            The information is not available
# #            in the provided document.

# #         4. Do not create an answer from unrelated
# #            context.

# #         Context:
# #         {context}

# #         Question:
# #         {question}

# #         Answer:
# #         """
# #     )


# #     # ==========================================
# #     # 12. Create RAG chain
# #     # ==========================================

# #     rag_chain = (
# #         prompt
# #         | llm
# #         | StrOutputParser()
# #     )


# #     # ==========================================
# #     # 13. User question
# #     # ==========================================

# #     question = st.text_input(
# #         "Ask a question about your PDF"
# #     )


# #     if question:

# #         with st.spinner(
# #             "Searching and generating answer..."
# #         ):


# #             # ==========================================
# #             # 14. Retrieve relevant chunks
# #             # ==========================================

# #             relevant_chunks = retriever.invoke(
# #                 question
# #             )


# #             # ==========================================
# #             # 15. Combine chunks into context
# #             # ==========================================

# #             context = "\n\n".join(
# #                 chunk.page_content
# #                 for chunk in relevant_chunks
# #             )


# #             # ==========================================
# #             # 16. Generate final answer
# #             # ==========================================

# #             response = rag_chain.invoke(
# #                 {
# #                     "context": context,
# #                     "question": question
# #                 }
# #             )


# #         # ==========================================
# #         # 17. Display final answer
# #         # ==========================================

# #         st.subheader("Answer")

# #         st.write(
# #             response
# #         )


# #         # ==========================================
# #         # 18. Display source citations
# #         # ==========================================

# #         st.subheader("Sources")

# #         source_pages = set()


# #         for chunk in relevant_chunks:

# #             page_number = (
# #                 chunk.metadata.get(
# #                     "page",
# #                     0
# #                 ) + 1
# #             )

# #             source_pages.add(
# #                 page_number
# #             )


# #         for page in sorted(
# #             source_pages
# #         ):

# #             st.write(
# #                 f"📄 Page {page}"
# #             )


# # else:

# #     st.info(
# #         "Please upload a PDF file."
# #     )



# #               < Source Content Verification >             #



# # import streamlit as st
# # import tempfile
# # import uuid

# # from pathlib import Path
# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma

# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser


# # # ==========================================
# # # 1. Load environment variables
# # # ==========================================

# # project_folder = Path(__file__).resolve().parent

# # load_dotenv(project_folder / ".env")


# # # ==========================================
# # # 2. Streamlit configuration
# # # ==========================================

# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG App")

# # st.write(
# #     "Upload a PDF and ask questions about it."
# # )


# # # ==========================================
# # # 3. PDF upload
# # # ==========================================

# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success("PDF uploaded successfully!")


# #     # ==========================================
# #     # 4. Create temporary PDF file
# #     # ==========================================

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name


# #     # ==========================================
# #     # 5. Load PDF
# #     # ==========================================

# #     with st.spinner("Loading PDF..."):

# #         loader = PyPDFLoader(pdf_path)

# #         documents = loader.load()


# #     st.write(
# #         "Total pages:",
# #         len(documents)
# #     )


# #     # ==========================================
# #     # 6. Split PDF into chunks
# #     # ==========================================

# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = splitter.split_documents(
# #         documents
# #     )


# #     st.write(
# #         "Total chunks:",
# #         len(chunks)
# #     )


# #     # ==========================================
# #     # 7. Create embeddings
# #     # ==========================================

# #     with st.spinner("Creating embeddings..."):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )


# #     # ==========================================
# #     # 8. Create unique Chroma collection
# #     # ==========================================

# #     collection_name = (
# #         "pdf_rag_"
# #         + uuid.uuid4().hex
# #     )


# #     with st.spinner("Storing chunks in ChromaDB..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name=collection_name
# #         )


# #     st.success("PDF processed successfully!")


# #     # ==========================================
# #     # 9. Create MMR retriever
# #     # ==========================================

# #     retriever = vector_store.as_retriever(
# #         search_type="mmr",
# #         search_kwargs={
# #             "k": 3,
# #             "fetch_k": 10,
# #             "lambda_mult": 0.7
# #         }
# #     )


# #     # ==========================================
# #     # 10. Create Groq LLM
# #     # ==========================================

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )


# #     # ==========================================
# #     # 11. Create prompt template
# #     # ==========================================

# #     prompt = PromptTemplate.from_template(
# #         """
# #         You are a helpful PDF question-answering assistant.

# #         Answer the question ONLY using the provided context.

# #         Rules:
# #         1. Do not use outside knowledge.
# #         2. Do not make assumptions.
# #         3. Do not use unrelated information.
# #         4. Give a concise answer in 3 to 5 sentences
# #            when the question needs an explanation.
# #         5. Use bullet points when appropriate.
# #         6. If the answer is not clearly available
# #            in the context, say exactly:

# #            The information is not available
# #            in the provided document.

# #         Context:
# #         {context}

# #         Question:
# #         {question}

# #         Answer:
# #         """
# #     )


# #     # ==========================================
# #     # 12. Create RAG chain
# #     # ==========================================

# #     rag_chain = (
# #         prompt
# #         | llm
# #         | StrOutputParser()
# #     )


# #     # ==========================================
# #     # 13. User question
# #     # ==========================================

# #     question = st.text_input(
# #         "Ask a question about your PDF"
# #     )


# #     if question.strip():

# #         with st.spinner(
# #             "Searching and generating answer..."
# #         ):


# #             # ==========================================
# #             # 14. Retrieve relevant chunks
# #             # ==========================================

# #             relevant_chunks = retriever.invoke(
# #                 question
# #             )


# #             # ==========================================
# #             # 15. Remove duplicate chunks
# #             # ==========================================

# #             unique_chunks = []

# #             seen_chunks = set()


# #             for chunk in relevant_chunks:

# #                 chunk_text = (
# #                     chunk.page_content.strip()
# #                 )

# #                 if (
# #                     chunk_text
# #                     and chunk_text not in seen_chunks
# #                 ):

# #                     seen_chunks.add(
# #                         chunk_text
# #                     )

# #                     unique_chunks.append(
# #                         chunk
# #                     )


# #             # ==========================================
# #             # 16. Create context
# #             # ==========================================

# #             context = "\n\n".join(
# #                 chunk.page_content
# #                 for chunk in unique_chunks
# #             )


# #             # ==========================================
# #             # 17. Generate final answer
# #             # ==========================================

# #             response = rag_chain.invoke(
# #                 {
# #                     "context": context,
# #                     "question": question
# #                 }
# #             )


# #         # ==========================================
# #         # 18. Display answer
# #         # ==========================================

# #         st.subheader("Answer")

# #         st.write(response)


# #         # ==========================================
# #         # 19. Display sources
# #         # ==========================================

# #         st.subheader("Sources")


# #         if unique_chunks:

# #             displayed_sources = set()


# #             for index, chunk in enumerate(
# #                 unique_chunks,
# #                 start=1
# #             ):

# #                 page_number = (
# #                     chunk.metadata.get(
# #                         "page",
# #                         0
# #                     ) + 1
# #                 )

# #                 source_key = (
# #                     page_number,
# #                     chunk.page_content.strip()
# #                 )


# #                 if source_key in displayed_sources:

# #                     continue


# #                 displayed_sources.add(
# #                     source_key
# #                 )


# #                 with st.expander(
# #                     f"📄 Source {index} - Page {page_number}"
# #                 ):

# #                     st.write(
# #                         chunk.page_content
# #                     )


# #         else:

# #             st.info(
# #                 "No relevant sources were retrieved."
# #             )


# # else:

# #     st.info(
# #         "Please upload a PDF file."
# #     )


# #           < Compression Retriever >           # 



# # import streamlit as st
# # import tempfile
# # import uuid

# # from pathlib import Path
# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma

# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # ==========================================
# # # 1. Load environment variables
# # # ==========================================

# # project_folder = Path(__file__).resolve().parent

# # load_dotenv(
# #     project_folder / ".env"
# # )


# # # ==========================================
# # # 2. Streamlit configuration
# # # ==========================================

# # st.set_page_config(
# #     page_title="PDF RAG App",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG App")

# # st.write(
# #     "Upload a PDF and ask questions about it."
# # )


# # # ==========================================
# # # 3. PDF upload
# # # ==========================================

# # uploaded_file = st.file_uploader(
# #     "Choose a PDF file",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success(
# #         "PDF uploaded successfully!"
# #     )


# #     # ==========================================
# #     # 4. Create temporary PDF file
# #     # ==========================================

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temporary_file:

# #         temporary_file.write(
# #             uploaded_file.getvalue()
# #         )

# #         pdf_path = temporary_file.name


# #     # ==========================================
# #     # 5. Load PDF
# #     # ==========================================

# #     with st.spinner(
# #         "Loading PDF..."
# #     ):

# #         loader = PyPDFLoader(
# #             pdf_path
# #         )

# #         documents = loader.load()


# #     st.write(
# #         "Total pages:",
# #         len(documents)
# #     )


# #     # ==========================================
# #     # 6. Split PDF into chunks
# #     # ==========================================

# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = splitter.split_documents(
# #         documents
# #     )


# #     st.write(
# #         "Total chunks:",
# #         len(chunks)
# #     )


# #     # ==========================================
# #     # 7. Create embeddings
# #     # ==========================================

# #     with st.spinner(
# #         "Creating embeddings..."
# #     ):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )


# #     # ==========================================
# #     # 8. Create unique Chroma collection
# #     # ==========================================

# #     collection_name = (
# #         "pdf_rag_"
# #         + uuid.uuid4().hex
# #     )


# #     with st.spinner(
# #         "Storing chunks in ChromaDB..."
# #     ):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name=collection_name
# #         )


# #     st.success(
# #         "PDF processed successfully!"
# #     )


# #     # ==========================================
# #     # 9. Create Groq LLM
# #     # ==========================================

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )


# #     # ==========================================
# #     # 10. Create MMR retriever
# #     # ==========================================

# #     base_retriever = vector_store.as_retriever(
# #         search_type="mmr",
# #         search_kwargs={
# #             "k": 3,
# #             "fetch_k": 10,
# #             "lambda_mult": 0.7
# #         }
# #     )


# #     # ==========================================
# #     # 11. Create compression prompt
# #     # ==========================================

# #     compression_prompt = PromptTemplate.from_template(
# #         """
# #         You are a document relevance filter.

# #         Extract only the information from the
# #         context that is directly relevant to
# #         the user's question.

# #         Rules:
# #         1. Keep only relevant information.
# #         2. Remove unrelated information.
# #         3. Do not add outside knowledge.
# #         4. Preserve important facts and details.
# #         5. If the context has no relevant information,
# #            return exactly: EMPTY

# #         Context:
# #         {context}

# #         Question:
# #         {question}

# #         Relevant information:
# #         """
# #     )


# #     # ==========================================
# #     # 12. Create compression chain
# #     # ==========================================

# #     compression_chain = (
# #         compression_prompt
# #         | llm
# #         | StrOutputParser()
# #     )


# #     # ==========================================
# #     # 13. Compression function
# #     # ==========================================

# #     def compress_documents(
# #         question,
# #         documents
# #     ):

# #         compressed_documents = []

# #         for document in documents:

# #             compressed_text = (
# #                 compression_chain.invoke(
# #                     {
# #                         "context": document.page_content,
# #                         "question": question
# #                     }
# #                 )
# #             )

# #             compressed_text = (
# #                 compressed_text.strip()
# #             )


# #             if (
# #                 compressed_text
# #                 and compressed_text.upper() != "EMPTY"
# #             ):

# #                 compressed_documents.append(
# #                     Document(
# #                         page_content=compressed_text,
# #                         metadata=document.metadata
# #                     )
# #                 )


# #         return compressed_documents


# #     # ==========================================
# #     # 14. Create final answer prompt
# #     # ==========================================

# #     answer_prompt = PromptTemplate.from_template(
# #         """
# #         You are a helpful PDF question-answering assistant.

# #         Answer the question ONLY using the provided context.

# #         Rules:
# #         1. Do not use outside knowledge.
# #         2. Do not make assumptions.
# #         3. Do not use unrelated information.
# #         4. Give a concise answer in 3 to 5 sentences
# #            when an explanation is needed.
# #         5. Use bullet points when appropriate.
# #         6. If the answer is not clearly available
# #            in the context, say:

# #            The information is not available
# #            in the provided document.

# #         Context:
# #         {context}

# #         Question:
# #         {question}

# #         Answer:
# #         """
# #     )


# #     # ==========================================
# #     # 15. Create final RAG chain
# #     # ==========================================

# #     rag_chain = (
# #         answer_prompt
# #         | llm
# #         | StrOutputParser()
# #     )


# #     # ==========================================
# #     # 16. User question
# #     # ==========================================

# #     question = st.text_input(
# #         "Ask a question about your PDF"
# #     )


# #     if question.strip():

# #         with st.spinner(
# #             "Retrieving relevant chunks..."
# #         ):

# #             # ==========================================
# #             # 17. Retrieve original chunks
# #             # ==========================================

# #             retrieved_chunks = (
# #                 base_retriever.invoke(
# #                     question
# #                 )
# #             )


# #         with st.spinner(
# #             "Compressing context..."
# #         ):

# #             # ==========================================
# #             # 18. Compress retrieved chunks
# #             # ==========================================

# #             relevant_chunks = (
# #                 compress_documents(
# #                     question,
# #                     retrieved_chunks
# #                 )
# #             )


# #         # ==========================================
# #         # 19. Remove duplicate chunks
# #         # ==========================================

# #         unique_chunks = []

# #         seen_chunks = set()


# #         for chunk in relevant_chunks:

# #             chunk_text = (
# #                 chunk.page_content.strip()
# #             )


# #             if (
# #                 chunk_text
# #                 and chunk_text not in seen_chunks
# #             ):

# #                 seen_chunks.add(
# #                     chunk_text
# #                 )

# #                 unique_chunks.append(
# #                     chunk
# #                 )


# #         # ==========================================
# #         # 20. Create final context
# #         # ==========================================

# #         context = "\n\n".join(
# #             chunk.page_content
# #             for chunk in unique_chunks
# #         )


# #         # ==========================================
# #         # 21. Generate final answer
# #         # ==========================================

# #         if context.strip():

# #             with st.spinner(
# #                 "Generating final answer..."
# #             ):

# #                 response = rag_chain.invoke(
# #                     {
# #                         "context": context,
# #                         "question": question
# #                     }
# #                 )

# #         else:

# #             response = (
# #                 "The information is not available "
# #                 "in the provided document."
# #             )


# #         # ==========================================
# #         # 22. Display answer
# #         # ==========================================

# #         st.subheader(
# #             "Answer"
# #         )

# #         st.write(
# #             response
# #         )


# #         # ==========================================
# #         # 23. Display sources
# #         # ==========================================

# #         st.subheader(
# #             "Sources"
# #         )


# #         if unique_chunks:

# #             displayed_sources = set()


# #             for index, chunk in enumerate(
# #                 unique_chunks,
# #                 start=1
# #             ):

# #                 page_number = (
# #                     chunk.metadata.get(
# #                         "page",
# #                         0
# #                     ) + 1
# #                 )


# #                 source_key = (
# #                     page_number,
# #                     chunk.page_content.strip()
# #                 )


# #                 if source_key in displayed_sources:

# #                     continue


# #                 displayed_sources.add(
# #                     source_key
# #                 )


# #                 with st.expander(
# #                     f"📄 Source {index} - Page {page_number}"
# #                 ):

# #                     st.write(
# #                         chunk.page_content
# #                     )


# #         else:

# #             st.info(
# #                 "No relevant sources were retrieved."
# #             )


# # else:

# #     st.info(
# #         "Please upload a PDF file."
# #     )



# #               < Chat History ka complete code integration >             #



# # import streamlit as st
# # import tempfile
# # import uuid
# # from pathlib import Path

# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq

# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser


# # # --------------------------------------------------
# # # 1. Page Configuration
# # # --------------------------------------------------

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📚",
# #     layout="wide"
# # )

# # st.title("📚 PDF RAG Chatbot")
# # st.write("Upload a PDF and ask multiple questions about it.")


# # # --------------------------------------------------
# # # 2. Load Environment Variables
# # # --------------------------------------------------

# # project_folder = Path(__file__).resolve().parent
# # load_dotenv(project_folder / ".env")


# # # --------------------------------------------------
# # # 3. Initialize Chat History
# # # --------------------------------------------------

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []


# # # --------------------------------------------------
# # # 4. New Chat Button
# # # --------------------------------------------------

# # if st.button("🗑️ Clear Chat History"):
# #     st.session_state.chat_history = []
# #     st.rerun()


# # # --------------------------------------------------
# # # 5. PDF Upload
# # # --------------------------------------------------

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )


# # if uploaded_file is not None:

# #     st.success(f"Uploaded: {uploaded_file.name}")


# #     # --------------------------------------------------
# #     # 6. Save Uploaded PDF Temporarily
# #     # --------------------------------------------------

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temp_file:

# #         temp_file.write(uploaded_file.getvalue())
# #         pdf_path = temp_file.name


# #     # --------------------------------------------------
# #     # 7. Load PDF
# #     # --------------------------------------------------

# #     loader = PyPDFLoader(pdf_path)
# #     documents = loader.load()


# #     # --------------------------------------------------
# #     # 8. Split Documents into Chunks
# #     # --------------------------------------------------

# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = text_splitter.split_documents(documents)


# #     # --------------------------------------------------
# #     # 9. Create Embeddings
# #     # --------------------------------------------------

# #     embeddings = HuggingFaceEmbeddings(
# #         model_name="sentence-transformers/all-MiniLM-L6-v2"
# #     )


# #     # --------------------------------------------------
# #     # 10. Create Chroma Vector Store
# #     # --------------------------------------------------

# #     vector_store = Chroma.from_documents(
# #         documents=chunks,
# #         embedding=embeddings,
# #         collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# #     )


# #     # --------------------------------------------------
# #     # 11. Create MMR Retriever
# #     # --------------------------------------------------

# #     retriever = vector_store.as_retriever(
# #         search_type="mmr",
# #         search_kwargs={
# #             "k": 3,
# #             "fetch_k": 10,
# #             "lambda_mult": 0.7
# #         }
# #     )


# #     # --------------------------------------------------
# #     # 12. Initialize LLM
# #     # --------------------------------------------------

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )


# #     # --------------------------------------------------
# #     # 13. Create Final RAG Prompt
# #     # --------------------------------------------------

# #     rag_prompt = PromptTemplate.from_template(
# #         """
# # You are a helpful PDF assistant.

# # Answer the user's question using ONLY the provided PDF context
# # and conversation history.

# # Rules:
# # 1. Do not invent information.
# # 2. If the answer is not available in the PDF context, say:
# #    "Information not available in the uploaded PDF."
# # 3. Keep the answer clear and concise.
# # 4. Use conversation history only to understand references
# #    such as "it", "this", or "that".
# # 5. Do not answer unrelated questions using outside knowledge.

# # Conversation History:
# # {chat_history}

# # PDF Context:
# # {context}

# # Current Question:
# # {question}

# # Answer:
# # """
# #     )


# #     # --------------------------------------------------
# #     # 14. Create RAG Chain
# #     # --------------------------------------------------

# #     rag_chain = rag_prompt | llm | StrOutputParser()


# #     # --------------------------------------------------
# #     # 15. Display Previous Chat History
# #     # --------------------------------------------------

# #     st.subheader("💬 Conversation")

# #     for message in st.session_state.chat_history:

# #         if message["role"] == "user":

# #             with st.chat_message("user"):
# #                 st.write(message["content"])

# #         else:

# #             with st.chat_message("assistant"):
# #                 st.write(message["content"])


# #     # --------------------------------------------------
# #     # 16. User Question Input
# #     # --------------------------------------------------

# #     question = st.chat_input(
# #         "Ask a question about your PDF..."
# #     )


# #     if question:

# #         # --------------------------------------------------
# #         # 17. Retrieve Relevant Chunks
# #         # --------------------------------------------------

# #         retrieved_chunks = retriever.invoke(question)


# #         # --------------------------------------------------
# #         # 18. Remove Duplicate Chunks
# #         # --------------------------------------------------

# #         unique_chunks = []
# #         seen_chunks = set()

# #         for chunk in retrieved_chunks:

# #             text = chunk.page_content.strip()

# #             if text not in seen_chunks:

# #                 seen_chunks.add(text)
# #                 unique_chunks.append(chunk)


# #         # --------------------------------------------------
# #         # 19. Build PDF Context
# #         # --------------------------------------------------

# #         context = "\n\n".join(
# #             chunk.page_content
# #             for chunk in unique_chunks
# #         )


# #         # --------------------------------------------------
# #         # 20. Build Conversation History
# #         # --------------------------------------------------

# #         history_text = "\n".join(
# #             f"{message['role']}: {message['content']}"
# #             for message in st.session_state.chat_history
# #         )


# #         # --------------------------------------------------
# #         # 21. Generate Final Answer
# #         # --------------------------------------------------

# #         with st.spinner("Thinking..."):

# #             answer = rag_chain.invoke(
# #                 {
# #                     "chat_history": history_text,
# #                     "context": context,
# #                     "question": question
# #                 }
# #             )


# #         # --------------------------------------------------
# #         # 22. Save User Question and AI Answer
# #         # --------------------------------------------------

# #         st.session_state.chat_history.append(
# #             {
# #                 "role": "user",
# #                 "content": question
# #             }
# #         )

# #         st.session_state.chat_history.append(
# #             {
# #                 "role": "assistant",
# #                 "content": answer
# #             }
# #         )


# #         # --------------------------------------------------
# #         # 23. Display Latest Answer
# #         # --------------------------------------------------

# #         with st.chat_message("user"):
# #             st.write(question)

# #         with st.chat_message("assistant"):
# #             st.write(answer)


# #         # --------------------------------------------------
# #         # 24. Display Sources
# #         # --------------------------------------------------

# #         st.subheader("📌 Sources")

# #         for index, chunk in enumerate(unique_chunks):

# #             page_number = chunk.metadata.get("page", 0) + 1

# #             with st.expander(
# #                 f"Source {index + 1} — Page {page_number}"
# #             ):

# #                 st.write(chunk.page_content)


# #               < Final code: Relevance Filtering + Exact Compression>  #



# # import streamlit as st
# # import tempfile
# # import uuid
# # from pathlib import Path

# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq

# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # ==================================================
# # # 1. PAGE CONFIGURATION
# # # ==================================================

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📚",
# #     layout="wide"
# # )

# # st.title("📚 PDF RAG Chatbot")
# # st.write("Upload a PDF and ask questions about its content.")


# # # ==================================================
# # # 2. LOAD ENVIRONMENT VARIABLES
# # # ==================================================

# # project_folder = Path(__file__).resolve().parent

# # load_dotenv(project_folder / ".env")


# # # ==================================================
# # # 3. CHAT HISTORY
# # # ==================================================

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []


# # if st.button("🗑️ Clear Chat History"):

# #     st.session_state.chat_history = []

# #     st.rerun()


# # # ==================================================
# # # 4. PDF UPLOAD
# # # ==================================================

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )


# # if uploaded_file is None:

# #     st.info("Please upload a PDF to start.")

# #     st.stop()


# # st.success(f"Uploaded: {uploaded_file.name}")


# # # ==================================================
# # # 5. SAVE PDF TEMPORARILY
# # # ==================================================

# # with tempfile.NamedTemporaryFile(
# #     delete=False,
# #     suffix=".pdf"
# # ) as temp_file:

# #     temp_file.write(uploaded_file.getvalue())

# #     pdf_path = temp_file.name


# # # ==================================================
# # # 6. LOAD PDF
# # # ==================================================

# # loader = PyPDFLoader(pdf_path)

# # documents = loader.load()


# # # ==================================================
# # # 7. TEXT CHUNKING
# # # ==================================================

# # text_splitter = RecursiveCharacterTextSplitter(
# #     chunk_size=500,
# #     chunk_overlap=50
# # )

# # chunks = text_splitter.split_documents(documents)


# # # ==================================================
# # # 8. EMBEDDINGS
# # # ==================================================

# # embeddings = HuggingFaceEmbeddings(
# #     model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )


# # # ==================================================
# # # 9. CHROMA VECTOR STORE
# # # ==================================================

# # vector_store = Chroma.from_documents(
# #     documents=chunks,
# #     embedding=embeddings,
# #     collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# # )


# # # ==================================================
# # # 10. MMR RETRIEVER
# # # ==================================================

# # # MMR tries to retrieve relevant and diverse chunks.
# # # It reduces duplicate/similar chunks.
# # # MMR alone does NOT guarantee that every chunk is relevant.

# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 5,
# #         "fetch_k": 15,
# #         "lambda_mult": 0.7
# #     }
# # )


# # # ==================================================
# # # 11. INITIALIZE LLM
# # # ==================================================

# # llm = ChatGroq(
# #     model="openai/gpt-oss-20b",
# #     temperature=0
# # )


# # # ==================================================
# # # 12. RELEVANCE GRADING PROMPT
# # # ==================================================

# # relevance_prompt = PromptTemplate.from_template(
# #     """
# # You are a strict relevance classifier.

# # Decide whether the given PDF context contains information
# # that can help answer the user's question.

# # Return ONLY one of these exact outputs:

# # RELEVANT
# # NOT_RELEVANT

# # Do not explain your decision.

# # PDF Context:
# # {context}

# # User Question:
# # {question}

# # Decision:
# # """
# # )


# # relevance_chain = (
# #     relevance_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # ==================================================
# # # 13. FILTER RELEVANT DOCUMENTS
# # # ==================================================

# # def filter_relevant_documents(question, documents):

# #     relevant_documents = []

# #     for document in documents:

# #         result = relevance_chain.invoke(
# #             {
# #                 "context": document.page_content,
# #                 "question": question
# #             }
# #         ).strip().upper()

# #         # Exact check avoids treating NOT_RELEVANT
# #         # as RELEVANT.

# #         if result == "RELEVANT":

# #             relevant_documents.append(document)

# #     return relevant_documents


# # # ==================================================
# # # 14. EXACT CONTEXT COMPRESSION
# # # ==================================================

# # compression_prompt = PromptTemplate.from_template(
# #     """
# # You are an extractive context compressor.

# # Your task is to extract only the exact sentences
# # from the PDF context that help answer the question.

# # STRICT RULES:
# # 1. Copy sentences exactly from the PDF context.
# # 2. Do not rewrite or paraphrase.
# # 3. Do not add new information.
# # 4. Do not make assumptions.
# # 5. If no exact relevant sentence exists, return EMPTY.
# # 6. Return only the extracted sentences or EMPTY.

# # PDF Context:
# # {context}

# # Question:
# # {question}

# # Extracted Text:
# # """
# # )


# # compression_chain = (
# #     compression_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def compress_documents(question, documents):

# #     compressed_documents = []

# #     for document in documents:

# #         compressed_text = compression_chain.invoke(
# #             {
# #                 "context": document.page_content,
# #                 "question": question
# #             }
# #         ).strip()

# #         if not compressed_text:
# #             continue

# #         if compressed_text.upper() == "EMPTY":
# #             continue

# #         # Preserve the original document metadata.
# #         # This keeps the original page number.

# #         compressed_document = Document(
# #             page_content=compressed_text,
# #             metadata=document.metadata
# #         )

# #         compressed_documents.append(compressed_document)

# #     return compressed_documents


# # # ==================================================
# # # 15. FINAL RAG PROMPT
# # # ==================================================

# # rag_prompt = PromptTemplate.from_template(
# #     """
# # You are a helpful PDF assistant.

# # Answer the question using ONLY the provided PDF context.

# # Conversation history is provided only to understand
# # references such as "it", "this", or "that".

# # STRICT RULES:
# # 1. Do not use outside knowledge.
# # 2. Do not invent information.
# # 3. If the answer is not present in the context, return exactly:
# #    Information not available in the uploaded PDF.
# # 4. Keep the answer clear and concise.
# # 5. Do not mention sources that are not present in the context.

# # Conversation History:
# # {chat_history}

# # PDF Context:
# # {context}

# # Current Question:
# # {question}

# # Answer:
# # """
# # )


# # rag_chain = (
# #     rag_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # ==================================================
# # # 16. DISPLAY PREVIOUS CHAT HISTORY
# # # ==================================================

# # st.subheader("💬 Conversation")


# # for message in st.session_state.chat_history:

# #     with st.chat_message(message["role"]):

# #         st.write(message["content"])


# # # ==================================================
# # # 17. USER QUESTION
# # # ==================================================

# # question = st.chat_input(
# #     "Ask a question about your PDF..."
# # )


# # if question:

# #     # --------------------------------------------------
# #     # A. RETRIEVE CHUNKS USING MMR
# #     # --------------------------------------------------

# #     retrieved_chunks = retriever.invoke(question)


# #     # --------------------------------------------------
# #     # B. REMOVE DUPLICATE CHUNKS
# #     # --------------------------------------------------

# #     unique_chunks = []

# #     seen_chunks = set()

# #     for chunk in retrieved_chunks:

# #         text = chunk.page_content.strip()

# #         if text not in seen_chunks:

# #             seen_chunks.add(text)

# #             unique_chunks.append(chunk)


# #     # --------------------------------------------------
# #     # C. RELEVANCE FILTERING
# #     # --------------------------------------------------

# #     with st.spinner("Checking document relevance..."):

# #         relevant_chunks = filter_relevant_documents(
# #             question,
# #             unique_chunks
# #         )


# #     # --------------------------------------------------
# #     # D. COMPRESS ONLY RELEVANT CHUNKS
# #     # --------------------------------------------------

# #     compressed_chunks = []

# #     if relevant_chunks:

# #         with st.spinner("Extracting relevant context..."):

# #             compressed_chunks = compress_documents(
# #                 question,
# #                 relevant_chunks
# #             )


# #     # --------------------------------------------------
# #     # E. BUILD CONVERSATION HISTORY
# #     # --------------------------------------------------

# #     history_text = "\n".join(
# #         f"{message['role']}: {message['content']}"
# #         for message in st.session_state.chat_history
# #     )


# #     # --------------------------------------------------
# #     # F. GENERATE ANSWER ONLY IF CONTEXT EXISTS
# #     # --------------------------------------------------

# #     unavailable_message = (
# #         "Information not available in the uploaded PDF."
# #     )


# #     if not compressed_chunks:

# #         answer = unavailable_message

# #     else:

# #         context = "\n\n".join(
# #             document.page_content
# #             for document in compressed_chunks
# #         )

# #         with st.spinner("Generating answer..."):

# #             answer = rag_chain.invoke(
# #                 {
# #                     "chat_history": history_text,
# #                     "context": context,
# #                     "question": question
# #                 }
# #             ).strip()


# #     # --------------------------------------------------
# #     # G. SAVE CHAT HISTORY
# #     # --------------------------------------------------

# #     st.session_state.chat_history.append(
# #         {
# #             "role": "user",
# #             "content": question
# #         }
# #     )

# #     st.session_state.chat_history.append(
# #         {
# #             "role": "assistant",
# #             "content": answer
# #         }
# #     )


# #     # --------------------------------------------------
# #     # H. DISPLAY LATEST ANSWER
# #     # --------------------------------------------------

# #     with st.chat_message("user"):

# #         st.write(question)


# #     with st.chat_message("assistant"):

# #         st.write(answer)


# #     # --------------------------------------------------
# #     # I. DISPLAY SOURCES ONLY IF ANSWER IS AVAILABLE
# #     # --------------------------------------------------

# #     answer_is_unavailable = (
# #         answer.strip().lower()
# #         == unavailable_message.lower()
# #     )


# #     if compressed_chunks and not answer_is_unavailable:

# #         st.subheader("📌 Sources")

# #         for index, compressed_document in enumerate(
# #             compressed_chunks
# #         ):

# #             page_number = (
# #                 compressed_document.metadata.get("page", 0) + 1
# #             )

# #             with st.expander(
# #                 f"Source {index + 1} — Page {page_number}"
# #             ):

# #                 st.write(
# #                     "Relevant extracted text:"
# #                 )

# #                 st.write(
# #                     compressed_document.page_content
# #                 )




# #               < Error Handling >                      #


# # import streamlit as st
# # import tempfile
# # import uuid
# # from pathlib import Path

# # from dotenv import load_dotenv
# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # -----------------------------
# # # CONFIGURATION
# # # -----------------------------

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📄",
# #     layout="wide"
# # )

# # st.title("📄 PDF RAG Chatbot")

# # project_folder = Path(__file__).resolve().parent
# # load_dotenv(project_folder / ".env")


# # # -----------------------------
# # # SESSION STATE
# # # -----------------------------

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []


# # if st.button("🗑️ Clear Chat History"):
# #     st.session_state.chat_history = []
# #     st.rerun()


# # # -----------------------------
# # # PDF UPLOAD
# # # -----------------------------

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )


# # if uploaded_file is None:
# #     st.info("Please upload a PDF to start chatting.")
# #     st.stop()


# # # -----------------------------
# # # SAVE PDF TEMPORARILY
# # # -----------------------------

# # pdf_bytes = uploaded_file.getvalue()

# # try:
# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temp_file:

# #         temp_file.write(pdf_bytes)
# #         pdf_path = temp_file.name

# # except Exception:
# #     st.error("Unable to save the uploaded PDF.")
# #     st.stop()


# # # -----------------------------
# # # LOAD PDF
# # # -----------------------------

# # try:
# #     with st.spinner("Loading PDF..."):

# #         loader = PyPDFLoader(pdf_path)
# #         documents = loader.load()

# #     st.success("PDF loaded successfully!")

# # except Exception:
# #     st.error(
# #         "Unable to read this PDF. "
# #         "Please upload a valid PDF file."
# #     )
# #     st.stop()


# # # -----------------------------
# # # SPLIT DOCUMENTS
# # # -----------------------------

# # try:
# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = text_splitter.split_documents(documents)

# #     if not chunks:
# #         st.error("No readable text found in this PDF.")
# #         st.stop()

# # except Exception:
# #     st.error("Error while splitting the PDF.")
# #     st.stop()


# # # -----------------------------
# # # EMBEDDINGS
# # # -----------------------------

# # try:
# #     with st.spinner("Creating embeddings..."):

# #         embeddings = HuggingFaceEmbeddings(
# #             model_name="sentence-transformers/all-MiniLM-L6-v2"
# #         )

# # except Exception:
# #     st.error("Error while loading the embedding model.")
# #     st.stop()


# # # -----------------------------
# # # VECTOR DATABASE
# # # -----------------------------

# # try:
# #     with st.spinner("Creating vector database..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# #         )

# # except Exception:
# #     st.error("Error while creating the vector database.")
# #     st.stop()


# # # -----------------------------
# # # RETRIEVER WITH MMR
# # # -----------------------------

# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 5,
# #         "fetch_k": 15,
# #         "lambda_mult": 0.7
# #     }
# # )


# # # -----------------------------
# # # LLM
# # # -----------------------------

# # try:
# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )

# # except Exception:
# #     st.error("Error while connecting to the AI model.")
# #     st.stop()


# # # -----------------------------
# # # RELEVANCE CHECK
# # # -----------------------------

# # relevance_prompt = PromptTemplate.from_template(
# #     """
# # You are a document relevance checker.

# # Question:
# # {question}

# # Document:
# # {document}

# # Check whether the document contains information
# # that can help answer the question.

# # Return ONLY one of these:
# # RELEVANT
# # NOT_RELEVANT
# # """
# # )

# # relevance_chain = (
# #     relevance_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def filter_relevant_documents(question, documents):

# #     relevant_documents = []

# #     for document in documents:

# #         try:
# #             result = relevance_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip().upper()

# #             if result == "RELEVANT":
# #                 relevant_documents.append(document)

# #         except Exception:
# #             continue

# #     return relevant_documents


# # # -----------------------------
# # # CONTEXT COMPRESSION
# # # -----------------------------

# # compression_prompt = PromptTemplate.from_template(
# #     """
# # You are an extractive document compressor.

# # Question:
# # {question}

# # Document:
# # {document}

# # Instructions:
# # - Extract only exact sentences relevant to the question.
# # - Do not paraphrase.
# # - Do not add new information.
# # - If no relevant information exists, return EMPTY.
# # - Return only the extracted text.
# # """
# # )

# # compression_chain = (
# #     compression_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def compress_documents(question, documents):

# #     compressed_documents = []

# #     for document in documents:

# #         try:
# #             compressed_text = compression_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip()

# #             if (
# #                 compressed_text
# #                 and compressed_text.upper() != "EMPTY"
# #             ):

# #                 compressed_documents.append(
# #                     Document(
# #                         page_content=compressed_text,
# #                         metadata=document.metadata
# #                     )
# #                 )

# #         except Exception:
# #             continue

# #     return compressed_documents


# # # -----------------------------
# # # FINAL RAG PROMPT
# # # -----------------------------

# # rag_prompt = PromptTemplate.from_template(
# #     """
# # You are a helpful PDF question-answering assistant.

# # Answer the question using ONLY the provided context.

# # Conversation History:
# # {history}

# # Context:
# # {context}

# # Question:
# # {question}

# # Rules:
# # - Use only the given context.
# # - Do not invent information.
# # - Keep the answer concise and clear.
# # - If the answer is not present in the context,
# #   respond exactly:
# #   Information not available in the uploaded document.
# # """
# # )

# # rag_chain = (
# #     rag_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # -----------------------------
# # # CHAT HISTORY DISPLAY
# # # -----------------------------

# # for message in st.session_state.chat_history:

# #     with st.chat_message(message["role"]):
# #         st.markdown(message["content"])


# # # -----------------------------
# # # USER QUESTION
# # # -----------------------------

# # question = st.chat_input(
# #     "Ask a question about your PDF..."
# # )


# # if question:

# #     question = question.strip()

# #     if not question:
# #         st.warning("Please enter a valid question.")
# #         st.stop()

# #     with st.chat_message("user"):
# #         st.markdown(question)

# #     # Save user message
# #     st.session_state.chat_history.append({
# #         "role": "user",
# #         "content": question
# #     })

# #     # -----------------------------
# #     # RETRIEVAL
# #     # -----------------------------

# #     try:

# #         with st.spinner("Searching document..."):

# #             retrieved_documents = retriever.invoke(question)

# #     except Exception:

# #         st.error("Error while searching the document.")
# #         st.stop()


# #     # -----------------------------
# #     # REMOVE DUPLICATES
# #     # -----------------------------

# #     unique_documents = []
# #     seen_text = set()

# #     for document in retrieved_documents:

# #         text = document.page_content.strip()

# #         if text not in seen_text:

# #             seen_text.add(text)
# #             unique_documents.append(document)


# #     # -----------------------------
# #     # RELEVANCE FILTERING
# #     # -----------------------------

# #     with st.spinner("Checking relevant information..."):

# #         relevant_documents = filter_relevant_documents(
# #             question,
# #             unique_documents
# #         )


# #     # -----------------------------
# #     # CONTEXT COMPRESSION
# #     # -----------------------------

# #     with st.spinner("Preparing relevant context..."):

# #         compressed_documents = compress_documents(
# #             question,
# #             relevant_documents
# #         )


# #     # -----------------------------
# #     # CHAT HISTORY FORMAT
# #     # -----------------------------

# #     history = "\n".join(
# #         f'{message["role"]}: {message["content"]}'
# #         for message in st.session_state.chat_history[-6:]
# #     )


# #     # -----------------------------
# #     # FINAL ANSWER
# #     # -----------------------------

# #     if not compressed_documents:

# #         answer = (
# #             "Information not available in the "
# #             "uploaded document."
# #         )

# #     else:

# #         context = "\n\n".join(
# #             document.page_content
# #             for document in compressed_documents
# #         )

# #         try:

# #             with st.spinner("Generating answer..."):

# #                 answer = rag_chain.invoke({
# #                     "context": context,
# #                     "question": question,
# #                     "history": history
# #                 }).strip()

# #         except Exception:

# #             answer = (
# #                 "Sorry, I could not generate an answer. "
# #                 "Please try again."
# #             )

# #             st.error(
# #                 "There was a problem connecting "
# #                 "to the AI model."
# #             )


# #     # -----------------------------
# #     # DISPLAY ANSWER
# #     # -----------------------------

# #     with st.chat_message("assistant"):

# #         st.markdown(answer)


# #     # Save assistant message
# #     st.session_state.chat_history.append({
# #         "role": "assistant",
# #         "content": answer
# #     })


# #     # -----------------------------
# #     # DISPLAY SOURCES
# #     # -----------------------------

# #     unavailable_message = (
# #         "Information not available in the "
# #         "uploaded document."
# #     )

# #     if (
# #         compressed_documents
# #         and answer != unavailable_message
# #         and not answer.startswith("Sorry")
# #     ):

# #         with st.expander("📚 Sources"):

# #             shown_pages = set()

# #             for document in compressed_documents:

# #                 page_number = document.metadata.get(
# #                     "page",
# #                     document.metadata.get("page_label", "Unknown")
# #                 )

# #                 if page_number not in shown_pages:

# #                     shown_pages.add(page_number)

# #                     st.write(
# #                         f"**Page:** {int(page_number) + 1}"
# #                         if isinstance(page_number, int)
# #                         else f"**Page:** {page_number}"
# #                     )

# #                     st.write(document.page_content)
# #                     st.divider()



# #                   < Caching >         # 

# # import streamlit as st
# # import tempfile
# # import uuid
# # from pathlib import Path

# # from dotenv import load_dotenv
# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # =============================
# # # CONFIGURATION
# # # =============================

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG Chatbot")

# # project_folder = Path(__file__).resolve().parent
# # load_dotenv(project_folder / ".env")


# # # =============================
# # # SESSION STATE
# # # =============================

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # if st.button("🗑️ Clear Chat History"):
# #     st.session_state.chat_history = []
# #     st.rerun()


# # # =============================
# # # CACHED EMBEDDINGS
# # # =============================

# # @st.cache_resource
# # def get_embeddings():

# #     return HuggingFaceEmbeddings(
# #         model_name="sentence-transformers/all-MiniLM-L6-v2"
# #     )


# # # =============================
# # # PDF UPLOAD
# # # =============================

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )

# # if uploaded_file is None:
# #     st.info("Please upload a PDF to start chatting.")
# #     st.stop()


# # # =============================
# # # SAVE PDF TEMPORARILY
# # # =============================

# # pdf_bytes = uploaded_file.getvalue()

# # try:

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temp_file:

# #         temp_file.write(pdf_bytes)
# #         pdf_path = temp_file.name

# # except Exception:

# #     st.error("Unable to save the uploaded PDF.")
# #     st.stop()


# # # =============================
# # # LOAD PDF
# # # =============================

# # try:

# #     with st.spinner("Loading PDF..."):

# #         loader = PyPDFLoader(pdf_path)
# #         documents = loader.load()

# #     st.success("PDF loaded successfully!")

# # except Exception:

# #     st.error(
# #         "Unable to read this PDF. "
# #         "Please upload a valid PDF."
# #     )

# #     st.stop()


# # # =============================
# # # SPLIT DOCUMENTS
# # # =============================

# # try:

# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     chunks = text_splitter.split_documents(documents)

# #     if not chunks:
# #         st.error("No readable text found in this PDF.")
# #         st.stop()

# # except Exception:

# #     st.error("Error while splitting the PDF.")
# #     st.stop()


# # # =============================
# # # EMBEDDINGS WITH CACHE
# # # =============================

# # try:

# #     with st.spinner("Loading embeddings..."):

# #         embeddings = get_embeddings()

# # except Exception:

# #     st.error("Error while loading embedding model.")
# #     st.stop()


# # # =============================
# # # VECTOR DATABASE
# # # =============================

# # try:

# #     with st.spinner("Creating vector database..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# #         )

# # except Exception:

# #     st.error("Error while creating vector database.")
# #     st.stop()


# # # =============================
# # # MMR RETRIEVER
# # # =============================

# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 5,
# #         "fetch_k": 15,
# #         "lambda_mult": 0.7
# #     }
# # )


# # # =============================
# # # LLM
# # # =============================

# # try:

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )

# # except Exception:

# #     st.error("Error while connecting to AI model.")
# #     st.stop()


# # # =============================
# # # RELEVANCE CHECK
# # # =============================

# # relevance_prompt = PromptTemplate.from_template(
# #     """
# # You are a document relevance checker.

# # Question:
# # {question}

# # Document:
# # {document}

# # Does this document contain information
# # that can help answer the question?

# # Return ONLY:
# # RELEVANT
# # or
# # NOT_RELEVANT
# # """
# # )

# # relevance_chain = (
# #     relevance_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def filter_relevant_documents(question, documents):

# #     relevant_documents = []

# #     for document in documents:

# #         try:

# #             result = relevance_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip().upper()

# #             if result == "RELEVANT":
# #                 relevant_documents.append(document)

# #         except Exception:

# #             continue

# #     return relevant_documents


# # # =============================
# # # CONTEXT COMPRESSION
# # # =============================

# # compression_prompt = PromptTemplate.from_template(
# #     """
# # You are an extractive document compressor.

# # Question:
# # {question}

# # Document:
# # {document}

# # Instructions:
# # - Extract only exact relevant sentences.
# # - Do not paraphrase.
# # - Do not add new information.
# # - If no relevant information exists, return EMPTY.
# # - Return only extracted text.
# # """
# # )

# # compression_chain = (
# #     compression_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def compress_documents(question, documents):

# #     compressed_documents = []

# #     for document in documents:

# #         try:

# #             compressed_text = compression_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip()

# #             if (
# #                 compressed_text
# #                 and compressed_text.upper() != "EMPTY"
# #             ):

# #                 compressed_documents.append(
# #                     Document(
# #                         page_content=compressed_text,
# #                         metadata=document.metadata
# #                     )
# #                 )

# #         except Exception:

# #             continue

# #     return compressed_documents


# # # =============================
# # # FINAL RAG PROMPT
# # # =============================

# # rag_prompt = PromptTemplate.from_template(
# #     """
# # You are a helpful PDF question-answering assistant.

# # Answer using ONLY the provided context.

# # Conversation History:
# # {history}

# # Context:
# # {context}

# # Question:
# # {question}

# # Rules:
# # - Use only the given context.
# # - Do not invent information.
# # - Keep the answer concise.
# # - If the answer is unavailable, respond exactly:

# # Information not available in the uploaded document.
# # """
# # )

# # rag_chain = (
# #     rag_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # =============================
# # # DISPLAY CHAT HISTORY
# # # =============================

# # for message in st.session_state.chat_history:

# #     with st.chat_message(message["role"]):
# #         st.markdown(message["content"])


# # # =============================
# # # USER QUESTION
# # # =============================

# # question = st.chat_input(
# #     "Ask a question about your PDF..."
# # )


# # if question:

# #     question = question.strip()

# #     if not question:

# #         st.warning("Please enter a valid question.")
# #         st.stop()

# #     with st.chat_message("user"):
# #         st.markdown(question)

# #     st.session_state.chat_history.append({
# #         "role": "user",
# #         "content": question
# #     })


# #     # =============================
# #     # RETRIEVAL
# #     # =============================

# #     try:

# #         with st.spinner("Searching document..."):

# #             retrieved_documents = retriever.invoke(question)

# #     except Exception:

# #         st.error("Error while searching document.")
# #         st.stop()


# #     # =============================
# #     # REMOVE DUPLICATES
# #     # =============================

# #     unique_documents = []
# #     seen_text = set()

# #     for document in retrieved_documents:

# #         text = document.page_content.strip()

# #         if text not in seen_text:

# #             seen_text.add(text)
# #             unique_documents.append(document)


# #     # =============================
# #     # RELEVANCE FILTERING
# #     # =============================

# #     with st.spinner("Checking relevant information..."):

# #         relevant_documents = filter_relevant_documents(
# #             question,
# #             unique_documents
# #         )


# #     # =============================
# #     # COMPRESSION
# #     # =============================

# #     with st.spinner("Preparing relevant context..."):

# #         compressed_documents = compress_documents(
# #             question,
# #             relevant_documents
# #         )


# #     # =============================
# #     # CHAT HISTORY
# #     # =============================

# #     history = "\n".join(
# #         f'{message["role"]}: {message["content"]}'
# #         for message in st.session_state.chat_history[-6:]
# #     )


# #     # =============================
# #     # FINAL ANSWER
# #     # =============================

# #     unavailable_message = (
# #         "Information not available in the "
# #         "uploaded document."
# #     )

# #     if not compressed_documents:

# #         answer = unavailable_message

# #     else:

# #         context = "\n\n".join(
# #             document.page_content
# #             for document in compressed_documents
# #         )

# #         try:

# #             with st.spinner("Generating answer..."):

# #                 answer = rag_chain.invoke({
# #                     "context": context,
# #                     "question": question,
# #                     "history": history
# #                 }).strip()

# #         except Exception:

# #             answer = (
# #                 "Sorry, I could not generate an answer. "
# #                 "Please try again."
# #             )

# #             st.error(
# #                 "There was a problem connecting "
# #                 "to the AI model."
# #             )


# #     # =============================
# #     # DISPLAY ANSWER
# #     # =============================

# #     with st.chat_message("assistant"):

# #         st.markdown(answer)

# #     st.session_state.chat_history.append({
# #         "role": "assistant",
# #         "content": answer
# #     })


# #     # =============================
# #     # SOURCES
# #     # =============================

# #     if (
# #         compressed_documents
# #         and answer != unavailable_message
# #         and not answer.startswith("Sorry")
# #     ):

# #         with st.expander("📚 Sources"):

# #             shown_pages = set()

# #             for document in compressed_documents:

# #                 page_number = document.metadata.get(
# #                     "page",
# #                     document.metadata.get(
# #                         "page_label",
# #                         "Unknown"
# #                     )
# #                 )

# #                 if page_number not in shown_pages:

# #                     shown_pages.add(page_number)

# #                     if isinstance(page_number, int):

# #                         st.write(
# #                             f"**Page:** {page_number + 1}"
# #                         )

# #                     else:

# #                         st.write(
# #                             f"**Page:** {page_number}"
# #                         )

# #                     st.write(document.page_content)
# #                     st.divider()


# #                   < PDF Loading + Chunking ko st.cache_data se cache karenge.>


# # import streamlit as st
# # import tempfile
# # import uuid
# # from pathlib import Path

# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq

# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # =============================
# # # CONFIGURATION
# # # =============================

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG Chatbot")

# # project_folder = Path(__file__).resolve().parent
# # load_dotenv(project_folder / ".env")


# # # =============================
# # # SESSION STATE
# # # =============================

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []


# # if st.button("🗑️ Clear Chat History"):

# #     st.session_state.chat_history = []
# #     st.rerun()


# # # =============================
# # # CACHED PDF LOADING + CHUNKING
# # # =============================

# # @st.cache_data
# # def load_and_split_pdf(pdf_bytes):

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temp_file:

# #         temp_file.write(pdf_bytes)
# #         pdf_path = temp_file.name

# #     try:

# #         loader = PyPDFLoader(pdf_path)
# #         documents = loader.load()

# #         text_splitter = RecursiveCharacterTextSplitter(
# #             chunk_size=500,
# #             chunk_overlap=50
# #         )

# #         chunks = text_splitter.split_documents(documents)

# #         return chunks

# #     finally:

# #         Path(pdf_path).unlink(missing_ok=True)


# # # =============================
# # # CACHED EMBEDDING MODEL
# # # =============================

# # @st.cache_resource
# # def get_embeddings():

# #     return HuggingFaceEmbeddings(
# #         model_name="sentence-transformers/all-MiniLM-L6-v2"
# #     )


# # # =============================
# # # PDF UPLOAD
# # # =============================

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )


# # if uploaded_file is None:

# #     st.info("Please upload a PDF to start chatting.")
# #     st.stop()


# # # =============================
# # # PDF PROCESSING
# # # =============================

# # pdf_bytes = uploaded_file.getvalue()

# # try:

# #     with st.spinner("Loading and splitting PDF..."):

# #         chunks = load_and_split_pdf(pdf_bytes)

# #     if not chunks:

# #         st.error("No readable text found in this PDF.")
# #         st.stop()

# #     st.success(
# #         f"PDF processed successfully! "
# #         f"Total chunks: {len(chunks)}"
# #     )

# # except Exception:

# #     st.error(
# #         "Unable to process this PDF. "
# #         "Please upload a valid PDF."
# #     )

# #     st.stop()


# # # =============================
# # # EMBEDDINGS
# # # =============================

# # try:

# #     with st.spinner("Loading embedding model..."):

# #         embeddings = get_embeddings()

# # except Exception:

# #     st.error("Error while loading embedding model.")
# #     st.stop()


# # # =============================
# # # VECTOR DATABASE
# # # =============================

# # try:

# #     with st.spinner("Creating vector database..."):

# #         vector_store = Chroma.from_documents(
# #             documents=chunks,
# #             embedding=embeddings,
# #             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# #         )

# # except Exception:

# #     st.error("Error while creating vector database.")
# #     st.stop()


# # # =============================
# # # RETRIEVER
# # # =============================

# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 5,
# #         "fetch_k": 15,
# #         "lambda_mult": 0.7
# #     }
# # )


# # # =============================
# # # LLM
# # # =============================

# # try:

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )

# # except Exception:

# #     st.error("Error while connecting to AI model.")
# #     st.stop()


# # # =============================
# # # RELEVANCE CHECK
# # # =============================

# # relevance_prompt = PromptTemplate.from_template(
# #     """
# # You are a document relevance checker.

# # Question:
# # {question}

# # Document:
# # {document}

# # Check whether the document contains information
# # that can help answer the question.

# # Return ONLY:
# # RELEVANT
# # or
# # NOT_RELEVANT
# # """
# # )


# # relevance_chain = (
# #     relevance_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def filter_relevant_documents(question, documents):

# #     relevant_documents = []

# #     for document in documents:

# #         try:

# #             result = relevance_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip().upper()

# #             if result == "RELEVANT":

# #                 relevant_documents.append(document)

# #         except Exception:

# #             continue

# #     return relevant_documents


# # # =============================
# # # CONTEXT COMPRESSION
# # # =============================

# # compression_prompt = PromptTemplate.from_template(
# #     """
# # You are an extractive document compressor.

# # Question:
# # {question}

# # Document:
# # {document}

# # Instructions:
# # - Extract only exact sentences relevant to the question.
# # - Do not paraphrase.
# # - Do not add new information.
# # - If no relevant information exists, return EMPTY.
# # - Return only the extracted text.
# # """
# # )


# # compression_chain = (
# #     compression_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def compress_documents(question, documents):

# #     compressed_documents = []

# #     for document in documents:

# #         try:

# #             compressed_text = compression_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip()

# #             if (
# #                 compressed_text
# #                 and compressed_text.upper() != "EMPTY"
# #             ):

# #                 compressed_documents.append(
# #                     Document(
# #                         page_content=compressed_text,
# #                         metadata=document.metadata
# #                     )
# #                 )

# #         except Exception:

# #             continue

# #     return compressed_documents


# # # =============================
# # # FINAL RAG CHAIN
# # # =============================

# # rag_prompt = PromptTemplate.from_template(
# #     """
# # You are a helpful PDF question-answering assistant.

# # Answer using ONLY the provided context.

# # Conversation History:
# # {history}

# # Context:
# # {context}

# # Question:
# # {question}

# # Rules:
# # - Use only the given context.
# # - Do not invent information.
# # - Keep the answer concise and clear.
# # - If the answer is unavailable, respond exactly:

# # Information not available in the uploaded document.
# # """
# # )


# # rag_chain = (
# #     rag_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # =============================
# # # DISPLAY CHAT HISTORY
# # # =============================

# # for message in st.session_state.chat_history:

# #     with st.chat_message(message["role"]):

# #         st.markdown(message["content"])


# # # =============================
# # # USER QUESTION
# # # =============================

# # question = st.chat_input(
# #     "Ask a question about your PDF..."
# # )


# # if question:

# #     question = question.strip()

# #     if not question:

# #         st.warning("Please enter a valid question.")
# #         st.stop()


# #     with st.chat_message("user"):

# #         st.markdown(question)


# #     st.session_state.chat_history.append({
# #         "role": "user",
# #         "content": question
# #     })


# #     # =============================
# #     # RETRIEVAL
# #     # =============================

# #     try:

# #         with st.spinner("Searching document..."):

# #             retrieved_documents = retriever.invoke(question)

# #     except Exception:

# #         st.error("Error while searching document.")
# #         st.stop()


# #     # =============================
# #     # REMOVE DUPLICATES
# #     # =============================

# #     unique_documents = []
# #     seen_text = set()

# #     for document in retrieved_documents:

# #         text = document.page_content.strip()

# #         if text not in seen_text:

# #             seen_text.add(text)
# #             unique_documents.append(document)


# #     # =============================
# #     # RELEVANCE FILTERING
# #     # =============================

# #     with st.spinner("Checking relevant information..."):

# #         relevant_documents = filter_relevant_documents(
# #             question,
# #             unique_documents
# #         )


# #     # =============================
# #     # COMPRESSION
# #     # =============================

# #     with st.spinner("Preparing relevant context..."):

# #         compressed_documents = compress_documents(
# #             question,
# #             relevant_documents
# #         )


# #     # =============================
# #     # CHAT HISTORY
# #     # =============================

# #     history = "\n".join(
# #         f'{message["role"]}: {message["content"]}'
# #         for message in st.session_state.chat_history[-6:]
# #     )


# #     # =============================
# #     # FINAL ANSWER
# #     # =============================

# #     unavailable_message = (
# #         "Information not available in the "
# #         "uploaded document."
# #     )


# #     if not compressed_documents:

# #         answer = unavailable_message

# #     else:

# #         context = "\n\n".join(
# #             document.page_content
# #             for document in compressed_documents
# #         )

# #         try:

# #             with st.spinner("Generating answer..."):

# #                 answer = rag_chain.invoke({
# #                     "context": context,
# #                     "question": question,
# #                     "history": history
# #                 }).strip()

# #         except Exception:

# #             answer = (
# #                 "Sorry, I could not generate an answer. "
# #                 "Please try again."
# #             )

# #             st.error(
# #                 "There was a problem connecting "
# #                 "to the AI model."
# #             )


# #     # =============================
# #     # DISPLAY ANSWER
# #     # =============================

# #     with st.chat_message("assistant"):

# #         st.markdown(answer)


# #     st.session_state.chat_history.append({
# #         "role": "assistant",
# #         "content": answer
# #     })


# #     # =============================
# #     # SOURCES
# #     # =============================

# #     if (
# #         compressed_documents
# #         and answer != unavailable_message
# #         and not answer.startswith("Sorry")
# #     ):

# #         with st.expander("📚 Sources"):

# #             shown_pages = set()

# #             for document in compressed_documents:

# #                 page_number = document.metadata.get(
# #                     "page",
# #                     document.metadata.get(
# #                         "page_label",
# #                         "Unknown"
# #                     )
# #                 )

# #                 if page_number not in shown_pages:

# #                     shown_pages.add(page_number)

# #                     if isinstance(page_number, int):

# #                         st.write(
# #                             f"**Page:** {page_number + 1}"
# #                         )

# #                     else:

# #                         st.write(
# #                             f"**Page:** {page_number}"
# #                         )

# #                     st.write(document.page_content)
# #                     st.divider()



# #.              < final after all catch >         #




# # import streamlit as st
# # import tempfile
# # import uuid
# # import hashlib
# # from pathlib import Path

# # from dotenv import load_dotenv

# # from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_groq import ChatGroq

# # from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_core.documents import Document


# # # =============================
# # # CONFIGURATION
# # # =============================

# # st.set_page_config(
# #     page_title="PDF RAG Chatbot",
# #     page_icon="📄"
# # )

# # st.title("📄 PDF RAG Chatbot")

# # project_folder = Path(__file__).resolve().parent
# # load_dotenv(project_folder / ".env")


# # # =============================
# # # SESSION STATE
# # # =============================

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []


# # if "pdf_hash" not in st.session_state:
# #     st.session_state.pdf_hash = None


# # if "vector_store" not in st.session_state:
# #     st.session_state.vector_store = None


# # if st.button("🗑️ Clear Chat History"):

# #     st.session_state.chat_history = []
# #     st.rerun()


# # # =============================
# # # CACHED PDF LOADING + CHUNKING
# # # =============================

# # @st.cache_data
# # def load_and_split_pdf(pdf_bytes):

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=".pdf"
# #     ) as temp_file:

# #         temp_file.write(pdf_bytes)
# #         pdf_path = temp_file.name

# #     try:

# #         loader = PyPDFLoader(pdf_path)
# #         documents = loader.load()

# #         text_splitter = RecursiveCharacterTextSplitter(
# #             chunk_size=500,
# #             chunk_overlap=50
# #         )

# #         chunks = text_splitter.split_documents(documents)

# #         return chunks

# #     finally:

# #         Path(pdf_path).unlink(missing_ok=True)


# # # =============================
# # # CACHED EMBEDDING MODEL
# # # =============================

# # @st.cache_resource
# # def get_embeddings():

# #     return HuggingFaceEmbeddings(
# #         model_name="sentence-transformers/all-MiniLM-L6-v2"
# #     )


# # # =============================
# # # PDF UPLOAD
# # # =============================

# # uploaded_file = st.file_uploader(
# #     "Upload your PDF",
# #     type=["pdf"]
# # )


# # if uploaded_file is None:

# #     st.info("Please upload a PDF to start chatting.")
# #     st.stop()


# # # =============================
# # # PDF PROCESSING
# # # =============================

# # pdf_bytes = uploaded_file.getvalue()

# # pdf_hash = hashlib.md5(pdf_bytes).hexdigest()


# # try:

# #     with st.spinner("Loading and splitting PDF..."):

# #         chunks = load_and_split_pdf(pdf_bytes)

# #     if not chunks:

# #         st.error("No readable text found in this PDF.")
# #         st.stop()

# #     st.success(
# #         f"PDF processed successfully! "
# #         f"Total chunks: {len(chunks)}"
# #     )

# # except Exception:

# #     st.error(
# #         "Unable to process this PDF. "
# #         "Please upload a valid PDF."
# #     )

# #     st.stop()


# # # =============================
# # # EMBEDDINGS
# # # =============================

# # try:

# #     with st.spinner("Loading embedding model..."):

# #         embeddings = get_embeddings()

# # except Exception:

# #     st.error("Error while loading embedding model.")
# #     st.stop()


# # # =============================
# # # VECTOR DATABASE REUSE
# # # =============================

# # if (
# #     st.session_state.pdf_hash != pdf_hash
# #     or st.session_state.vector_store is None
# # ):

# #     try:

# #         with st.spinner("Creating vector database..."):

# #             vector_store = Chroma.from_documents(
# #                 documents=chunks,
# #                 embedding=embeddings,
# #                 collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# #             )

# #         st.session_state.vector_store = vector_store
# #         st.session_state.pdf_hash = pdf_hash

# #         st.success(
# #             "Vector database created successfully!"
# #         )

# #     except Exception:

# #         st.error(
# #             "Error while creating vector database."
# #         )

# #         st.stop()

# # else:

# #     vector_store = st.session_state.vector_store

# #     st.info("Using cached vector database.")


# # # =============================
# # # MMR RETRIEVER
# # # =============================

# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 5,
# #         "fetch_k": 15,
# #         "lambda_mult": 0.7
# #     }
# # )


# # # =============================
# # # LLM
# # # =============================

# # try:

# #     llm = ChatGroq(
# #         model="openai/gpt-oss-20b",
# #         temperature=0
# #     )

# # except Exception:

# #     st.error("Error while connecting to AI model.")
# #     st.stop()


# # # =============================
# # # RELEVANCE CHECK
# # # =============================

# # relevance_prompt = PromptTemplate.from_template(
# #     """
# # You are a document relevance checker.

# # Question:
# # {question}

# # Document:
# # {document}

# # Check whether the document contains information
# # that can help answer the question.

# # Return ONLY:
# # RELEVANT
# # or
# # NOT_RELEVANT
# # """
# # )


# # relevance_chain = (
# #     relevance_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def filter_relevant_documents(question, documents):

# #     relevant_documents = []

# #     for document in documents:

# #         try:

# #             result = relevance_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip().upper()

# #             if result == "RELEVANT":

# #                 relevant_documents.append(document)

# #         except Exception:

# #             continue

# #     return relevant_documents


# # # =============================
# # # CONTEXT COMPRESSION
# # # =============================

# # compression_prompt = PromptTemplate.from_template(
# #     """
# # You are an extractive document compressor.

# # Question:
# # {question}

# # Document:
# # {document}

# # Instructions:
# # - Extract only exact sentences relevant to the question.
# # - Do not paraphrase.
# # - Do not add new information.
# # - If no relevant information exists, return EMPTY.
# # - Return only the extracted text.
# # """
# # )


# # compression_chain = (
# #     compression_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # def compress_documents(question, documents):

# #     compressed_documents = []

# #     for document in documents:

# #         try:

# #             compressed_text = compression_chain.invoke({
# #                 "question": question,
# #                 "document": document.page_content
# #             }).strip()

# #             if (
# #                 compressed_text
# #                 and compressed_text.upper() != "EMPTY"
# #             ):

# #                 compressed_documents.append(
# #                     Document(
# #                         page_content=compressed_text,
# #                         metadata=document.metadata
# #                     )
# #                 )

# #         except Exception:

# #             continue

# #     return compressed_documents


# # # =============================
# # # FINAL RAG CHAIN
# # # =============================

# # rag_prompt = PromptTemplate.from_template(
# #     """
# # You are a helpful PDF question-answering assistant.

# # Answer using ONLY the provided context.

# # Conversation History:
# # {history}

# # Context:
# # {context}

# # Question:
# # {question}

# # Rules:
# # - Use only the given context.
# # - Do not invent information.
# # - Keep the answer concise and clear.
# # - If the answer is unavailable, respond exactly:

# # Information not available in the uploaded document.
# # """
# # )


# # rag_chain = (
# #     rag_prompt
# #     | llm
# #     | StrOutputParser()
# # )


# # # =============================
# # # DISPLAY CHAT HISTORY
# # # =============================

# # for message in st.session_state.chat_history:

# #     with st.chat_message(message["role"]):

# #         st.markdown(message["content"])


# # # =============================
# # # USER QUESTION
# # # =============================

# # question = st.chat_input(
# #     "Ask a question about your PDF..."
# # )


# # if question:

# #     question = question.strip()

# #     if not question:

# #         st.warning("Please enter a valid question.")
# #         st.stop()


# #     with st.chat_message("user"):

# #         st.markdown(question)


# #     st.session_state.chat_history.append({
# #         "role": "user",
# #         "content": question
# #     })


# #     # =============================
# #     # RETRIEVAL
# #     # =============================

# #     try:

# #         with st.spinner("Searching document..."):

# #             retrieved_documents = retriever.invoke(question)

# #     except Exception:

# #         st.error("Error while searching document.")
# #         st.stop()


# #     # =============================
# #     # REMOVE DUPLICATES
# #     # =============================

# #     unique_documents = []
# #     seen_text = set()

# #     for document in retrieved_documents:

# #         text = document.page_content.strip()

# #         if text not in seen_text:

# #             seen_text.add(text)
# #             unique_documents.append(document)


# #     # =============================
# #     # RELEVANCE FILTERING
# #     # =============================

# #     with st.spinner("Checking relevant information..."):

# #         relevant_documents = filter_relevant_documents(
# #             question,
# #             unique_documents
# #         )


# #     # =============================
# #     # CONTEXT COMPRESSION
# #     # =============================

# #     with st.spinner("Preparing relevant context..."):

# #         compressed_documents = compress_documents(
# #             question,
# #             relevant_documents
# #         )


# #     # =============================
# #     # CHAT HISTORY
# #     # =============================

# #     history = "\n".join(
# #         f'{message["role"]}: {message["content"]}'
# #         for message in st.session_state.chat_history[-6:]
# #     )


# #     # =============================
# #     # FINAL ANSWER
# #     # =============================

# #     unavailable_message = (
# #         "Information not available in the "
# #         "uploaded document."
# #     )


# #     if not compressed_documents:

# #         answer = unavailable_message

# #     else:

# #         context = "\n\n".join(
# #             document.page_content
# #             for document in compressed_documents
# #         )

# #         try:

# #             with st.spinner("Generating answer..."):

# #                 answer = rag_chain.invoke({
# #                     "context": context,
# #                     "question": question,
# #                     "history": history
# #                 }).strip()

# #         except Exception:

# #             answer = (
# #                 "Sorry, I could not generate an answer. "
# #                 "Please try again."
# #             )

# #             st.error(
# #                 "There was a problem connecting "
# #                 "to the AI model."
# #             )


# #     # =============================
# #     # DISPLAY ANSWER
# #     # =============================

# #     with st.chat_message("assistant"):

# #         st.markdown(answer)


# #     st.session_state.chat_history.append({
# #         "role": "assistant",
# #         "content": answer
# #     })


# #     # =============================
# #     # SOURCES
# #     # =============================

# #     if (
# #         compressed_documents
# #         and answer != unavailable_message
# #         and not answer.startswith("Sorry")
# #     ):

# #         with st.expander("📚 Sources"):

# #             shown_pages = set()

# #             for document in compressed_documents:

# #                 page_number = document.metadata.get(
# #                     "page",
# #                     document.metadata.get(
# #                         "page_label",
# #                         "Unknown"
# #                     )
# #                 )

# #                 if page_number not in shown_pages:

# #                     shown_pages.add(page_number)

# #                     if isinstance(page_number, int):

# #                         st.write(
# #                             f"**Page:** {page_number + 1}"
# #                         )

# #                     else:

# #                         st.write(
# #                             f"**Page:** {page_number}"
# #                         )

# #                     st.write(document.page_content)
# #                     st.divider()

# #           < iam working here for two thing first for wide or fit to screen display and 
#  #          second for giving info from trained knowledge >



# import streamlit as st
# import tempfile
# import hashlib
# import uuid
# import os

# from pathlib import Path
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# from langchain_groq import ChatGroq

# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.documents import Document


# # =========================================================
# # 1. PAGE CONFIGURATION
# # =========================================================

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📄",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


# # =========================================================
# # 2. LOAD ENVIRONMENT VARIABLES
# # =========================================================

# project_folder = Path(__file__).resolve().parent

# load_dotenv(project_folder / ".env")


# # =========================================================
# # 3. API KEY CONFIGURATION
# # =========================================================

# groq_api_key = st.secrets.get(
#     "GROQ_API_KEY",
#     os.getenv("GROQ_API_KEY")
# )

# if not groq_api_key:
#     st.error("GROQ_API_KEY is missing. Please configure your API key.")
#     st.stop()


# # =========================================================
# # 4. SESSION STATE
# # =========================================================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "pdf_hash" not in st.session_state:
#     st.session_state.pdf_hash = None

# if "vector_store" not in st.session_state:
#     st.session_state.vector_store = None


# # =========================================================
# # 5. SIDEBAR SETTINGS
# # =========================================================

# st.sidebar.title("⚙️ Settings")


# screen_mode = st.sidebar.radio(
#     "🖥️ Screen Layout",
#     ["Wide Screen", "Fit to Screen"],
#     index=0
# )


# temperature = st.sidebar.slider(
#     "🌡️ Temperature",
#     min_value=0.0,
#     max_value=1.0,
#     value=0.0,
#     step=0.1
# )


# allow_general_knowledge = st.sidebar.checkbox(
#     "🧠 Allow General Knowledge Fallback",
#     value=True
# )


# if st.sidebar.button("🗑️ Clear Chat History"):
#     st.session_state.chat_history = []
#     st.rerun()


# # =========================================================
# # 6. CUSTOM SCREEN LAYOUT
# # =========================================================

# if screen_mode == "Fit to Screen":

#     st.markdown(
#         """
#         <style>
#         .stMainBlockContainer {
#             max-width: 900px;
#             margin: auto;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# else:

#     st.markdown(
#         """
#         <style>
#         .stMainBlockContainer {
#             max-width: 100%;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )


# # =========================================================
# # 7. PAGE TITLE
# # =========================================================

# st.title("📄 PDF RAG Chatbot")

# st.write(
#     "Upload a PDF and ask questions from the document. "
#     "If enabled, general knowledge fallback will be used "
#     "when relevant PDF information is not found."
# )


# # =========================================================
# # 8. CACHED PDF LOADING AND CHUNKING
# # =========================================================

# @st.cache_data
# def load_and_split_pdf(pdf_bytes):

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temp_file:

#         temp_file.write(pdf_bytes)
#         pdf_path = temp_file.name

#     try:

#         loader = PyPDFLoader(pdf_path)

#         documents = loader.load()

#         splitter = RecursiveCharacterTextSplitter(
#             chunk_size=500,
#             chunk_overlap=50
#         )

#         chunks = splitter.split_documents(documents)

#         return chunks

#     finally:

#         Path(pdf_path).unlink(missing_ok=True)


# # =========================================================
# # 9. CACHED EMBEDDING MODEL
# # =========================================================

# @st.cache_resource
# def get_embeddings():

#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


# # =========================================================
# # 10. PDF UPLOAD
# # =========================================================

# uploaded_file = st.file_uploader(
#     "📤 Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is None:

#     st.info("Please upload a PDF to start asking questions.")

#     st.stop()


# pdf_bytes = uploaded_file.getvalue()

# pdf_hash = hashlib.md5(pdf_bytes).hexdigest()


# # =========================================================
# # 11. LOAD AND SPLIT PDF
# # =========================================================

# try:

#     with st.spinner("Loading and splitting PDF..."):

#         chunks = load_and_split_pdf(pdf_bytes)

#     st.success(
#         f"PDF processed successfully! Total chunks: {len(chunks)}"
#     )

# except Exception:

#     st.error(
#         "Unable to read this PDF. Please upload a valid PDF file."
#     )

#     st.stop()


# # =========================================================
# # 12. EMBEDDINGS
# # =========================================================

# try:

#     with st.spinner("Loading embedding model..."):

#         embeddings = get_embeddings()

# except Exception:

#     st.error(
#         "Unable to load the embedding model."
#     )

#     st.stop()


# # =========================================================
# # 13. VECTOR STORE CREATION AND REUSE
# # =========================================================

# if (
#     st.session_state.pdf_hash != pdf_hash
#     or st.session_state.vector_store is None
# ):

#     try:

#         with st.spinner("Creating vector database..."):

#             vector_store = Chroma.from_documents(
#                 documents=chunks,
#                 embedding=embeddings,
#                 collection_name=f"pdf_rag_{uuid.uuid4().hex}"
#             )

#         st.session_state.vector_store = vector_store

#         st.session_state.pdf_hash = pdf_hash

#         # Clear old chat when a new PDF is uploaded
#         st.session_state.chat_history = []

#     except Exception:

#         st.error(
#             "Unable to create the vector database."
#         )

#         st.stop()

# else:

#     vector_store = st.session_state.vector_store


# # =========================================================
# # 14. RETRIEVER
# # =========================================================

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # =========================================================
# # 15. LLM
# # =========================================================

# try:

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=temperature,
#         api_key=groq_api_key
#     )

# except Exception:

#     st.error(
#         "Unable to connect to the Groq model."
#     )

#     st.stop()


# # =========================================================
# # 16. RELEVANCE GRADING PROMPT
# # =========================================================

# relevance_prompt = PromptTemplate.from_template(
#     """
#     You are a document relevance grader.

#     Decide whether the context contains useful information
#     to answer the question.

#     Return ONLY one of these exact words:

#     RELEVANT
#     NOT_RELEVANT

#     Question:
#     {question}

#     Context:
#     {context}
#     """
# )


# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# def is_relevant(question, document):

#     try:

#         result = relevance_chain.invoke(
#             {
#                 "question": question,
#                 "context": document.page_content
#             }
#         ).strip().upper()

#         return result == "RELEVANT"

#     except Exception:

#         return False


# # =========================================================
# # 17. CONTEXT COMPRESSION PROMPT
# # =========================================================

# compression_prompt = PromptTemplate.from_template(
#     """
#     You are a context extraction assistant.

#     Extract ONLY the information from the context
#     that is directly useful for answering the question.

#     Rules:
#     - Do not add outside knowledge.
#     - Do not invent facts.
#     - If useful information is not present, return an empty response.
#     - Keep important facts, numbers, and names.
#     - Keep the answer concise.

#     Question:
#     {question}

#     Context:
#     {context}
#     """
# )


# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_document(question, document):

#     try:

#         compressed_text = compression_chain.invoke(
#             {
#                 "question": question,
#                 "context": document.page_content
#             }
#         ).strip()

#         if not compressed_text:
#             return None

#         return Document(
#             page_content=compressed_text,
#             metadata=document.metadata
#         )

#     except Exception:

#         return None


# # =========================================================
# # 18. PDF RAG PROMPT
# # =========================================================

# rag_prompt = PromptTemplate.from_template(
#     """
#     You are a helpful PDF question-answering assistant.

#     Answer the question using ONLY the provided PDF context.

#     Rules:
#     - Do not use outside knowledge.
#     - Do not invent information.
#     - Give a clear and concise answer.
#     - If the context does not contain the answer,
#       respond exactly:
#       Information not available in the provided document.

#     Conversation History:
#     {chat_history}

#     PDF Context:
#     {context}

#     Question:
#     {question}

#     Answer:
#     """
# )


# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # =========================================================
# # 19. GENERAL KNOWLEDGE PROMPT
# # =========================================================

# general_prompt = PromptTemplate.from_template(
#     """
#     You are a helpful AI assistant.

#     Answer the user's question using your general
#     pretrained knowledge.

#     Rules:
#     - Do not claim that the answer comes from the PDF.
#     - Do not invent facts.
#     - If you are uncertain, clearly mention the uncertainty.
#     - Give a clear and concise answer.

#     Question:
#     {question}

#     Answer:
#     """
# )


# general_chain = (
#     general_prompt
#     | llm
#     | StrOutputParser()
# )


# # =========================================================
# # 20. DISPLAY CHAT HISTORY
# # =========================================================

# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):

#         st.markdown(message["content"])

#         if message["role"] == "assistant":

#             if "source" in message:

#                 st.caption(message["source"])


# # =========================================================
# # 21. USER QUESTION
# # =========================================================

# user_question = st.chat_input(
#     "Ask a question about your PDF..."
# )


# if user_question:

#     # Display user message
#     with st.chat_message("user"):

#         st.markdown(user_question)

#     st.session_state.chat_history.append(
#         {
#             "role": "user",
#             "content": user_question
#         }
#     )


#     # =====================================================
#     # 22. RETRIEVE DOCUMENTS
#     # =====================================================

#     try:

#         with st.spinner("Searching the PDF..."):

#             retrieved_docs = retriever.invoke(
#                 user_question
#             )

#     except Exception:

#         retrieved_docs = []

#         st.warning(
#             "Unable to retrieve relevant PDF context."
#         )


#     # =====================================================
#     # 23. REMOVE DUPLICATE DOCUMENTS
#     # =====================================================

#     unique_docs = []

#     seen_content = set()

#     for doc in retrieved_docs:

#         content = doc.page_content.strip()

#         if content not in seen_content:

#             seen_content.add(content)

#             unique_docs.append(doc)


#     # =====================================================
#     # 24. RELEVANCE FILTERING
#     # =====================================================

#     relevant_docs = []

#     with st.spinner("Checking document relevance..."):

#         for doc in unique_docs:

#             if is_relevant(user_question, doc):

#                 relevant_docs.append(doc)


#     # =====================================================
#     # 25. CONTEXT COMPRESSION
#     # =====================================================

#     compressed_docs = []

#     if relevant_docs:

#         with st.spinner("Preparing relevant context..."):

#             for doc in relevant_docs:

#                 compressed_doc = compress_document(
#                     user_question,
#                     doc
#                 )

#                 if compressed_doc:

#                     compressed_docs.append(compressed_doc)


#     # =====================================================
#     # 26. CHAT HISTORY TEXT
#     # =====================================================

#     history_text = ""

#     for message in st.session_state.chat_history[-6:]:

#         history_text += (
#             f"{message['role']}: "
#             f"{message['content']}\n"
#         )


#     # =====================================================
#     # 27. ANSWER GENERATION
#     # =====================================================

#     answer = ""

#     answer_source = ""

#     source_documents = []


#     try:

#         with st.spinner("Generating answer..."):

#             if compressed_docs:

#                 context = "\n\n".join(
#                     doc.page_content
#                     for doc in compressed_docs
#                 )

#                 answer = rag_chain.invoke(
#                     {
#                         "context": context,
#                         "question": user_question,
#                         "chat_history": history_text
#                     }
#                 ).strip()

#                 # If the strict PDF chain cannot answer,
#                 # optionally use general knowledge fallback.
#                 unavailable_text = (
#                     "information not available"
#                 )

#                 if (
#                     allow_general_knowledge
#                     and unavailable_text in answer.lower()
#                 ):

#                     answer = general_chain.invoke(
#                         {
#                             "question": user_question
#                         }
#                     ).strip()

#                     answer_source = (
#                         "🧠 Source: General Knowledge (LLM)"
#                     )

#                 else:

#                     answer_source = (
#                         "📄 Source: Uploaded PDF"
#                     )

#                     source_documents = compressed_docs

#             else:

#                 if allow_general_knowledge:

#                     answer = general_chain.invoke(
#                         {
#                             "question": user_question
#                         }
#                     ).strip()

#                     answer_source = (
#                         "🧠 Source: General Knowledge (LLM)"
#                     )

#                 else:

#                     answer = (
#                         "Information not available "
#                         "in the provided document."
#                     )

#                     answer_source = (
#                         "📄 Source: Uploaded PDF"
#                     )


#     except Exception:

#         answer = (
#             "Sorry, I could not generate an answer. "
#             "Please try again."
#         )

#         answer_source = (
#             "⚠️ Answer generation failed"
#         )

#         st.error(
#             "There was a problem connecting to the AI model."
#         )


#     # =====================================================
#     # 28. DISPLAY ASSISTANT RESPONSE
#     # =====================================================

#     with st.chat_message("assistant"):

#         st.markdown(answer)

#         st.caption(answer_source)


#         # =================================================
#         # 29. DISPLAY PDF SOURCES
#         # =================================================

#         if source_documents:

#             st.markdown("#### 📚 PDF Sources")

#             displayed_sources = set()

#             for doc in source_documents:

#                 page_number = doc.metadata.get(
#                     "page",
#                     None
#                 )

#                 if page_number is not None:

#                     page_number = int(page_number) + 1

#                     source_label = (
#                         f"Page {page_number}"
#                     )

#                 else:

#                     source_label = "Page number unavailable"


#                 if source_label not in displayed_sources:

#                     displayed_sources.add(source_label)

#                     st.write(f"📄 {source_label}")


#     # =====================================================
#     # 30. SAVE ASSISTANT MESSAGE
#     # =====================================================

#     st.session_state.chat_history.append(
#         {
#             "role": "assistant",
#             "content": answer,
#             "source": answer_source
#         }
#     )



#               < Advance rag >.                 #

# import os
# import re
# import hashlib
# import tempfile
# from pathlib import Path

# import streamlit as st
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# from langchain_groq import ChatGroq
# from langchain_core.documents import Document
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# # ============================================================
# # 1. PAGE CONFIGURATION
# # ============================================================

# st.set_page_config(
#     page_title="Advanced PDF RAG Chatbot",
#     page_icon="📄",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# st.title("📄 Advanced PDF RAG Chatbot")
# st.caption(
#     "Multi-Query | Parent-Child Retrieval | Reranking | "
#     "Compression | Answer Verification"
# )


# # ============================================================
# # 2. LOAD ENVIRONMENT VARIABLES
# # ============================================================

# PROJECT_FOLDER = Path(__file__).resolve().parent
# load_dotenv(PROJECT_FOLDER / ".env")

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     st.error("GROQ_API_KEY is missing in the .env file.")
#     st.stop()


# # ============================================================
# # 3. SESSION STATE
# # ============================================================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "pdf_hash" not in st.session_state:
#     st.session_state.pdf_hash = None

# if "vector_store" not in st.session_state:
#     st.session_state.vector_store = None

# if "parent_store" not in st.session_state:
#     st.session_state.parent_store = {}

# if "child_chunks" not in st.session_state:
#     st.session_state.child_chunks = []

# if "bm25_chunks" not in st.session_state:
#     st.session_state.bm25_chunks = []


# # ============================================================
# # 4. CACHED EMBEDDINGS
# # ============================================================

# @st.cache_resource
# def get_embeddings():
#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


# # ============================================================
# # 5. LOAD PDF AND CREATE PARENT CHUNKS
# # ============================================================

# @st.cache_data(show_spinner=False)
# def load_pdf_and_create_parent_chunks(pdf_bytes):
#     temp_path = None

#     try:
#         with tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".pdf"
#         ) as temp_file:
#             temp_file.write(pdf_bytes)
#             temp_path = temp_file.name

#         loader = PyPDFLoader(temp_path)
#         documents = loader.load()

#         parent_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=1000,
#             chunk_overlap=100,
#             separators=[
#                 "\n\n",
#                 "\n",
#                 ". ",
#                 " ",
#                 ""
#             ]
#         )

#         parent_chunks = parent_splitter.split_documents(
#             documents
#         )

#         return parent_chunks

#     finally:
#         if temp_path and os.path.exists(temp_path):
#             os.remove(temp_path)


# # ============================================================
# # 6. CREATE CHILD CHUNKS AND PARENT STORE
# # ============================================================

# def create_parent_child_chunks(parent_chunks):
#     child_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=250,
#         chunk_overlap=50,
#         separators=[
#             "\n\n",
#             "\n",
#             ". ",
#             " ",
#             ""
#         ]
#     )

#     child_chunks = []
#     parent_store = {}

#     for parent_id, parent_doc in enumerate(parent_chunks):
#         parent_key = str(parent_id)

#         parent_doc.metadata["parent_id"] = parent_key
#         parent_store[parent_key] = parent_doc

#         children = child_splitter.split_documents(
#             [parent_doc]
#         )

#         for child_index, child_doc in enumerate(children):
#             child_doc.metadata["parent_id"] = parent_key
#             child_doc.metadata["child_id"] = (
#                 f"{parent_key}_{child_index}"
#             )

#             child_chunks.append(child_doc)

#     return child_chunks, parent_store


# # ============================================================
# # 7. CREATE VECTOR STORE
# # ============================================================

# def create_vector_store(child_chunks, embeddings, pdf_hash):
#     collection_name = (
#         "pdf_rag_" + pdf_hash[:16]
#     )

#     vector_store = Chroma.from_documents(
#         documents=child_chunks,
#         embedding=embeddings,
#         collection_name=collection_name
#     )

#     return vector_store


# # ============================================================
# # 8. INITIALIZE LLM
# # ============================================================

# @st.cache_resource
# def get_llm():
#     return ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


# # ============================================================
# # 9. MULTI-QUERY RETRIEVAL
# # ============================================================

# def generate_multi_queries(question, llm):
#     multi_query_prompt = PromptTemplate.from_template(
#         """
#         Generate three different search queries for the
#         user's question.

#         Rules:
#         - Preserve the original meaning.
#         - Use different wording.
#         - Return only one query per line.
#         - Do not add numbering.
#         - Do not add explanations.

#         User question:
#         {question}
#         """
#     )

#     query_chain = (
#         multi_query_prompt
#         | llm
#         | StrOutputParser()
#     )

#     response = query_chain.invoke({
#         "question": question
#     })

#     queries = []

#     for line in response.splitlines():
#         query = re.sub(
#             r"^\s*[-*]?\s*\d*[\).\:-]?\s*",
#             "",
#             line
#         ).strip()

#         if query:
#             queries.append(query)

#     # Include the original question
#     all_queries = [question]

#     for query in queries:
#         if query.lower() not in {
#             item.lower() for item in all_queries
#         }:
#             all_queries.append(query)

#     return all_queries[:4]


# def multi_query_retrieval(
#     question,
#     vector_store,
#     parent_store,
#     llm,
#     top_k=3
# ):
#     queries = generate_multi_queries(
#         question,
#         llm
#     )

#     retrieved_parents = []
#     seen_parent_ids = set()

#     for query in queries:
#         child_results = vector_store.similarity_search(
#             query,
#             k=top_k
#         )

#         for child_doc in child_results:
#             parent_id = child_doc.metadata.get(
#                 "parent_id"
#             )

#             if (
#                 parent_id is not None
#                 and parent_id in parent_store
#                 and parent_id not in seen_parent_ids
#             ):
#                 retrieved_parents.append(
#                     parent_store[parent_id]
#                 )

#                 seen_parent_ids.add(parent_id)

#     return retrieved_parents, queries


# # ============================================================
# # 10. LLM-BASED RERANKING
# # ============================================================

# rerank_prompt = PromptTemplate.from_template(
#     """
#     You are a document relevance evaluator.

#     Give a relevance score from 0 to 10.
#     The score should represent how useful the document
#     is for answering the question.

#     Rules:
#     - Return only a number.
#     - Do not provide an explanation.
#     - Use 0 if the document is not relevant.

#     Question:
#     {question}

#     Document:
#     {document}

#     Relevance score:
#     """
# )


# def rerank_documents(
#     question,
#     documents,
#     llm,
#     top_k=4
# ):
#     rerank_chain = (
#         rerank_prompt
#         | llm
#         | StrOutputParser()
#     )

#     scored_documents = []

#     for doc in documents:
#         try:
#             response = rerank_chain.invoke({
#                 "question": question,
#                 "document": doc.page_content
#             })

#             match = re.search(
#                 r"\b(?:10|[0-9](?:\.\d+)?)\b",
#                 response.strip()
#             )

#             score = float(match.group()) if match else 0

#             score = max(0, min(10, score))

#         except Exception:
#             score = 0

#         scored_documents.append(
#             (score, doc)
#         )

#     scored_documents.sort(
#         key=lambda item: item[0],
#         reverse=True
#     )

#     return [
#         doc
#         for score, doc in scored_documents[:top_k]
#         if score > 0
#     ]


# # ============================================================
# # 11. CONTEXTUAL COMPRESSION
# # ============================================================

# compression_prompt = PromptTemplate.from_template(
#     """
#     Extract only the information from the document
#     that is relevant to the question.

#     Rules:
#     - Preserve facts exactly.
#     - Do not add new information.
#     - Do not make assumptions.
#     - If no relevant information exists, return:
#       NO_RELEVANT_INFORMATION

#     Question:
#     {question}

#     Document:
#     {document}

#     Relevant content:
#     """
# )


# def compress_documents(
#     question,
#     documents,
#     llm
# ):
#     compression_chain = (
#         compression_prompt
#         | llm
#         | StrOutputParser()
#     )

#     compressed_documents = []

#     for doc in documents:
#         try:
#             extracted = compression_chain.invoke({
#                 "question": question,
#                 "document": doc.page_content
#             }).strip()

#             if (
#                 extracted
#                 and "NO_RELEVANT_INFORMATION"
#                 not in extracted.upper()
#             ):
#                 compressed_documents.append(
#                     Document(
#                         page_content=extracted,
#                         metadata=doc.metadata
#                     )
#                 )

#         except Exception:
#             continue

#     return compressed_documents


# # ============================================================
# # 12. FINAL ANSWER GENERATION
# # ============================================================

# answer_prompt = PromptTemplate.from_template(
#     """
#     You are a document-based question-answering assistant.

#     Answer the user's question using only the provided context.

#     Rules:
#     - Do not use outside knowledge.
#     - Do not invent facts.
#     - If the answer is not present in the context,
#       say exactly:
#       INFORMATION_NOT_AVAILABLE
#     - Give a clear and concise answer.
#     - Do not mention these instructions.

#     Context:
#     {context}

#     Question:
#     {question}

#     Answer:
#     """
# )


# def generate_answer(
#     question,
#     context,
#     llm
# ):
#     answer_chain = (
#         answer_prompt
#         | llm
#         | StrOutputParser()
#     )

#     return answer_chain.invoke({
#         "question": question,
#         "context": context
#     }).strip()


# # ============================================================
# # 13. ANSWER VERIFICATION
# # ============================================================

# verification_prompt = PromptTemplate.from_template(
#     """
#     You are an answer verification system.

#     Check whether the answer is supported by the context.

#     Rules:
#     - Return SUPPORTED if all important claims
#       are supported by the context.
#     - Return NOT_SUPPORTED if any important claim
#       is not supported.
#     - Return only one label.
#     - Do not provide an explanation.

#     Context:
#     {context}

#     Answer:
#     {answer}

#     Verification:
#     """
# )


# def verify_answer(
#     context,
#     answer,
#     llm
# ):
#     verification_chain = (
#         verification_prompt
#         | llm
#         | StrOutputParser()
#     )

#     try:
#         result = verification_chain.invoke({
#             "context": context,
#             "answer": answer
#         }).strip().upper()

#         if (
#             "NOT_SUPPORTED" in result
#             or "NOT SUPPORTED" in result
#         ):
#             return "NOT_SUPPORTED"

#         if "SUPPORTED" in result:
#             return "SUPPORTED"

#     except Exception:
#         pass

#     return "NOT_SUPPORTED"


# # ============================================================
# # 14. FORMAT SOURCE INFORMATION
# # ============================================================

# def get_source_text(documents):
#     sources = []

#     for doc in documents:
#         page = doc.metadata.get("page")

#         if page is not None:
#             page_number = page + 1
#             source = f"Page {page_number}"
#         else:
#             source = "Page information unavailable"

#         if source not in sources:
#             sources.append(source)

#     return sources


# # ============================================================
# # 15. DISPLAY CHAT HISTORY
# # ============================================================

# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # ============================================================
# # 16. SIDEBAR
# # ============================================================

# with st.sidebar:
#     st.header("⚙️ Settings")

#     retrieval_k = st.slider(
#         "Initial retrieval count",
#         min_value=2,
#         max_value=8,
#         value=4
#     )

#     rerank_k = st.slider(
#         "Documents after reranking",
#         min_value=1,
#         max_value=5,
#         value=3
#     )

#     enable_verification = st.checkbox(
#         "Enable answer verification",
#         value=True
#     )

#     if st.button("🗑️ Clear Chat"):
#         st.session_state.chat_history = []
#         st.rerun()


# # ============================================================
# # 17. PDF UPLOAD
# # ============================================================

# uploaded_file = st.file_uploader(
#     "Upload a PDF document",
#     type=["pdf"]
# )

# if uploaded_file is None:
#     st.info("Please upload a PDF to start chatting.")
#     st.stop()


# pdf_bytes = uploaded_file.getvalue()

# if not pdf_bytes:
#     st.error("The uploaded PDF is empty.")
#     st.stop()


# current_pdf_hash = hashlib.md5(
#     pdf_bytes
# ).hexdigest()


# # ============================================================
# # 18. PROCESS NEW PDF
# # ============================================================

# if (
#     st.session_state.pdf_hash != current_pdf_hash
#     or st.session_state.vector_store is None
# ):
#     with st.spinner(
#         "Loading PDF and creating vector database..."
#     ):
#         try:
#             parent_chunks = load_pdf_and_create_parent_chunks(
#                 pdf_bytes
#             )

#             if not parent_chunks:
#                 st.error(
#                     "No readable text was found in the PDF."
#                 )
#                 st.stop()

#             child_chunks, parent_store = (
#                 create_parent_child_chunks(
#                     parent_chunks
#                 )
#             )

#             embeddings = get_embeddings()

#             vector_store = create_vector_store(
#                 child_chunks,
#                 embeddings,
#                 current_pdf_hash
#             )

#             st.session_state.pdf_hash = current_pdf_hash
#             st.session_state.vector_store = vector_store
#             st.session_state.parent_store = parent_store
#             st.session_state.child_chunks = child_chunks
#             st.session_state.chat_history = []

#             st.success(
#                 f"PDF processed successfully. "
#                 f"Parents: {len(parent_store)}, "
#                 f"Children: {len(child_chunks)}"
#             )

#         except Exception as error:
#             st.error(
#                 f"PDF processing failed: {error}"
#             )
#             st.stop()


# # ============================================================
# # 19. INITIALIZE LLM
# # ============================================================

# try:
#     llm = get_llm()

# except Exception as error:
#     st.error(
#         f"LLM initialization failed: {error}"
#     )
#     st.stop()


# # ============================================================
# # 20. USER QUESTION
# # ============================================================

# question = st.chat_input(
#     "Ask a question about your PDF..."
# )

# if question:
#     question = question.strip()

#     if not question:
#         st.warning("Please enter a valid question.")
#         st.stop()

#     with st.chat_message("user"):
#         st.markdown(question)

#     st.session_state.chat_history.append({
#         "role": "user",
#         "content": question
#     })

#     try:
#         with st.spinner(
#             "Running advanced retrieval..."
#         ):
#             # --------------------------------------------
#             # Step A: Multi-Query + Parent Retrieval
#             # --------------------------------------------

#             retrieved_docs, generated_queries = (
#                 multi_query_retrieval(
#                     question=question,
#                     vector_store=st.session_state.vector_store,
#                     parent_store=st.session_state.parent_store,
#                     llm=llm,
#                     top_k=retrieval_k
#                 )
#             )

#             if not retrieved_docs:
#                 answer = (
#                     "INFORMATION_NOT_AVAILABLE"
#                 )
#                 verification_result = "NOT_SUPPORTED"
#                 compressed_docs = []

#             else:
#                 # ----------------------------------------
#                 # Step B: Reranking
#                 # ----------------------------------------

#                 reranked_docs = rerank_documents(
#                     question=question,
#                     documents=retrieved_docs,
#                     llm=llm,
#                     top_k=rerank_k
#                 )

#                 if not reranked_docs:
#                     answer = (
#                         "INFORMATION_NOT_AVAILABLE"
#                     )
#                     verification_result = "NOT_SUPPORTED"
#                     compressed_docs = []

#                 else:
#                     # ------------------------------------
#                     # Step C: Contextual Compression
#                     # ------------------------------------

#                     compressed_docs = compress_documents(
#                         question=question,
#                         documents=reranked_docs,
#                         llm=llm
#                     )

#                     if not compressed_docs:
#                         answer = (
#                             "INFORMATION_NOT_AVAILABLE"
#                         )
#                         verification_result = "NOT_SUPPORTED"

#                     else:
#                         # --------------------------------
#                         # Step D: Create Final Context
#                         # --------------------------------

#                         context = "\n\n".join(
#                             doc.page_content
#                             for doc in compressed_docs
#                         )

#                         # --------------------------------
#                         # Step E: Generate Answer
#                         # --------------------------------

#                         answer = generate_answer(
#                             question=question,
#                             context=context,
#                             llm=llm
#                         )

#                         # --------------------------------
#                         # Step F: Verify Answer
#                         # --------------------------------

#                         if (
#                             enable_verification
#                             and answer
#                             != "INFORMATION_NOT_AVAILABLE"
#                         ):
#                             verification_result = (
#                                 verify_answer(
#                                     context=context,
#                                     answer=answer,
#                                     llm=llm
#                                 )
#                             )
#                         else:
#                             verification_result = (
#                                 "NOT_SUPPORTED"
#                             )

#                         # --------------------------------
#                         # Step G: Safe Fallback
#                         # --------------------------------

#                         if (
#                             answer
#                             == "INFORMATION_NOT_AVAILABLE"
#                             or verification_result
#                             != "SUPPORTED"
#                         ):
#                             answer = (
#                                 "I could not verify a reliable "
#                                 "answer from the uploaded PDF."
#                             )

#         # ====================================================
#         # 21. DISPLAY FINAL ANSWER
#         # ====================================================

#         with st.chat_message("assistant"):
#             st.markdown(answer)

#             if enable_verification:
#                 if verification_result == "SUPPORTED":
#                     st.success(
#                         "Answer verification: SUPPORTED"
#                     )
#                 else:
#                     st.warning(
#                         "Answer verification: "
#                         "NOT SUPPORTED / UNVERIFIED"
#                     )

#             source_documents = (
#                 compressed_docs
#                 if compressed_docs
#                 else []
#             )

#             sources = get_source_text(
#                 source_documents
#             )

#             if sources:
#                 with st.expander("📚 Sources"):
#                     for source in sources:
#                         st.write(f"- {source}")

#             with st.expander("🔍 Retrieval Details"):
#                 st.write("Generated search queries:")
#                 for query in generated_queries:
#                     st.write(f"- {query}")

#                 st.write(
#                     f"Retrieved parent documents: "
#                     f"{len(retrieved_docs)}"
#                 )

#                 st.write(
#                     f"Compressed documents: "
#                     f"{len(compressed_docs)}"
#                 )

#     except Exception as error:
#         answer = (
#             "An error occurred while processing your question."
#         )

#         with st.chat_message("assistant"):
#             st.error(
#                 f"{answer}\n\nDetails: {error}"
#             )

#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })



#               < image -QUERY RAG >.                 #
# import base64
# import os

# import streamlit as st
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# st.set_page_config(
#     page_title="Multimodal RAG",
#     page_icon="📊"
# )

# st.title("📄 Multimodal RAG")
# st.write("Upload a chart image and extract information using Vision LLM.")


# # -----------------------------
# # Groq Client
# # -----------------------------

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )


# # -----------------------------
# # Image Upload
# # -----------------------------

# uploaded_file = st.file_uploader(
#     "Upload a chart image",
#     type=["png", "jpg", "jpeg"]
# )


# if uploaded_file:

#     # Display image
#     st.image(
#         uploaded_file,
#         caption="Uploaded Chart",
#         use_container_width=True
#     )

#     if st.button("🔍 Analyze Chart"):

#         with st.spinner("Analyzing chart..."):

#             # Read image
#             image_bytes = uploaded_file.read()

#             # Convert image → Base64
#             base64_image = base64.b64encode(
#                 image_bytes
#             ).decode("utf-8")

#             # Vision LLM
#             response = client.chat.completions.create(
#                 model="qwen/qwen3.8-27b",
#                 max_tokens=400,
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": [
#                             {
#                                 "type": "text",
#                                 "text": """
#                                 Analyze this chart.

#                                 Extract:
#                                 1. All labels
#                                 2. All values
#                                 3. Highest value
#                                 4. Lowest value
#                                 5. Overall trend

#                                 Do not invent any information.
#                                 """
#                             },
#                             {
#                                 "type": "image_url",
#                                 "image_url": {
#                                     "url": (
#                                         f"data:image/png;base64,"
#                                         f"{base64_image}"
#                                     )
#                                 }
#                             }
#                         ]
#                     }
#                 ]
#             )

#             description = response.choices[0].message.content

#         st.subheader("📊 Chart Information")

#         st.write(description)


#               < final project >                   #



# import base64
# import os
# import tempfile

# import fitz
# import streamlit as st
# from dotenv import load_dotenv
# from groq import Groq
# from langchain_community.document_loaders import PyPDFLoader


# # =========================
# # ENVIRONMENT
# # =========================

# load_dotenv()

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# VISION_MODEL = "qwen/qwen3.8-27b"


# # =========================
# # PAGE CONFIG
# # =========================

# st.set_page_config(
#     page_title="Multimodal PDF RAG",
#     page_icon="📄",
#     layout="wide"
# )


# # =========================
# # SIDEBAR
# # =========================

# st.sidebar.title("⚙️ Settings")

# screen_layout = st.sidebar.selectbox(
#     "🖥️ Screen Layout",
#     ["Wide screen", "Fit to screen"]
# )

# answer_mode = st.sidebar.selectbox(
#     "🧠 Answer Mode",
#     [
#         "PDF + General Knowledge",
#         "PDF Only"
#     ]
# )


# # =========================
# # SCREEN WIDTH
# # =========================

# if screen_layout == "Fit to screen":
#     st.markdown(
#         """
#         <style>
#         .block-container {
#             max-width: 900px;
#             margin: auto;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )


# # =========================
# # TITLE
# # =========================

# st.title("📄 Multimodal PDF RAG")

# st.write(
#     "Upload a PDF and ask questions about its "
#     "text, tables, charts, graphs, diagrams and images."
# )


# # =========================
# # PDF UPLOAD
# # =========================

# uploaded_file = st.file_uploader(
#     "📤 Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file:

#     # =========================
#     # SAVE PDF TEMPORARILY
#     # =========================

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temp_file:

#         temp_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temp_file.name


#     # =========================
#     # LOAD PDF TEXT
#     # =========================

#     try:

#         loader = PyPDFLoader(pdf_path)

#         documents = loader.load()

#     except Exception as e:

#         st.error(
#             f"❌ PDF load nahi ho payi: {e}"
#         )

#         st.stop()


#     # =========================
#     # CONVERT PDF PAGES TO IMAGES
#     # =========================

#     try:

#         pdf = fitz.open(pdf_path)

#         pages = []

#         for page_number, page in enumerate(pdf):

#             matrix = fitz.Matrix(
#                 1.5,
#                 1.5
#             )

#             pixmap = page.get_pixmap(
#                 matrix=matrix,
#                 alpha=False
#             )

#             image_bytes = pixmap.tobytes(
#                 "png"
#             )

#             pages.append(
#                 {
#                     "page_number": page_number + 1,
#                     "image": image_bytes,
#                     "text": documents[
#                         page_number
#                     ].page_content
#                 }
#             )

#         pdf.close()

#     except Exception as e:

#         st.error(
#             f"❌ PDF pages process nahi ho paaye: {e}"
#         )

#         st.stop()


#     st.success(
#         f"✅ PDF loaded successfully — {len(pages)} pages"
#     )


#     # =========================
#     # QUESTION FORM
#     # =========================
#     # Enter OR Ask button dono kaam karenge

#     with st.form("question_form"):

#         question = st.text_input(
#             "❓ Ask anything about your PDF",
#             placeholder="Type your question and press Enter..."
#         )

#         ask = st.form_submit_button(
#             "🔍 Ask"
#         )


#     # =========================
#     # PROCESS QUESTION
#     # =========================

#     if ask and question.strip():

#         with st.spinner(
#             "🔎 Searching the PDF and analyzing relevant content..."
#         ):

#             # =========================
#             # FIND RELEVANT PAGES
#             # =========================

#             question_words = set(
#                 question.lower().split()
#             )

#             scored_pages = []

#             for page in pages:

#                 page_text = page["text"].lower()

#                 score = sum(
#                     1
#                     for word in question_words
#                     if len(word) > 2
#                     and word in page_text
#                 )

#                 scored_pages.append(
#                     (
#                         score,
#                         page
#                     )
#                 )


#             # Highest matching pages first

#             scored_pages.sort(
#                 key=lambda x: x[0],
#                 reverse=True
#             )


#             # Pages having at least one match

#             relevant_pages = [
#                 page
#                 for score, page in scored_pages
#                 if score > 0
#             ]


#             # If no text match is found,
#             # use first few pages so that
#             # visual content can still be inspected.

#             if not relevant_pages:

#                 relevant_pages = pages


#             # Keep Vision request manageable

#             relevant_pages = relevant_pages[:3]


#             # =========================
#             # ANSWER MODE
#             # =========================

#             if answer_mode == "PDF Only":

#                 knowledge_instruction = """
# Use ONLY information available in the PDF.

# If the answer cannot be found in the PDF,
# say exactly:

# "Information not found in the PDF."

# Do not use outside knowledge.
# Do not invent information.
# """

#             else:

#                 knowledge_instruction = """
# Use information from the PDF whenever available.

# You may also use your general pretrained knowledge
# when the required information is not available in
# the PDF.

# Clearly distinguish PDF information from general
# knowledge when necessary.

# Do not invent information.
# """


#             # =========================
#             # VISION PROMPT
#             # =========================

#             content = [
#                 {
#                     "type": "text",
#                     "text": f"""
# You are answering a question about a PDF.

# The PDF may contain:

# - normal text
# - tables
# - charts
# - graphs
# - diagrams
# - images

# Carefully inspect BOTH:

# 1. Extracted PDF text
# 2. Visual content of the PDF pages

# {knowledge_instruction}

# User question:

# {question}

# Give a clear and direct answer.

# If the answer depends on a chart, table,
# graph, diagram or image, read the visual
# content carefully.

# Do not guess values that cannot be read.
# """
#                 }
#             ]


#             # =========================
#             # ADD RELEVANT PAGES
#             # =========================

#             for page in relevant_pages:

#                 base64_image = base64.b64encode(
#                     page["image"]
#                 ).decode("utf-8")


#                 # Add page text

#                 content.append(
#                     {
#                         "type": "text",
#                         "text": f"""
# ========================
# PDF PAGE {page['page_number']}
# ========================

# Extracted text:

# {page['text'][:5000]}
# """
#                     }
#                 )


#                 # Add page image

#                 content.append(
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url":
#                             f"data:image/png;base64,{base64_image}"
#                         }
#                     }
#                 )


#             # =========================
#             # CALL VISION LLM
#             # =========================

#             try:

#                 response = client.chat.completions.create(
#                     model=VISION_MODEL,
#                     max_completion_tokens=500,
#                     reasoning_effort="none",
#                     messages=[
#                         {
#                             "role": "user",
#                             "content": content
#                         }
#                     ]
#                 )


#                 answer = (
#                     response
#                     .choices[0]
#                     .message
#                     .content
#                 )


#             except Exception as e:

#                 st.error(
#                     f"❌ AI response error: {e}"
#                 )

#                 st.stop()


#         # =========================
#         # ANSWER
#         # =========================

#         st.subheader("🤖 Answer")

#         st.write(answer)


#         # =========================
#         # SOURCES
#         # =========================

#         st.subheader("📚 Sources")

#         for page in relevant_pages:

#             st.write(
#                 f"📄 Page {page['page_number']}"
#             )


#     elif ask and not question.strip():

#         st.warning(
#             "⚠️ Please enter a question."
#         )


# else:

#     st.info(
#         "📤 Upload a PDF to start asking questions."
#     )




#               < app with ui >                  #          #
import base64
import os
import tempfile

import fitz
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader


# =========================================================
# ENVIRONMENT
# =========================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found.")
    st.stop()

client = Groq(api_key=api_key)

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
# CUSTOM UI
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f6f7fb;
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    /* Main title */
    h1 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Buttons */
    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 10px;
        border: none;
        padding: 0.55rem 1.2rem;
        font-weight: 600;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #ffffff;
        border-radius: 14px;
        padding: 10px;
        border: 1px solid #e5e7eb;
    }

    /* Text input */
    [data-testid="stTextInput"] input {
        border-radius: 10px;
    }

    /* Answer box */
    .answer-box {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px;
        margin-top: 10px;
        line-height: 1.6;
    }

    /* Source box */
    .source-box {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 10px 15px;
        margin: 6px 0;
    }

    /* Alerts */
    [data-testid="stAlert"] {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
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
# HEADER
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
# WHEN PDF IS UPLOADED
# =========================================================

if uploaded_file:

    # -----------------------------------------------------
    # SAVE PDF TEMPORARILY
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
            f"❌ Could not save PDF: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # LOAD PDF TEXT
    # -----------------------------------------------------

    try:

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

    except Exception as e:

        st.error(
            f"❌ Could not load PDF: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # CONVERT PDF PAGES INTO IMAGES
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
            f"❌ Could not process PDF pages: {e}"
        )

        st.stop()


    # -----------------------------------------------------
    # SUCCESS MESSAGE
    # -----------------------------------------------------

    st.success(
        f"✅ PDF loaded successfully — {len(pages)} pages"
    )


    # =====================================================
    # QUESTION FORM
    # =====================================================
    # Enter key OR Ask button will submit the question.

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
                "⚠️ Please enter a question."
            )

            st.stop()


        with st.spinner(
            "🔎 Searching the PDF and analyzing relevant content..."
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


            # Highest matching pages first

            scored_pages.sort(
                key=lambda x: x[0],
                reverse=True
            )


            # Pages containing question keywords

            relevant_pages = [
                page
                for score, page in scored_pages
                if score > 0
            ]


            # If no text match exists,
            # allow visual inspection.

            if not relevant_pages:

                relevant_pages = pages


            # Keep request manageable

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

Clearly distinguish PDF information from general
knowledge when necessary.

Do not invent information.
"""


            # -------------------------------------------------
            # VISION MODEL PROMPT
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
            # CALL GROQ VISION MODEL
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
                    f"❌ AI response error: {e}"
                )

                st.stop()


        # =================================================
        # ANSWER
        # =================================================

        st.subheader("🤖 Answer")

        st.markdown(
            f"""
            <div class="answer-box">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # SOURCES
        # =================================================

        st.subheader("📚 Sources")

        for page in relevant_pages:

            st.markdown(
                f"""
                <div class="source-box">
                    📄 <b>Page {page['page_number']}</b>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# NO PDF MESSAGE
# =========================================================

else:

    st.info(
        "📤 Upload a PDF to start asking questions."
    )