#               < learning PypdfLoader >              #
# import streamlit as st
# import tempfile

# from langchain_community.document_loaders import PyPDFLoader


# st.set_page_config(
#     page_title="PDF Reader",
#     page_icon="📄"
# )

# st.title("📄 PDF Reader App")

# st.write("Upload a PDF to read its content.")


# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success("PDF uploaded successfully!")

#     # Step 1: Create temporary PDF file
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name

#     st.write("Temporary file created successfully.")

#     # Step 2: Load PDF using PyPDFLoader
#     loader = PyPDFLoader(pdf_path)

#     documents = loader.load()

#     # Step 3: Display total pages
#     st.write("Total pages:", len(documents))

#     # Step 4: Display extracted text
#     if documents:

#         st.subheader("Extracted Text")

#         st.write(
#             documents[0].page_content[:1000]
#         )

# else:

#     st.info("Please upload a PDF file.")





#                         < Text chunking >                         #

# import streamlit as st
# import tempfile

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma


# st.set_page_config(
#     page_title="PDF Chunking",
#     page_icon="📄"
# )

# st.title("📄 PDF Chunking App")

# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success("PDF uploaded successfully!")

#     # Step 1: Create a temporary PDF file
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name

#     # Step 2: Load PDF
#     loader = PyPDFLoader(pdf_path)

#     documents = loader.load()

#     st.write("Total pages:", len(documents))

#     # Step 3: Create text splitter
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     # Step 4: Split PDF text into chunks
#     chunks = splitter.split_documents(documents)

#     st.write("Total chunks:", len(chunks))

#     # Step 5: Display first chunk
#     if chunks:

#         st.subheader("First Chunk")

#         st.write(chunks[0].page_content)

#         st.write("Chunk metadata:")
#         st.write(chunks[0].metadata)

# else:

#     st.info("Please upload a PDF file.")







#               < Create vector store >              #


# import streamlit as st
# import tempfile

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma


# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG App")

# st.write("Upload a PDF to create chunks and store them in Chroma.")


# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success("PDF uploaded successfully!")

#     # Step 1: Create a temporary PDF file
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name

#     st.write("Temporary file created successfully.")

#     # Step 2: Load PDF using PyPDFLoader
#     loader = PyPDFLoader(pdf_path)

#     documents = loader.load()

#     st.write("Total pages:", len(documents))

#     # Step 3: Create text splitter
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     # Step 4: Split PDF into chunks
#     chunks = splitter.split_documents(documents)

#     st.write("Total chunks:", len(chunks))

#     # Step 5: Display first chunk
#     if chunks:

#         st.subheader("First Chunk")

#         st.write(
#             chunks[0].page_content
#         )

#         st.write("Chunk metadata:")

#         st.write(
#             chunks[0].metadata
#         )

#     # Step 6: Create embedding model
#     with st.spinner("Creating embeddings..."):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )

#     # Step 7: Store chunks and embeddings in Chroma
#     with st.spinner("Storing chunks in Chroma..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name="streamlit_pdf_rag"
#         )

#     st.success(
# #         "Chunks stored in Chroma successfully!"
# #     )

# # else:

# #     st.info("Please upload a PDF file.")


# #           < Retriever ka complete final code >          #

# import streamlit as st
# import tempfile

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma


# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG App")

# st.write(
#     "Upload a PDF and retrieve relevant text chunks."
# )


# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success("PDF uploaded successfully!")

#     # Step 1: Create a temporary PDF file
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name

#     st.write("Temporary file created successfully.")

#     # Step 2: Load PDF using PyPDFLoader
#     loader = PyPDFLoader(pdf_path)

#     documents = loader.load()

#     st.write("Total pages:", len(documents))

#     # Step 3: Create text splitter
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     # Step 4: Split PDF into chunks
#     chunks = splitter.split_documents(documents)

#     st.write("Total chunks:", len(chunks))

#     # Step 5: Display first chunk
#     if chunks:

#         st.subheader("First Chunk")

#         st.write(
#             chunks[0].page_content
#         )

#         st.write("Chunk metadata:")

#         st.write(
#             chunks[0].metadata
#         )

#     # Step 6: Create embedding model
#     with st.spinner("Creating embeddings..."):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )

#     # Step 7: Store chunks and embeddings in Chroma
#     with st.spinner("Storing chunks in Chroma..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name="streamlit_pdf_rag"
#         )

#     st.success(
#         "Chunks stored in Chroma successfully!"
#     )

#     # Step 8: Create retriever
#     retriever = vector_store.as_retriever(
#         search_kwargs={"k": 3}
#     )

#     # Step 9: Ask a question
#     question = st.text_input(
#         "Ask a question about your PDF"
#     )

#     if question:

#         # Step 10: Retrieve relevant chunks
#         relevant_chunks = retriever.invoke(
#             question
#         )

#         st.subheader("Retrieved Chunks")

#         st.write(
#             "Number of retrieved chunks:",
#             len(relevant_chunks)
#         )

#         # Step 11: Display retrieved chunks
#         for i, chunk in enumerate(
#             relevant_chunks,
#             start=1
#         ):

#             st.write(f"### Chunk {i}")

#             st.write(
#                 chunk.page_content
#             )

#             st.write(
#                 "Metadata:",
#                 chunk.metadata
#             )

# else:

#     st.info("Please upload a PDF file.")



#     #           < Retriever + Prompt + LLM → Final Answer >         #




# import streamlit as st
# import tempfile

# from pathlib import Path
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# # Load environment variables
# project_folder = Path(__file__).resolve().parent

# load_dotenv(
#     project_folder / ".env"
# )


# # Streamlit page configuration
# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )


# st.title("📄 PDF RAG App")

# st.write(
#     "Upload a PDF and ask questions about it."
# )


# # PDF upload
# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success(
#         "PDF uploaded successfully!"
#     )

#     # Step 1: Create temporary PDF file
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name


#     # Step 2: Load PDF
#     loader = PyPDFLoader(
#         pdf_path
#     )

#     documents = loader.load()


#     # Step 3: Split documents into chunks
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.split_documents(
#         documents
#     )


#     # Step 4: Create embeddings
#     with st.spinner(
#         "Creating embeddings..."
#     ):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )


#     # Step 5: Store chunks in Chroma
#     with st.spinner(
#         "Storing chunks in Chroma..."
#     ):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name="streamlit_pdf_rag"
#         )


#     # Step 6: Create retriever
#     retriever = vector_store.as_retriever(
#         search_kwargs={
#             "k": 3
#         }
#     )


#     # Step 7: Create LLM
#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


#     # Step 8: Create prompt template
#     prompt = PromptTemplate.from_template(
#         """
#         Answer the question using only the
#         provided context.

#         If the answer is not available in the
#         context, say:

#         "The information is not available
#         in the provided document."

#         Do not use outside knowledge.

#         Context:
#         {context}

#         Question:
#         {question}

#         Answer:
#         """
#     )


#     # Step 9: Create RAG chain
#     rag_chain = (
#         prompt
#         | llm
#         | StrOutputParser()
#     )


#     # Step 10: Ask a question
#     question = st.text_input(
#         "Ask a question about your PDF"
#     )


#     if question:

#         with st.spinner(
#             "Searching and generating answer..."
#         ):

#             # Retrieve relevant chunks
#             relevant_chunks = retriever.invoke(
#                 question
#             )


#             # Combine retrieved chunks
#             context = "\n\n".join(
#                 chunk.page_content
#                 for chunk in relevant_chunks
#             )


#             # Generate final answer
#             response = rag_chain.invoke(
#                 {
#                     "context": context,
#                     "question": question
#                 }
#             )


#         # Display final answer
#         st.subheader("Answer")

#         st.write(response)


# else:

#     st.info(
#         "Please upload a PDF file."
#     )


#               <source citation >             #        #
    

# import streamlit as st
# import tempfile

# from pathlib import Path
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# # ==========================================
# # 1. Load environment variables
# # ==========================================

# project_folder = Path(__file__).resolve().parent

# load_dotenv(
#     project_folder / ".env"
# )


# # ==========================================
# # 2. Streamlit page configuration
# # ==========================================

# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG App")

# st.write(
#     "Upload a PDF and ask questions about it."
# )


# # ==========================================
# # 3. PDF upload
# # ==========================================

# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success(
#         "PDF uploaded successfully!"
#     )


#     # ==========================================
#     # 4. Create temporary PDF file
#     # ==========================================

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name


#     # ==========================================
#     # 5. Load PDF
#     # ==========================================

#     with st.spinner(
#         "Loading PDF..."
#     ):

#         loader = PyPDFLoader(
#             pdf_path
#         )

#         documents = loader.load()


#     st.write(
#         "Total pages:",
#         len(documents)
#     )


#     # ==========================================
#     # 6. Split documents into chunks
#     # ==========================================

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.split_documents(
#         documents
#     )


#     st.write(
#         "Total chunks:",
#         len(chunks)
#     )


#     # ==========================================
#     # 7. Create embeddings
#     # ==========================================

#     with st.spinner(
#         "Creating embeddings..."
#     ):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )


#     # ==========================================
#     # 8. Store chunks in ChromaDB
#     # ==========================================

#     with st.spinner(
#         "Storing chunks in ChromaDB..."
#     ):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name="streamlit_pdf_rag"
#         )


#     st.success(
#         "PDF processed successfully!"
#     )


#     # ==========================================
#     # 9. Create retriever
#     # ==========================================

#     retriever = vector_store.as_retriever(
#         search_kwargs={
#             "k": 3
#         }
#     )


#     # ==========================================
#     # 10. Create Groq LLM
#     # ==========================================

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


#     # ==========================================
#     # 11. Create prompt template
#     # ==========================================

#     prompt = PromptTemplate.from_template(
#         """
#         You are a document question-answering assistant.

#         Answer the question ONLY using the
#         provided context.

#         Important rules:

#         1. Do not use your own knowledge.
#         2. Do not make assumptions.
#         3. If the context does not clearly contain
#            the answer, respond with:

#            The information is not available
#            in the provided document.

#         4. Do not create an answer from unrelated
#            context.

#         Context:
#         {context}

#         Question:
#         {question}

#         Answer:
#         """
#     )


#     # ==========================================
#     # 12. Create RAG chain
#     # ==========================================

#     rag_chain = (
#         prompt
#         | llm
#         | StrOutputParser()
#     )


#     # ==========================================
#     # 13. User question
#     # ==========================================

#     question = st.text_input(
#         "Ask a question about your PDF"
#     )


#     if question:

#         with st.spinner(
#             "Searching and generating answer..."
#         ):


#             # ==========================================
#             # 14. Retrieve relevant chunks
#             # ==========================================

#             relevant_chunks = retriever.invoke(
#                 question
#             )


#             # ==========================================
#             # 15. Combine chunks into context
#             # ==========================================

#             context = "\n\n".join(
#                 chunk.page_content
#                 for chunk in relevant_chunks
#             )


#             # ==========================================
#             # 16. Generate final answer
#             # ==========================================

#             response = rag_chain.invoke(
#                 {
#                     "context": context,
#                     "question": question
#                 }
#             )


#         # ==========================================
#         # 17. Display final answer
#         # ==========================================

#         st.subheader("Answer")

#         st.write(
#             response
#         )


#         # ==========================================
#         # 18. Display source citations
#         # ==========================================

#         st.subheader("Sources")

#         source_pages = set()


#         for chunk in relevant_chunks:

#             page_number = (
#                 chunk.metadata.get(
#                     "page",
#                     0
#                 ) + 1
#             )

#             source_pages.add(
#                 page_number
#             )


#         for page in sorted(
#             source_pages
#         ):

#             st.write(
#                 f"📄 Page {page}"
#             )


# else:

#     st.info(
#         "Please upload a PDF file."
#     )



#               < Source Content Verification >             #



# import streamlit as st
# import tempfile
# import uuid

# from pathlib import Path
# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# # ==========================================
# # 1. Load environment variables
# # ==========================================

# project_folder = Path(__file__).resolve().parent

# load_dotenv(project_folder / ".env")


# # ==========================================
# # 2. Streamlit configuration
# # ==========================================

# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG App")

# st.write(
#     "Upload a PDF and ask questions about it."
# )


# # ==========================================
# # 3. PDF upload
# # ==========================================

# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success("PDF uploaded successfully!")


#     # ==========================================
#     # 4. Create temporary PDF file
#     # ==========================================

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name


#     # ==========================================
#     # 5. Load PDF
#     # ==========================================

#     with st.spinner("Loading PDF..."):

#         loader = PyPDFLoader(pdf_path)

#         documents = loader.load()


#     st.write(
#         "Total pages:",
#         len(documents)
#     )


#     # ==========================================
#     # 6. Split PDF into chunks
#     # ==========================================

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.split_documents(
#         documents
#     )


#     st.write(
#         "Total chunks:",
#         len(chunks)
#     )


#     # ==========================================
#     # 7. Create embeddings
#     # ==========================================

#     with st.spinner("Creating embeddings..."):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )


#     # ==========================================
#     # 8. Create unique Chroma collection
#     # ==========================================

#     collection_name = (
#         "pdf_rag_"
#         + uuid.uuid4().hex
#     )


#     with st.spinner("Storing chunks in ChromaDB..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name=collection_name
#         )


#     st.success("PDF processed successfully!")


#     # ==========================================
#     # 9. Create MMR retriever
#     # ==========================================

#     retriever = vector_store.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k": 3,
#             "fetch_k": 10,
#             "lambda_mult": 0.7
#         }
#     )


#     # ==========================================
#     # 10. Create Groq LLM
#     # ==========================================

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


#     # ==========================================
#     # 11. Create prompt template
#     # ==========================================

#     prompt = PromptTemplate.from_template(
#         """
#         You are a helpful PDF question-answering assistant.

#         Answer the question ONLY using the provided context.

#         Rules:
#         1. Do not use outside knowledge.
#         2. Do not make assumptions.
#         3. Do not use unrelated information.
#         4. Give a concise answer in 3 to 5 sentences
#            when the question needs an explanation.
#         5. Use bullet points when appropriate.
#         6. If the answer is not clearly available
#            in the context, say exactly:

#            The information is not available
#            in the provided document.

#         Context:
#         {context}

#         Question:
#         {question}

#         Answer:
#         """
#     )


#     # ==========================================
#     # 12. Create RAG chain
#     # ==========================================

#     rag_chain = (
#         prompt
#         | llm
#         | StrOutputParser()
#     )


#     # ==========================================
#     # 13. User question
#     # ==========================================

#     question = st.text_input(
#         "Ask a question about your PDF"
#     )


#     if question.strip():

#         with st.spinner(
#             "Searching and generating answer..."
#         ):


#             # ==========================================
#             # 14. Retrieve relevant chunks
#             # ==========================================

#             relevant_chunks = retriever.invoke(
#                 question
#             )


#             # ==========================================
#             # 15. Remove duplicate chunks
#             # ==========================================

#             unique_chunks = []

#             seen_chunks = set()


#             for chunk in relevant_chunks:

#                 chunk_text = (
#                     chunk.page_content.strip()
#                 )

#                 if (
#                     chunk_text
#                     and chunk_text not in seen_chunks
#                 ):

#                     seen_chunks.add(
#                         chunk_text
#                     )

#                     unique_chunks.append(
#                         chunk
#                     )


#             # ==========================================
#             # 16. Create context
#             # ==========================================

#             context = "\n\n".join(
#                 chunk.page_content
#                 for chunk in unique_chunks
#             )


#             # ==========================================
#             # 17. Generate final answer
#             # ==========================================

#             response = rag_chain.invoke(
#                 {
#                     "context": context,
#                     "question": question
#                 }
#             )


#         # ==========================================
#         # 18. Display answer
#         # ==========================================

#         st.subheader("Answer")

#         st.write(response)


#         # ==========================================
#         # 19. Display sources
#         # ==========================================

#         st.subheader("Sources")


#         if unique_chunks:

#             displayed_sources = set()


#             for index, chunk in enumerate(
#                 unique_chunks,
#                 start=1
#             ):

#                 page_number = (
#                     chunk.metadata.get(
#                         "page",
#                         0
#                     ) + 1
#                 )

#                 source_key = (
#                     page_number,
#                     chunk.page_content.strip()
#                 )


#                 if source_key in displayed_sources:

#                     continue


#                 displayed_sources.add(
#                     source_key
#                 )


#                 with st.expander(
#                     f"📄 Source {index} - Page {page_number}"
#                 ):

#                     st.write(
#                         chunk.page_content
#                     )


#         else:

#             st.info(
#                 "No relevant sources were retrieved."
#             )


# else:

#     st.info(
#         "Please upload a PDF file."
#     )


#           < Compression Retriever >           # 



# import streamlit as st
# import tempfile
# import uuid

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


# # ==========================================
# # 1. Load environment variables
# # ==========================================

# project_folder = Path(__file__).resolve().parent

# load_dotenv(
#     project_folder / ".env"
# )


# # ==========================================
# # 2. Streamlit configuration
# # ==========================================

# st.set_page_config(
#     page_title="PDF RAG App",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG App")

# st.write(
#     "Upload a PDF and ask questions about it."
# )


# # ==========================================
# # 3. PDF upload
# # ==========================================

# uploaded_file = st.file_uploader(
#     "Choose a PDF file",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success(
#         "PDF uploaded successfully!"
#     )


#     # ==========================================
#     # 4. Create temporary PDF file
#     # ==========================================

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temporary_file:

#         temporary_file.write(
#             uploaded_file.getvalue()
#         )

#         pdf_path = temporary_file.name


#     # ==========================================
#     # 5. Load PDF
#     # ==========================================

#     with st.spinner(
#         "Loading PDF..."
#     ):

#         loader = PyPDFLoader(
#             pdf_path
#         )

#         documents = loader.load()


#     st.write(
#         "Total pages:",
#         len(documents)
#     )


#     # ==========================================
#     # 6. Split PDF into chunks
#     # ==========================================

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.split_documents(
#         documents
#     )


#     st.write(
#         "Total chunks:",
#         len(chunks)
#     )


#     # ==========================================
#     # 7. Create embeddings
#     # ==========================================

#     with st.spinner(
#         "Creating embeddings..."
#     ):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )


#     # ==========================================
#     # 8. Create unique Chroma collection
#     # ==========================================

#     collection_name = (
#         "pdf_rag_"
#         + uuid.uuid4().hex
#     )


#     with st.spinner(
#         "Storing chunks in ChromaDB..."
#     ):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name=collection_name
#         )


#     st.success(
#         "PDF processed successfully!"
#     )


#     # ==========================================
#     # 9. Create Groq LLM
#     # ==========================================

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


#     # ==========================================
#     # 10. Create MMR retriever
#     # ==========================================

#     base_retriever = vector_store.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k": 3,
#             "fetch_k": 10,
#             "lambda_mult": 0.7
#         }
#     )


#     # ==========================================
#     # 11. Create compression prompt
#     # ==========================================

#     compression_prompt = PromptTemplate.from_template(
#         """
#         You are a document relevance filter.

#         Extract only the information from the
#         context that is directly relevant to
#         the user's question.

#         Rules:
#         1. Keep only relevant information.
#         2. Remove unrelated information.
#         3. Do not add outside knowledge.
#         4. Preserve important facts and details.
#         5. If the context has no relevant information,
#            return exactly: EMPTY

#         Context:
#         {context}

#         Question:
#         {question}

#         Relevant information:
#         """
#     )


#     # ==========================================
#     # 12. Create compression chain
#     # ==========================================

#     compression_chain = (
#         compression_prompt
#         | llm
#         | StrOutputParser()
#     )


#     # ==========================================
#     # 13. Compression function
#     # ==========================================

#     def compress_documents(
#         question,
#         documents
#     ):

#         compressed_documents = []

#         for document in documents:

#             compressed_text = (
#                 compression_chain.invoke(
#                     {
#                         "context": document.page_content,
#                         "question": question
#                     }
#                 )
#             )

#             compressed_text = (
#                 compressed_text.strip()
#             )


#             if (
#                 compressed_text
#                 and compressed_text.upper() != "EMPTY"
#             ):

#                 compressed_documents.append(
#                     Document(
#                         page_content=compressed_text,
#                         metadata=document.metadata
#                     )
#                 )


#         return compressed_documents


#     # ==========================================
#     # 14. Create final answer prompt
#     # ==========================================

#     answer_prompt = PromptTemplate.from_template(
#         """
#         You are a helpful PDF question-answering assistant.

#         Answer the question ONLY using the provided context.

#         Rules:
#         1. Do not use outside knowledge.
#         2. Do not make assumptions.
#         3. Do not use unrelated information.
#         4. Give a concise answer in 3 to 5 sentences
#            when an explanation is needed.
#         5. Use bullet points when appropriate.
#         6. If the answer is not clearly available
#            in the context, say:

#            The information is not available
#            in the provided document.

#         Context:
#         {context}

#         Question:
#         {question}

#         Answer:
#         """
#     )


#     # ==========================================
#     # 15. Create final RAG chain
#     # ==========================================

#     rag_chain = (
#         answer_prompt
#         | llm
#         | StrOutputParser()
#     )


#     # ==========================================
#     # 16. User question
#     # ==========================================

#     question = st.text_input(
#         "Ask a question about your PDF"
#     )


#     if question.strip():

#         with st.spinner(
#             "Retrieving relevant chunks..."
#         ):

#             # ==========================================
#             # 17. Retrieve original chunks
#             # ==========================================

#             retrieved_chunks = (
#                 base_retriever.invoke(
#                     question
#                 )
#             )


#         with st.spinner(
#             "Compressing context..."
#         ):

#             # ==========================================
#             # 18. Compress retrieved chunks
#             # ==========================================

#             relevant_chunks = (
#                 compress_documents(
#                     question,
#                     retrieved_chunks
#                 )
#             )


#         # ==========================================
#         # 19. Remove duplicate chunks
#         # ==========================================

#         unique_chunks = []

#         seen_chunks = set()


#         for chunk in relevant_chunks:

#             chunk_text = (
#                 chunk.page_content.strip()
#             )


#             if (
#                 chunk_text
#                 and chunk_text not in seen_chunks
#             ):

#                 seen_chunks.add(
#                     chunk_text
#                 )

#                 unique_chunks.append(
#                     chunk
#                 )


#         # ==========================================
#         # 20. Create final context
#         # ==========================================

#         context = "\n\n".join(
#             chunk.page_content
#             for chunk in unique_chunks
#         )


#         # ==========================================
#         # 21. Generate final answer
#         # ==========================================

#         if context.strip():

#             with st.spinner(
#                 "Generating final answer..."
#             ):

#                 response = rag_chain.invoke(
#                     {
#                         "context": context,
#                         "question": question
#                     }
#                 )

#         else:

#             response = (
#                 "The information is not available "
#                 "in the provided document."
#             )


#         # ==========================================
#         # 22. Display answer
#         # ==========================================

#         st.subheader(
#             "Answer"
#         )

#         st.write(
#             response
#         )


#         # ==========================================
#         # 23. Display sources
#         # ==========================================

#         st.subheader(
#             "Sources"
#         )


#         if unique_chunks:

#             displayed_sources = set()


#             for index, chunk in enumerate(
#                 unique_chunks,
#                 start=1
#             ):

#                 page_number = (
#                     chunk.metadata.get(
#                         "page",
#                         0
#                     ) + 1
#                 )


#                 source_key = (
#                     page_number,
#                     chunk.page_content.strip()
#                 )


#                 if source_key in displayed_sources:

#                     continue


#                 displayed_sources.add(
#                     source_key
#                 )


#                 with st.expander(
#                     f"📄 Source {index} - Page {page_number}"
#                 ):

#                     st.write(
#                         chunk.page_content
#                     )


#         else:

#             st.info(
#                 "No relevant sources were retrieved."
#             )


# else:

#     st.info(
#         "Please upload a PDF file."
#     )



#               < Chat History ka complete code integration >             #



# import streamlit as st
# import tempfile
# import uuid
# from pathlib import Path

# from dotenv import load_dotenv

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# from langchain_groq import ChatGroq

# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# # --------------------------------------------------
# # 1. Page Configuration
# # --------------------------------------------------

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📚",
#     layout="wide"
# )

# st.title("📚 PDF RAG Chatbot")
# st.write("Upload a PDF and ask multiple questions about it.")


# # --------------------------------------------------
# # 2. Load Environment Variables
# # --------------------------------------------------

# project_folder = Path(__file__).resolve().parent
# load_dotenv(project_folder / ".env")


# # --------------------------------------------------
# # 3. Initialize Chat History
# # --------------------------------------------------

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# # --------------------------------------------------
# # 4. New Chat Button
# # --------------------------------------------------

# if st.button("🗑️ Clear Chat History"):
#     st.session_state.chat_history = []
#     st.rerun()


# # --------------------------------------------------
# # 5. PDF Upload
# # --------------------------------------------------

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is not None:

#     st.success(f"Uploaded: {uploaded_file.name}")


#     # --------------------------------------------------
#     # 6. Save Uploaded PDF Temporarily
#     # --------------------------------------------------

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temp_file:

#         temp_file.write(uploaded_file.getvalue())
#         pdf_path = temp_file.name


#     # --------------------------------------------------
#     # 7. Load PDF
#     # --------------------------------------------------

#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()


#     # --------------------------------------------------
#     # 8. Split Documents into Chunks
#     # --------------------------------------------------

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = text_splitter.split_documents(documents)


#     # --------------------------------------------------
#     # 9. Create Embeddings
#     # --------------------------------------------------

#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


#     # --------------------------------------------------
#     # 10. Create Chroma Vector Store
#     # --------------------------------------------------

#     vector_store = Chroma.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#         collection_name=f"pdf_rag_{uuid.uuid4().hex}"
#     )


#     # --------------------------------------------------
#     # 11. Create MMR Retriever
#     # --------------------------------------------------

#     retriever = vector_store.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k": 3,
#             "fetch_k": 10,
#             "lambda_mult": 0.7
#         }
#     )


#     # --------------------------------------------------
#     # 12. Initialize LLM
#     # --------------------------------------------------

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )


#     # --------------------------------------------------
#     # 13. Create Final RAG Prompt
#     # --------------------------------------------------

#     rag_prompt = PromptTemplate.from_template(
#         """
# You are a helpful PDF assistant.

# Answer the user's question using ONLY the provided PDF context
# and conversation history.

# Rules:
# 1. Do not invent information.
# 2. If the answer is not available in the PDF context, say:
#    "Information not available in the uploaded PDF."
# 3. Keep the answer clear and concise.
# 4. Use conversation history only to understand references
#    such as "it", "this", or "that".
# 5. Do not answer unrelated questions using outside knowledge.

# Conversation History:
# {chat_history}

# PDF Context:
# {context}

# Current Question:
# {question}

# Answer:
# """
#     )


#     # --------------------------------------------------
#     # 14. Create RAG Chain
#     # --------------------------------------------------

#     rag_chain = rag_prompt | llm | StrOutputParser()


#     # --------------------------------------------------
#     # 15. Display Previous Chat History
#     # --------------------------------------------------

#     st.subheader("💬 Conversation")

#     for message in st.session_state.chat_history:

#         if message["role"] == "user":

#             with st.chat_message("user"):
#                 st.write(message["content"])

#         else:

#             with st.chat_message("assistant"):
#                 st.write(message["content"])


#     # --------------------------------------------------
#     # 16. User Question Input
#     # --------------------------------------------------

#     question = st.chat_input(
#         "Ask a question about your PDF..."
#     )


#     if question:

#         # --------------------------------------------------
#         # 17. Retrieve Relevant Chunks
#         # --------------------------------------------------

#         retrieved_chunks = retriever.invoke(question)


#         # --------------------------------------------------
#         # 18. Remove Duplicate Chunks
#         # --------------------------------------------------

#         unique_chunks = []
#         seen_chunks = set()

#         for chunk in retrieved_chunks:

#             text = chunk.page_content.strip()

#             if text not in seen_chunks:

#                 seen_chunks.add(text)
#                 unique_chunks.append(chunk)


#         # --------------------------------------------------
#         # 19. Build PDF Context
#         # --------------------------------------------------

#         context = "\n\n".join(
#             chunk.page_content
#             for chunk in unique_chunks
#         )


#         # --------------------------------------------------
#         # 20. Build Conversation History
#         # --------------------------------------------------

#         history_text = "\n".join(
#             f"{message['role']}: {message['content']}"
#             for message in st.session_state.chat_history
#         )


#         # --------------------------------------------------
#         # 21. Generate Final Answer
#         # --------------------------------------------------

#         with st.spinner("Thinking..."):

#             answer = rag_chain.invoke(
#                 {
#                     "chat_history": history_text,
#                     "context": context,
#                     "question": question
#                 }
#             )


#         # --------------------------------------------------
#         # 22. Save User Question and AI Answer
#         # --------------------------------------------------

#         st.session_state.chat_history.append(
#             {
#                 "role": "user",
#                 "content": question
#             }
#         )

#         st.session_state.chat_history.append(
#             {
#                 "role": "assistant",
#                 "content": answer
#             }
#         )


#         # --------------------------------------------------
#         # 23. Display Latest Answer
#         # --------------------------------------------------

#         with st.chat_message("user"):
#             st.write(question)

#         with st.chat_message("assistant"):
#             st.write(answer)


#         # --------------------------------------------------
#         # 24. Display Sources
#         # --------------------------------------------------

#         st.subheader("📌 Sources")

#         for index, chunk in enumerate(unique_chunks):

#             page_number = chunk.metadata.get("page", 0) + 1

#             with st.expander(
#                 f"Source {index + 1} — Page {page_number}"
#             ):

#                 st.write(chunk.page_content)


#               < Final code: Relevance Filtering + Exact Compression>  #



# import streamlit as st
# import tempfile
# import uuid
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


# # ==================================================
# # 1. PAGE CONFIGURATION
# # ==================================================

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📚",
#     layout="wide"
# )

# st.title("📚 PDF RAG Chatbot")
# st.write("Upload a PDF and ask questions about its content.")


# # ==================================================
# # 2. LOAD ENVIRONMENT VARIABLES
# # ==================================================

# project_folder = Path(__file__).resolve().parent

# load_dotenv(project_folder / ".env")


# # ==================================================
# # 3. CHAT HISTORY
# # ==================================================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# if st.button("🗑️ Clear Chat History"):

#     st.session_state.chat_history = []

#     st.rerun()


# # ==================================================
# # 4. PDF UPLOAD
# # ==================================================

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is None:

#     st.info("Please upload a PDF to start.")

#     st.stop()


# st.success(f"Uploaded: {uploaded_file.name}")


# # ==================================================
# # 5. SAVE PDF TEMPORARILY
# # ==================================================

# with tempfile.NamedTemporaryFile(
#     delete=False,
#     suffix=".pdf"
# ) as temp_file:

#     temp_file.write(uploaded_file.getvalue())

#     pdf_path = temp_file.name


# # ==================================================
# # 6. LOAD PDF
# # ==================================================

# loader = PyPDFLoader(pdf_path)

# documents = loader.load()


# # ==================================================
# # 7. TEXT CHUNKING
# # ==================================================

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# chunks = text_splitter.split_documents(documents)


# # ==================================================
# # 8. EMBEDDINGS
# # ==================================================

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# # ==================================================
# # 9. CHROMA VECTOR STORE
# # ==================================================

# vector_store = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     collection_name=f"pdf_rag_{uuid.uuid4().hex}"
# )


# # ==================================================
# # 10. MMR RETRIEVER
# # ==================================================

# # MMR tries to retrieve relevant and diverse chunks.
# # It reduces duplicate/similar chunks.
# # MMR alone does NOT guarantee that every chunk is relevant.

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # ==================================================
# # 11. INITIALIZE LLM
# # ==================================================

# llm = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0
# )


# # ==================================================
# # 12. RELEVANCE GRADING PROMPT
# # ==================================================

# relevance_prompt = PromptTemplate.from_template(
#     """
# You are a strict relevance classifier.

# Decide whether the given PDF context contains information
# that can help answer the user's question.

# Return ONLY one of these exact outputs:

# RELEVANT
# NOT_RELEVANT

# Do not explain your decision.

# PDF Context:
# {context}

# User Question:
# {question}

# Decision:
# """
# )


# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# # ==================================================
# # 13. FILTER RELEVANT DOCUMENTS
# # ==================================================

# def filter_relevant_documents(question, documents):

#     relevant_documents = []

#     for document in documents:

#         result = relevance_chain.invoke(
#             {
#                 "context": document.page_content,
#                 "question": question
#             }
#         ).strip().upper()

#         # Exact check avoids treating NOT_RELEVANT
#         # as RELEVANT.

#         if result == "RELEVANT":

#             relevant_documents.append(document)

#     return relevant_documents


# # ==================================================
# # 14. EXACT CONTEXT COMPRESSION
# # ==================================================

# compression_prompt = PromptTemplate.from_template(
#     """
# You are an extractive context compressor.

# Your task is to extract only the exact sentences
# from the PDF context that help answer the question.

# STRICT RULES:
# 1. Copy sentences exactly from the PDF context.
# 2. Do not rewrite or paraphrase.
# 3. Do not add new information.
# 4. Do not make assumptions.
# 5. If no exact relevant sentence exists, return EMPTY.
# 6. Return only the extracted sentences or EMPTY.

# PDF Context:
# {context}

# Question:
# {question}

# Extracted Text:
# """
# )


# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_documents(question, documents):

#     compressed_documents = []

#     for document in documents:

#         compressed_text = compression_chain.invoke(
#             {
#                 "context": document.page_content,
#                 "question": question
#             }
#         ).strip()

#         if not compressed_text:
#             continue

#         if compressed_text.upper() == "EMPTY":
#             continue

#         # Preserve the original document metadata.
#         # This keeps the original page number.

#         compressed_document = Document(
#             page_content=compressed_text,
#             metadata=document.metadata
#         )

#         compressed_documents.append(compressed_document)

#     return compressed_documents


# # ==================================================
# # 15. FINAL RAG PROMPT
# # ==================================================

# rag_prompt = PromptTemplate.from_template(
#     """
# You are a helpful PDF assistant.

# Answer the question using ONLY the provided PDF context.

# Conversation history is provided only to understand
# references such as "it", "this", or "that".

# STRICT RULES:
# 1. Do not use outside knowledge.
# 2. Do not invent information.
# 3. If the answer is not present in the context, return exactly:
#    Information not available in the uploaded PDF.
# 4. Keep the answer clear and concise.
# 5. Do not mention sources that are not present in the context.

# Conversation History:
# {chat_history}

# PDF Context:
# {context}

# Current Question:
# {question}

# Answer:
# """
# )


# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # ==================================================
# # 16. DISPLAY PREVIOUS CHAT HISTORY
# # ==================================================

# st.subheader("💬 Conversation")


# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):

#         st.write(message["content"])


# # ==================================================
# # 17. USER QUESTION
# # ==================================================

# question = st.chat_input(
#     "Ask a question about your PDF..."
# )


# if question:

#     # --------------------------------------------------
#     # A. RETRIEVE CHUNKS USING MMR
#     # --------------------------------------------------

#     retrieved_chunks = retriever.invoke(question)


#     # --------------------------------------------------
#     # B. REMOVE DUPLICATE CHUNKS
#     # --------------------------------------------------

#     unique_chunks = []

#     seen_chunks = set()

#     for chunk in retrieved_chunks:

#         text = chunk.page_content.strip()

#         if text not in seen_chunks:

#             seen_chunks.add(text)

#             unique_chunks.append(chunk)


#     # --------------------------------------------------
#     # C. RELEVANCE FILTERING
#     # --------------------------------------------------

#     with st.spinner("Checking document relevance..."):

#         relevant_chunks = filter_relevant_documents(
#             question,
#             unique_chunks
#         )


#     # --------------------------------------------------
#     # D. COMPRESS ONLY RELEVANT CHUNKS
#     # --------------------------------------------------

#     compressed_chunks = []

#     if relevant_chunks:

#         with st.spinner("Extracting relevant context..."):

#             compressed_chunks = compress_documents(
#                 question,
#                 relevant_chunks
#             )


#     # --------------------------------------------------
#     # E. BUILD CONVERSATION HISTORY
#     # --------------------------------------------------

#     history_text = "\n".join(
#         f"{message['role']}: {message['content']}"
#         for message in st.session_state.chat_history
#     )


#     # --------------------------------------------------
#     # F. GENERATE ANSWER ONLY IF CONTEXT EXISTS
#     # --------------------------------------------------

#     unavailable_message = (
#         "Information not available in the uploaded PDF."
#     )


#     if not compressed_chunks:

#         answer = unavailable_message

#     else:

#         context = "\n\n".join(
#             document.page_content
#             for document in compressed_chunks
#         )

#         with st.spinner("Generating answer..."):

#             answer = rag_chain.invoke(
#                 {
#                     "chat_history": history_text,
#                     "context": context,
#                     "question": question
#                 }
#             ).strip()


#     # --------------------------------------------------
#     # G. SAVE CHAT HISTORY
#     # --------------------------------------------------

#     st.session_state.chat_history.append(
#         {
#             "role": "user",
#             "content": question
#         }
#     )

#     st.session_state.chat_history.append(
#         {
#             "role": "assistant",
#             "content": answer
#         }
#     )


#     # --------------------------------------------------
#     # H. DISPLAY LATEST ANSWER
#     # --------------------------------------------------

#     with st.chat_message("user"):

#         st.write(question)


#     with st.chat_message("assistant"):

#         st.write(answer)


#     # --------------------------------------------------
#     # I. DISPLAY SOURCES ONLY IF ANSWER IS AVAILABLE
#     # --------------------------------------------------

#     answer_is_unavailable = (
#         answer.strip().lower()
#         == unavailable_message.lower()
#     )


#     if compressed_chunks and not answer_is_unavailable:

#         st.subheader("📌 Sources")

#         for index, compressed_document in enumerate(
#             compressed_chunks
#         ):

#             page_number = (
#                 compressed_document.metadata.get("page", 0) + 1
#             )

#             with st.expander(
#                 f"Source {index + 1} — Page {page_number}"
#             ):

#                 st.write(
#                     "Relevant extracted text:"
#                 )

#                 st.write(
#                     compressed_document.page_content
#                 )




#               < Error Handling >                      #


# import streamlit as st
# import tempfile
# import uuid
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


# # -----------------------------
# # CONFIGURATION
# # -----------------------------

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📄",
#     layout="wide"
# )

# st.title("📄 PDF RAG Chatbot")

# project_folder = Path(__file__).resolve().parent
# load_dotenv(project_folder / ".env")


# # -----------------------------
# # SESSION STATE
# # -----------------------------

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# if st.button("🗑️ Clear Chat History"):
#     st.session_state.chat_history = []
#     st.rerun()


# # -----------------------------
# # PDF UPLOAD
# # -----------------------------

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is None:
#     st.info("Please upload a PDF to start chatting.")
#     st.stop()


# # -----------------------------
# # SAVE PDF TEMPORARILY
# # -----------------------------

# pdf_bytes = uploaded_file.getvalue()

# try:
#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temp_file:

#         temp_file.write(pdf_bytes)
#         pdf_path = temp_file.name

# except Exception:
#     st.error("Unable to save the uploaded PDF.")
#     st.stop()


# # -----------------------------
# # LOAD PDF
# # -----------------------------

# try:
#     with st.spinner("Loading PDF..."):

#         loader = PyPDFLoader(pdf_path)
#         documents = loader.load()

#     st.success("PDF loaded successfully!")

# except Exception:
#     st.error(
#         "Unable to read this PDF. "
#         "Please upload a valid PDF file."
#     )
#     st.stop()


# # -----------------------------
# # SPLIT DOCUMENTS
# # -----------------------------

# try:
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = text_splitter.split_documents(documents)

#     if not chunks:
#         st.error("No readable text found in this PDF.")
#         st.stop()

# except Exception:
#     st.error("Error while splitting the PDF.")
#     st.stop()


# # -----------------------------
# # EMBEDDINGS
# # -----------------------------

# try:
#     with st.spinner("Creating embeddings..."):

#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )

# except Exception:
#     st.error("Error while loading the embedding model.")
#     st.stop()


# # -----------------------------
# # VECTOR DATABASE
# # -----------------------------

# try:
#     with st.spinner("Creating vector database..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
#         )

# except Exception:
#     st.error("Error while creating the vector database.")
#     st.stop()


# # -----------------------------
# # RETRIEVER WITH MMR
# # -----------------------------

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # -----------------------------
# # LLM
# # -----------------------------

# try:
#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )

# except Exception:
#     st.error("Error while connecting to the AI model.")
#     st.stop()


# # -----------------------------
# # RELEVANCE CHECK
# # -----------------------------

# relevance_prompt = PromptTemplate.from_template(
#     """
# You are a document relevance checker.

# Question:
# {question}

# Document:
# {document}

# Check whether the document contains information
# that can help answer the question.

# Return ONLY one of these:
# RELEVANT
# NOT_RELEVANT
# """
# )

# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# def filter_relevant_documents(question, documents):

#     relevant_documents = []

#     for document in documents:

#         try:
#             result = relevance_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip().upper()

#             if result == "RELEVANT":
#                 relevant_documents.append(document)

#         except Exception:
#             continue

#     return relevant_documents


# # -----------------------------
# # CONTEXT COMPRESSION
# # -----------------------------

# compression_prompt = PromptTemplate.from_template(
#     """
# You are an extractive document compressor.

# Question:
# {question}

# Document:
# {document}

# Instructions:
# - Extract only exact sentences relevant to the question.
# - Do not paraphrase.
# - Do not add new information.
# - If no relevant information exists, return EMPTY.
# - Return only the extracted text.
# """
# )

# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_documents(question, documents):

#     compressed_documents = []

#     for document in documents:

#         try:
#             compressed_text = compression_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip()

#             if (
#                 compressed_text
#                 and compressed_text.upper() != "EMPTY"
#             ):

#                 compressed_documents.append(
#                     Document(
#                         page_content=compressed_text,
#                         metadata=document.metadata
#                     )
#                 )

#         except Exception:
#             continue

#     return compressed_documents


# # -----------------------------
# # FINAL RAG PROMPT
# # -----------------------------

# rag_prompt = PromptTemplate.from_template(
#     """
# You are a helpful PDF question-answering assistant.

# Answer the question using ONLY the provided context.

# Conversation History:
# {history}

# Context:
# {context}

# Question:
# {question}

# Rules:
# - Use only the given context.
# - Do not invent information.
# - Keep the answer concise and clear.
# - If the answer is not present in the context,
#   respond exactly:
#   Information not available in the uploaded document.
# """
# )

# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # -----------------------------
# # CHAT HISTORY DISPLAY
# # -----------------------------

# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # -----------------------------
# # USER QUESTION
# # -----------------------------

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

#     # Save user message
#     st.session_state.chat_history.append({
#         "role": "user",
#         "content": question
#     })

#     # -----------------------------
#     # RETRIEVAL
#     # -----------------------------

#     try:

#         with st.spinner("Searching document..."):

#             retrieved_documents = retriever.invoke(question)

#     except Exception:

#         st.error("Error while searching the document.")
#         st.stop()


#     # -----------------------------
#     # REMOVE DUPLICATES
#     # -----------------------------

#     unique_documents = []
#     seen_text = set()

#     for document in retrieved_documents:

#         text = document.page_content.strip()

#         if text not in seen_text:

#             seen_text.add(text)
#             unique_documents.append(document)


#     # -----------------------------
#     # RELEVANCE FILTERING
#     # -----------------------------

#     with st.spinner("Checking relevant information..."):

#         relevant_documents = filter_relevant_documents(
#             question,
#             unique_documents
#         )


#     # -----------------------------
#     # CONTEXT COMPRESSION
#     # -----------------------------

#     with st.spinner("Preparing relevant context..."):

#         compressed_documents = compress_documents(
#             question,
#             relevant_documents
#         )


#     # -----------------------------
#     # CHAT HISTORY FORMAT
#     # -----------------------------

#     history = "\n".join(
#         f'{message["role"]}: {message["content"]}'
#         for message in st.session_state.chat_history[-6:]
#     )


#     # -----------------------------
#     # FINAL ANSWER
#     # -----------------------------

#     if not compressed_documents:

#         answer = (
#             "Information not available in the "
#             "uploaded document."
#         )

#     else:

#         context = "\n\n".join(
#             document.page_content
#             for document in compressed_documents
#         )

#         try:

#             with st.spinner("Generating answer..."):

#                 answer = rag_chain.invoke({
#                     "context": context,
#                     "question": question,
#                     "history": history
#                 }).strip()

#         except Exception:

#             answer = (
#                 "Sorry, I could not generate an answer. "
#                 "Please try again."
#             )

#             st.error(
#                 "There was a problem connecting "
#                 "to the AI model."
#             )


#     # -----------------------------
#     # DISPLAY ANSWER
#     # -----------------------------

#     with st.chat_message("assistant"):

#         st.markdown(answer)


#     # Save assistant message
#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })


#     # -----------------------------
#     # DISPLAY SOURCES
#     # -----------------------------

#     unavailable_message = (
#         "Information not available in the "
#         "uploaded document."
#     )

#     if (
#         compressed_documents
#         and answer != unavailable_message
#         and not answer.startswith("Sorry")
#     ):

#         with st.expander("📚 Sources"):

#             shown_pages = set()

#             for document in compressed_documents:

#                 page_number = document.metadata.get(
#                     "page",
#                     document.metadata.get("page_label", "Unknown")
#                 )

#                 if page_number not in shown_pages:

#                     shown_pages.add(page_number)

#                     st.write(
#                         f"**Page:** {int(page_number) + 1}"
#                         if isinstance(page_number, int)
#                         else f"**Page:** {page_number}"
#                     )

#                     st.write(document.page_content)
#                     st.divider()



#                   < Caching >         # 

# import streamlit as st
# import tempfile
# import uuid
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


# # =============================
# # CONFIGURATION
# # =============================

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG Chatbot")

# project_folder = Path(__file__).resolve().parent
# load_dotenv(project_folder / ".env")


# # =============================
# # SESSION STATE
# # =============================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if st.button("🗑️ Clear Chat History"):
#     st.session_state.chat_history = []
#     st.rerun()


# # =============================
# # CACHED EMBEDDINGS
# # =============================

# @st.cache_resource
# def get_embeddings():

#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


# # =============================
# # PDF UPLOAD
# # =============================

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )

# if uploaded_file is None:
#     st.info("Please upload a PDF to start chatting.")
#     st.stop()


# # =============================
# # SAVE PDF TEMPORARILY
# # =============================

# pdf_bytes = uploaded_file.getvalue()

# try:

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=".pdf"
#     ) as temp_file:

#         temp_file.write(pdf_bytes)
#         pdf_path = temp_file.name

# except Exception:

#     st.error("Unable to save the uploaded PDF.")
#     st.stop()


# # =============================
# # LOAD PDF
# # =============================

# try:

#     with st.spinner("Loading PDF..."):

#         loader = PyPDFLoader(pdf_path)
#         documents = loader.load()

#     st.success("PDF loaded successfully!")

# except Exception:

#     st.error(
#         "Unable to read this PDF. "
#         "Please upload a valid PDF."
#     )

#     st.stop()


# # =============================
# # SPLIT DOCUMENTS
# # =============================

# try:

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = text_splitter.split_documents(documents)

#     if not chunks:
#         st.error("No readable text found in this PDF.")
#         st.stop()

# except Exception:

#     st.error("Error while splitting the PDF.")
#     st.stop()


# # =============================
# # EMBEDDINGS WITH CACHE
# # =============================

# try:

#     with st.spinner("Loading embeddings..."):

#         embeddings = get_embeddings()

# except Exception:

#     st.error("Error while loading embedding model.")
#     st.stop()


# # =============================
# # VECTOR DATABASE
# # =============================

# try:

#     with st.spinner("Creating vector database..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
#         )

# except Exception:

#     st.error("Error while creating vector database.")
#     st.stop()


# # =============================
# # MMR RETRIEVER
# # =============================

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # =============================
# # LLM
# # =============================

# try:

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )

# except Exception:

#     st.error("Error while connecting to AI model.")
#     st.stop()


# # =============================
# # RELEVANCE CHECK
# # =============================

# relevance_prompt = PromptTemplate.from_template(
#     """
# You are a document relevance checker.

# Question:
# {question}

# Document:
# {document}

# Does this document contain information
# that can help answer the question?

# Return ONLY:
# RELEVANT
# or
# NOT_RELEVANT
# """
# )

# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# def filter_relevant_documents(question, documents):

#     relevant_documents = []

#     for document in documents:

#         try:

#             result = relevance_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip().upper()

#             if result == "RELEVANT":
#                 relevant_documents.append(document)

#         except Exception:

#             continue

#     return relevant_documents


# # =============================
# # CONTEXT COMPRESSION
# # =============================

# compression_prompt = PromptTemplate.from_template(
#     """
# You are an extractive document compressor.

# Question:
# {question}

# Document:
# {document}

# Instructions:
# - Extract only exact relevant sentences.
# - Do not paraphrase.
# - Do not add new information.
# - If no relevant information exists, return EMPTY.
# - Return only extracted text.
# """
# )

# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_documents(question, documents):

#     compressed_documents = []

#     for document in documents:

#         try:

#             compressed_text = compression_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip()

#             if (
#                 compressed_text
#                 and compressed_text.upper() != "EMPTY"
#             ):

#                 compressed_documents.append(
#                     Document(
#                         page_content=compressed_text,
#                         metadata=document.metadata
#                     )
#                 )

#         except Exception:

#             continue

#     return compressed_documents


# # =============================
# # FINAL RAG PROMPT
# # =============================

# rag_prompt = PromptTemplate.from_template(
#     """
# You are a helpful PDF question-answering assistant.

# Answer using ONLY the provided context.

# Conversation History:
# {history}

# Context:
# {context}

# Question:
# {question}

# Rules:
# - Use only the given context.
# - Do not invent information.
# - Keep the answer concise.
# - If the answer is unavailable, respond exactly:

# Information not available in the uploaded document.
# """
# )

# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # =============================
# # DISPLAY CHAT HISTORY
# # =============================

# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # =============================
# # USER QUESTION
# # =============================

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


#     # =============================
#     # RETRIEVAL
#     # =============================

#     try:

#         with st.spinner("Searching document..."):

#             retrieved_documents = retriever.invoke(question)

#     except Exception:

#         st.error("Error while searching document.")
#         st.stop()


#     # =============================
#     # REMOVE DUPLICATES
#     # =============================

#     unique_documents = []
#     seen_text = set()

#     for document in retrieved_documents:

#         text = document.page_content.strip()

#         if text not in seen_text:

#             seen_text.add(text)
#             unique_documents.append(document)


#     # =============================
#     # RELEVANCE FILTERING
#     # =============================

#     with st.spinner("Checking relevant information..."):

#         relevant_documents = filter_relevant_documents(
#             question,
#             unique_documents
#         )


#     # =============================
#     # COMPRESSION
#     # =============================

#     with st.spinner("Preparing relevant context..."):

#         compressed_documents = compress_documents(
#             question,
#             relevant_documents
#         )


#     # =============================
#     # CHAT HISTORY
#     # =============================

#     history = "\n".join(
#         f'{message["role"]}: {message["content"]}'
#         for message in st.session_state.chat_history[-6:]
#     )


#     # =============================
#     # FINAL ANSWER
#     # =============================

#     unavailable_message = (
#         "Information not available in the "
#         "uploaded document."
#     )

#     if not compressed_documents:

#         answer = unavailable_message

#     else:

#         context = "\n\n".join(
#             document.page_content
#             for document in compressed_documents
#         )

#         try:

#             with st.spinner("Generating answer..."):

#                 answer = rag_chain.invoke({
#                     "context": context,
#                     "question": question,
#                     "history": history
#                 }).strip()

#         except Exception:

#             answer = (
#                 "Sorry, I could not generate an answer. "
#                 "Please try again."
#             )

#             st.error(
#                 "There was a problem connecting "
#                 "to the AI model."
#             )


#     # =============================
#     # DISPLAY ANSWER
#     # =============================

#     with st.chat_message("assistant"):

#         st.markdown(answer)

#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })


#     # =============================
#     # SOURCES
#     # =============================

#     if (
#         compressed_documents
#         and answer != unavailable_message
#         and not answer.startswith("Sorry")
#     ):

#         with st.expander("📚 Sources"):

#             shown_pages = set()

#             for document in compressed_documents:

#                 page_number = document.metadata.get(
#                     "page",
#                     document.metadata.get(
#                         "page_label",
#                         "Unknown"
#                     )
#                 )

#                 if page_number not in shown_pages:

#                     shown_pages.add(page_number)

#                     if isinstance(page_number, int):

#                         st.write(
#                             f"**Page:** {page_number + 1}"
#                         )

#                     else:

#                         st.write(
#                             f"**Page:** {page_number}"
#                         )

#                     st.write(document.page_content)
#                     st.divider()


#                   < PDF Loading + Chunking ko st.cache_data se cache karenge.>


# import streamlit as st
# import tempfile
# import uuid
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


# # =============================
# # CONFIGURATION
# # =============================

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG Chatbot")

# project_folder = Path(__file__).resolve().parent
# load_dotenv(project_folder / ".env")


# # =============================
# # SESSION STATE
# # =============================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# if st.button("🗑️ Clear Chat History"):

#     st.session_state.chat_history = []
#     st.rerun()


# # =============================
# # CACHED PDF LOADING + CHUNKING
# # =============================

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

#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=500,
#             chunk_overlap=50
#         )

#         chunks = text_splitter.split_documents(documents)

#         return chunks

#     finally:

#         Path(pdf_path).unlink(missing_ok=True)


# # =============================
# # CACHED EMBEDDING MODEL
# # =============================

# @st.cache_resource
# def get_embeddings():

#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


# # =============================
# # PDF UPLOAD
# # =============================

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is None:

#     st.info("Please upload a PDF to start chatting.")
#     st.stop()


# # =============================
# # PDF PROCESSING
# # =============================

# pdf_bytes = uploaded_file.getvalue()

# try:

#     with st.spinner("Loading and splitting PDF..."):

#         chunks = load_and_split_pdf(pdf_bytes)

#     if not chunks:

#         st.error("No readable text found in this PDF.")
#         st.stop()

#     st.success(
#         f"PDF processed successfully! "
#         f"Total chunks: {len(chunks)}"
#     )

# except Exception:

#     st.error(
#         "Unable to process this PDF. "
#         "Please upload a valid PDF."
#     )

#     st.stop()


# # =============================
# # EMBEDDINGS
# # =============================

# try:

#     with st.spinner("Loading embedding model..."):

#         embeddings = get_embeddings()

# except Exception:

#     st.error("Error while loading embedding model.")
#     st.stop()


# # =============================
# # VECTOR DATABASE
# # =============================

# try:

#     with st.spinner("Creating vector database..."):

#         vector_store = Chroma.from_documents(
#             documents=chunks,
#             embedding=embeddings,
#             collection_name=f"pdf_rag_{uuid.uuid4().hex}"
#         )

# except Exception:

#     st.error("Error while creating vector database.")
#     st.stop()


# # =============================
# # RETRIEVER
# # =============================

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # =============================
# # LLM
# # =============================

# try:

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )

# except Exception:

#     st.error("Error while connecting to AI model.")
#     st.stop()


# # =============================
# # RELEVANCE CHECK
# # =============================

# relevance_prompt = PromptTemplate.from_template(
#     """
# You are a document relevance checker.

# Question:
# {question}

# Document:
# {document}

# Check whether the document contains information
# that can help answer the question.

# Return ONLY:
# RELEVANT
# or
# NOT_RELEVANT
# """
# )


# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# def filter_relevant_documents(question, documents):

#     relevant_documents = []

#     for document in documents:

#         try:

#             result = relevance_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip().upper()

#             if result == "RELEVANT":

#                 relevant_documents.append(document)

#         except Exception:

#             continue

#     return relevant_documents


# # =============================
# # CONTEXT COMPRESSION
# # =============================

# compression_prompt = PromptTemplate.from_template(
#     """
# You are an extractive document compressor.

# Question:
# {question}

# Document:
# {document}

# Instructions:
# - Extract only exact sentences relevant to the question.
# - Do not paraphrase.
# - Do not add new information.
# - If no relevant information exists, return EMPTY.
# - Return only the extracted text.
# """
# )


# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_documents(question, documents):

#     compressed_documents = []

#     for document in documents:

#         try:

#             compressed_text = compression_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip()

#             if (
#                 compressed_text
#                 and compressed_text.upper() != "EMPTY"
#             ):

#                 compressed_documents.append(
#                     Document(
#                         page_content=compressed_text,
#                         metadata=document.metadata
#                     )
#                 )

#         except Exception:

#             continue

#     return compressed_documents


# # =============================
# # FINAL RAG CHAIN
# # =============================

# rag_prompt = PromptTemplate.from_template(
#     """
# You are a helpful PDF question-answering assistant.

# Answer using ONLY the provided context.

# Conversation History:
# {history}

# Context:
# {context}

# Question:
# {question}

# Rules:
# - Use only the given context.
# - Do not invent information.
# - Keep the answer concise and clear.
# - If the answer is unavailable, respond exactly:

# Information not available in the uploaded document.
# """
# )


# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # =============================
# # DISPLAY CHAT HISTORY
# # =============================

# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):

#         st.markdown(message["content"])


# # =============================
# # USER QUESTION
# # =============================

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


#     # =============================
#     # RETRIEVAL
#     # =============================

#     try:

#         with st.spinner("Searching document..."):

#             retrieved_documents = retriever.invoke(question)

#     except Exception:

#         st.error("Error while searching document.")
#         st.stop()


#     # =============================
#     # REMOVE DUPLICATES
#     # =============================

#     unique_documents = []
#     seen_text = set()

#     for document in retrieved_documents:

#         text = document.page_content.strip()

#         if text not in seen_text:

#             seen_text.add(text)
#             unique_documents.append(document)


#     # =============================
#     # RELEVANCE FILTERING
#     # =============================

#     with st.spinner("Checking relevant information..."):

#         relevant_documents = filter_relevant_documents(
#             question,
#             unique_documents
#         )


#     # =============================
#     # COMPRESSION
#     # =============================

#     with st.spinner("Preparing relevant context..."):

#         compressed_documents = compress_documents(
#             question,
#             relevant_documents
#         )


#     # =============================
#     # CHAT HISTORY
#     # =============================

#     history = "\n".join(
#         f'{message["role"]}: {message["content"]}'
#         for message in st.session_state.chat_history[-6:]
#     )


#     # =============================
#     # FINAL ANSWER
#     # =============================

#     unavailable_message = (
#         "Information not available in the "
#         "uploaded document."
#     )


#     if not compressed_documents:

#         answer = unavailable_message

#     else:

#         context = "\n\n".join(
#             document.page_content
#             for document in compressed_documents
#         )

#         try:

#             with st.spinner("Generating answer..."):

#                 answer = rag_chain.invoke({
#                     "context": context,
#                     "question": question,
#                     "history": history
#                 }).strip()

#         except Exception:

#             answer = (
#                 "Sorry, I could not generate an answer. "
#                 "Please try again."
#             )

#             st.error(
#                 "There was a problem connecting "
#                 "to the AI model."
#             )


#     # =============================
#     # DISPLAY ANSWER
#     # =============================

#     with st.chat_message("assistant"):

#         st.markdown(answer)


#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })


#     # =============================
#     # SOURCES
#     # =============================

#     if (
#         compressed_documents
#         and answer != unavailable_message
#         and not answer.startswith("Sorry")
#     ):

#         with st.expander("📚 Sources"):

#             shown_pages = set()

#             for document in compressed_documents:

#                 page_number = document.metadata.get(
#                     "page",
#                     document.metadata.get(
#                         "page_label",
#                         "Unknown"
#                     )
#                 )

#                 if page_number not in shown_pages:

#                     shown_pages.add(page_number)

#                     if isinstance(page_number, int):

#                         st.write(
#                             f"**Page:** {page_number + 1}"
#                         )

#                     else:

#                         st.write(
#                             f"**Page:** {page_number}"
#                         )

#                     st.write(document.page_content)
#                     st.divider()



#.              < final after all catch >         #




# import streamlit as st
# import tempfile
# import uuid
# import hashlib
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


# # =============================
# # CONFIGURATION
# # =============================

# st.set_page_config(
#     page_title="PDF RAG Chatbot",
#     page_icon="📄"
# )

# st.title("📄 PDF RAG Chatbot")

# project_folder = Path(__file__).resolve().parent
# load_dotenv(project_folder / ".env")


# # =============================
# # SESSION STATE
# # =============================

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# if "pdf_hash" not in st.session_state:
#     st.session_state.pdf_hash = None


# if "vector_store" not in st.session_state:
#     st.session_state.vector_store = None


# if st.button("🗑️ Clear Chat History"):

#     st.session_state.chat_history = []
#     st.rerun()


# # =============================
# # CACHED PDF LOADING + CHUNKING
# # =============================

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

#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=500,
#             chunk_overlap=50
#         )

#         chunks = text_splitter.split_documents(documents)

#         return chunks

#     finally:

#         Path(pdf_path).unlink(missing_ok=True)


# # =============================
# # CACHED EMBEDDING MODEL
# # =============================

# @st.cache_resource
# def get_embeddings():

#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )


# # =============================
# # PDF UPLOAD
# # =============================

# uploaded_file = st.file_uploader(
#     "Upload your PDF",
#     type=["pdf"]
# )


# if uploaded_file is None:

#     st.info("Please upload a PDF to start chatting.")
#     st.stop()


# # =============================
# # PDF PROCESSING
# # =============================

# pdf_bytes = uploaded_file.getvalue()

# pdf_hash = hashlib.md5(pdf_bytes).hexdigest()


# try:

#     with st.spinner("Loading and splitting PDF..."):

#         chunks = load_and_split_pdf(pdf_bytes)

#     if not chunks:

#         st.error("No readable text found in this PDF.")
#         st.stop()

#     st.success(
#         f"PDF processed successfully! "
#         f"Total chunks: {len(chunks)}"
#     )

# except Exception:

#     st.error(
#         "Unable to process this PDF. "
#         "Please upload a valid PDF."
#     )

#     st.stop()


# # =============================
# # EMBEDDINGS
# # =============================

# try:

#     with st.spinner("Loading embedding model..."):

#         embeddings = get_embeddings()

# except Exception:

#     st.error("Error while loading embedding model.")
#     st.stop()


# # =============================
# # VECTOR DATABASE REUSE
# # =============================

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

#         st.success(
#             "Vector database created successfully!"
#         )

#     except Exception:

#         st.error(
#             "Error while creating vector database."
#         )

#         st.stop()

# else:

#     vector_store = st.session_state.vector_store

#     st.info("Using cached vector database.")


# # =============================
# # MMR RETRIEVER
# # =============================

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 5,
#         "fetch_k": 15,
#         "lambda_mult": 0.7
#     }
# )


# # =============================
# # LLM
# # =============================

# try:

#     llm = ChatGroq(
#         model="openai/gpt-oss-20b",
#         temperature=0
#     )

# except Exception:

#     st.error("Error while connecting to AI model.")
#     st.stop()


# # =============================
# # RELEVANCE CHECK
# # =============================

# relevance_prompt = PromptTemplate.from_template(
#     """
# You are a document relevance checker.

# Question:
# {question}

# Document:
# {document}

# Check whether the document contains information
# that can help answer the question.

# Return ONLY:
# RELEVANT
# or
# NOT_RELEVANT
# """
# )


# relevance_chain = (
#     relevance_prompt
#     | llm
#     | StrOutputParser()
# )


# def filter_relevant_documents(question, documents):

#     relevant_documents = []

#     for document in documents:

#         try:

#             result = relevance_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip().upper()

#             if result == "RELEVANT":

#                 relevant_documents.append(document)

#         except Exception:

#             continue

#     return relevant_documents


# # =============================
# # CONTEXT COMPRESSION
# # =============================

# compression_prompt = PromptTemplate.from_template(
#     """
# You are an extractive document compressor.

# Question:
# {question}

# Document:
# {document}

# Instructions:
# - Extract only exact sentences relevant to the question.
# - Do not paraphrase.
# - Do not add new information.
# - If no relevant information exists, return EMPTY.
# - Return only the extracted text.
# """
# )


# compression_chain = (
#     compression_prompt
#     | llm
#     | StrOutputParser()
# )


# def compress_documents(question, documents):

#     compressed_documents = []

#     for document in documents:

#         try:

#             compressed_text = compression_chain.invoke({
#                 "question": question,
#                 "document": document.page_content
#             }).strip()

#             if (
#                 compressed_text
#                 and compressed_text.upper() != "EMPTY"
#             ):

#                 compressed_documents.append(
#                     Document(
#                         page_content=compressed_text,
#                         metadata=document.metadata
#                     )
#                 )

#         except Exception:

#             continue

#     return compressed_documents


# # =============================
# # FINAL RAG CHAIN
# # =============================

# rag_prompt = PromptTemplate.from_template(
#     """
# You are a helpful PDF question-answering assistant.

# Answer using ONLY the provided context.

# Conversation History:
# {history}

# Context:
# {context}

# Question:
# {question}

# Rules:
# - Use only the given context.
# - Do not invent information.
# - Keep the answer concise and clear.
# - If the answer is unavailable, respond exactly:

# Information not available in the uploaded document.
# """
# )


# rag_chain = (
#     rag_prompt
#     | llm
#     | StrOutputParser()
# )


# # =============================
# # DISPLAY CHAT HISTORY
# # =============================

# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):

#         st.markdown(message["content"])


# # =============================
# # USER QUESTION
# # =============================

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


#     # =============================
#     # RETRIEVAL
#     # =============================

#     try:

#         with st.spinner("Searching document..."):

#             retrieved_documents = retriever.invoke(question)

#     except Exception:

#         st.error("Error while searching document.")
#         st.stop()


#     # =============================
#     # REMOVE DUPLICATES
#     # =============================

#     unique_documents = []
#     seen_text = set()

#     for document in retrieved_documents:

#         text = document.page_content.strip()

#         if text not in seen_text:

#             seen_text.add(text)
#             unique_documents.append(document)


#     # =============================
#     # RELEVANCE FILTERING
#     # =============================

#     with st.spinner("Checking relevant information..."):

#         relevant_documents = filter_relevant_documents(
#             question,
#             unique_documents
#         )


#     # =============================
#     # CONTEXT COMPRESSION
#     # =============================

#     with st.spinner("Preparing relevant context..."):

#         compressed_documents = compress_documents(
#             question,
#             relevant_documents
#         )


#     # =============================
#     # CHAT HISTORY
#     # =============================

#     history = "\n".join(
#         f'{message["role"]}: {message["content"]}'
#         for message in st.session_state.chat_history[-6:]
#     )


#     # =============================
#     # FINAL ANSWER
#     # =============================

#     unavailable_message = (
#         "Information not available in the "
#         "uploaded document."
#     )


#     if not compressed_documents:

#         answer = unavailable_message

#     else:

#         context = "\n\n".join(
#             document.page_content
#             for document in compressed_documents
#         )

#         try:

#             with st.spinner("Generating answer..."):

#                 answer = rag_chain.invoke({
#                     "context": context,
#                     "question": question,
#                     "history": history
#                 }).strip()

#         except Exception:

#             answer = (
#                 "Sorry, I could not generate an answer. "
#                 "Please try again."
#             )

#             st.error(
#                 "There was a problem connecting "
#                 "to the AI model."
#             )


#     # =============================
#     # DISPLAY ANSWER
#     # =============================

#     with st.chat_message("assistant"):

#         st.markdown(answer)


#     st.session_state.chat_history.append({
#         "role": "assistant",
#         "content": answer
#     })


#     # =============================
#     # SOURCES
#     # =============================

#     if (
#         compressed_documents
#         and answer != unavailable_message
#         and not answer.startswith("Sorry")
#     ):

#         with st.expander("📚 Sources"):

#             shown_pages = set()

#             for document in compressed_documents:

#                 page_number = document.metadata.get(
#                     "page",
#                     document.metadata.get(
#                         "page_label",
#                         "Unknown"
#                     )
#                 )

#                 if page_number not in shown_pages:

#                     shown_pages.add(page_number)

#                     if isinstance(page_number, int):

#                         st.write(
#                             f"**Page:** {page_number + 1}"
#                         )

#                     else:

#                         st.write(
#                             f"**Page:** {page_number}"
#                         )

#                     st.write(document.page_content)
#                     st.divider()

#           < iam working here for two thing first for wide or fit to screen display and 
 #          second for giving info from trained knowledge >



import streamlit as st
import tempfile
import hashlib
import uuid
import os

from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. LOAD ENVIRONMENT VARIABLES
# =========================================================

project_folder = Path(__file__).resolve().parent

load_dotenv(project_folder / ".env")


# =========================================================
# 3. API KEY CONFIGURATION
# =========================================================

groq_api_key = st.secrets.get(
    "GROQ_API_KEY",
    os.getenv("GROQ_API_KEY")
)

if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please configure your API key.")
    st.stop()


# =========================================================
# 4. SESSION STATE
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pdf_hash" not in st.session_state:
    st.session_state.pdf_hash = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


# =========================================================
# 5. SIDEBAR SETTINGS
# =========================================================

st.sidebar.title("⚙️ Settings")


screen_mode = st.sidebar.radio(
    "🖥️ Screen Layout",
    ["Wide Screen", "Fit to Screen"],
    index=0
)


temperature = st.sidebar.slider(
    "🌡️ Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.0,
    step=0.1
)


allow_general_knowledge = st.sidebar.checkbox(
    "🧠 Allow General Knowledge Fallback",
    value=True
)


if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()


# =========================================================
# 6. CUSTOM SCREEN LAYOUT
# =========================================================

if screen_mode == "Fit to Screen":

    st.markdown(
        """
        <style>
        .stMainBlockContainer {
            max-width: 900px;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <style>
        .stMainBlockContainer {
            max-width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 7. PAGE TITLE
# =========================================================

st.title("📄 PDF RAG Chatbot")

st.write(
    "Upload a PDF and ask questions from the document. "
    "If enabled, general knowledge fallback will be used "
    "when relevant PDF information is not found."
)


# =========================================================
# 8. CACHED PDF LOADING AND CHUNKING
# =========================================================

@st.cache_data
def load_and_split_pdf(pdf_bytes):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(pdf_bytes)
        pdf_path = temp_file.name

    try:

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documents)

        return chunks

    finally:

        Path(pdf_path).unlink(missing_ok=True)


# =========================================================
# 9. CACHED EMBEDDING MODEL
# =========================================================

@st.cache_resource
def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# =========================================================
# 10. PDF UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📤 Upload your PDF",
    type=["pdf"]
)


if uploaded_file is None:

    st.info("Please upload a PDF to start asking questions.")

    st.stop()


pdf_bytes = uploaded_file.getvalue()

pdf_hash = hashlib.md5(pdf_bytes).hexdigest()


# =========================================================
# 11. LOAD AND SPLIT PDF
# =========================================================

try:

    with st.spinner("Loading and splitting PDF..."):

        chunks = load_and_split_pdf(pdf_bytes)

    st.success(
        f"PDF processed successfully! Total chunks: {len(chunks)}"
    )

except Exception:

    st.error(
        "Unable to read this PDF. Please upload a valid PDF file."
    )

    st.stop()


# =========================================================
# 12. EMBEDDINGS
# =========================================================

try:

    with st.spinner("Loading embedding model..."):

        embeddings = get_embeddings()

except Exception:

    st.error(
        "Unable to load the embedding model."
    )

    st.stop()


# =========================================================
# 13. VECTOR STORE CREATION AND REUSE
# =========================================================

if (
    st.session_state.pdf_hash != pdf_hash
    or st.session_state.vector_store is None
):

    try:

        with st.spinner("Creating vector database..."):

            vector_store = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                collection_name=f"pdf_rag_{uuid.uuid4().hex}"
            )

        st.session_state.vector_store = vector_store

        st.session_state.pdf_hash = pdf_hash

        # Clear old chat when a new PDF is uploaded
        st.session_state.chat_history = []

    except Exception:

        st.error(
            "Unable to create the vector database."
        )

        st.stop()

else:

    vector_store = st.session_state.vector_store


# =========================================================
# 14. RETRIEVER
# =========================================================

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 15,
        "lambda_mult": 0.7
    }
)


# =========================================================
# 15. LLM
# =========================================================

try:

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=temperature,
        api_key=groq_api_key
    )

except Exception:

    st.error(
        "Unable to connect to the Groq model."
    )

    st.stop()


# =========================================================
# 16. RELEVANCE GRADING PROMPT
# =========================================================

relevance_prompt = PromptTemplate.from_template(
    """
    You are a document relevance grader.

    Decide whether the context contains useful information
    to answer the question.

    Return ONLY one of these exact words:

    RELEVANT
    NOT_RELEVANT

    Question:
    {question}

    Context:
    {context}
    """
)


relevance_chain = (
    relevance_prompt
    | llm
    | StrOutputParser()
)


def is_relevant(question, document):

    try:

        result = relevance_chain.invoke(
            {
                "question": question,
                "context": document.page_content
            }
        ).strip().upper()

        return result == "RELEVANT"

    except Exception:

        return False


# =========================================================
# 17. CONTEXT COMPRESSION PROMPT
# =========================================================

compression_prompt = PromptTemplate.from_template(
    """
    You are a context extraction assistant.

    Extract ONLY the information from the context
    that is directly useful for answering the question.

    Rules:
    - Do not add outside knowledge.
    - Do not invent facts.
    - If useful information is not present, return an empty response.
    - Keep important facts, numbers, and names.
    - Keep the answer concise.

    Question:
    {question}

    Context:
    {context}
    """
)


compression_chain = (
    compression_prompt
    | llm
    | StrOutputParser()
)


def compress_document(question, document):

    try:

        compressed_text = compression_chain.invoke(
            {
                "question": question,
                "context": document.page_content
            }
        ).strip()

        if not compressed_text:
            return None

        return Document(
            page_content=compressed_text,
            metadata=document.metadata
        )

    except Exception:

        return None


# =========================================================
# 18. PDF RAG PROMPT
# =========================================================

rag_prompt = PromptTemplate.from_template(
    """
    You are a helpful PDF question-answering assistant.

    Answer the question using ONLY the provided PDF context.

    Rules:
    - Do not use outside knowledge.
    - Do not invent information.
    - Give a clear and concise answer.
    - If the context does not contain the answer,
      respond exactly:
      Information not available in the provided document.

    Conversation History:
    {chat_history}

    PDF Context:
    {context}

    Question:
    {question}

    Answer:
    """
)


rag_chain = (
    rag_prompt
    | llm
    | StrOutputParser()
)


# =========================================================
# 19. GENERAL KNOWLEDGE PROMPT
# =========================================================

general_prompt = PromptTemplate.from_template(
    """
    You are a helpful AI assistant.

    Answer the user's question using your general
    pretrained knowledge.

    Rules:
    - Do not claim that the answer comes from the PDF.
    - Do not invent facts.
    - If you are uncertain, clearly mention the uncertainty.
    - Give a clear and concise answer.

    Question:
    {question}

    Answer:
    """
)


general_chain = (
    general_prompt
    | llm
    | StrOutputParser()
)


# =========================================================
# 20. DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if "source" in message:

                st.caption(message["source"])


# =========================================================
# 21. USER QUESTION
# =========================================================

user_question = st.chat_input(
    "Ask a question about your PDF..."
)


if user_question:

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_question)

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # =====================================================
    # 22. RETRIEVE DOCUMENTS
    # =====================================================

    try:

        with st.spinner("Searching the PDF..."):

            retrieved_docs = retriever.invoke(
                user_question
            )

    except Exception:

        retrieved_docs = []

        st.warning(
            "Unable to retrieve relevant PDF context."
        )


    # =====================================================
    # 23. REMOVE DUPLICATE DOCUMENTS
    # =====================================================

    unique_docs = []

    seen_content = set()

    for doc in retrieved_docs:

        content = doc.page_content.strip()

        if content not in seen_content:

            seen_content.add(content)

            unique_docs.append(doc)


    # =====================================================
    # 24. RELEVANCE FILTERING
    # =====================================================

    relevant_docs = []

    with st.spinner("Checking document relevance..."):

        for doc in unique_docs:

            if is_relevant(user_question, doc):

                relevant_docs.append(doc)


    # =====================================================
    # 25. CONTEXT COMPRESSION
    # =====================================================

    compressed_docs = []

    if relevant_docs:

        with st.spinner("Preparing relevant context..."):

            for doc in relevant_docs:

                compressed_doc = compress_document(
                    user_question,
                    doc
                )

                if compressed_doc:

                    compressed_docs.append(compressed_doc)


    # =====================================================
    # 26. CHAT HISTORY TEXT
    # =====================================================

    history_text = ""

    for message in st.session_state.chat_history[-6:]:

        history_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )


    # =====================================================
    # 27. ANSWER GENERATION
    # =====================================================

    answer = ""

    answer_source = ""

    source_documents = []


    try:

        with st.spinner("Generating answer..."):

            if compressed_docs:

                context = "\n\n".join(
                    doc.page_content
                    for doc in compressed_docs
                )

                answer = rag_chain.invoke(
                    {
                        "context": context,
                        "question": user_question,
                        "chat_history": history_text
                    }
                ).strip()

                # If the strict PDF chain cannot answer,
                # optionally use general knowledge fallback.
                unavailable_text = (
                    "information not available"
                )

                if (
                    allow_general_knowledge
                    and unavailable_text in answer.lower()
                ):

                    answer = general_chain.invoke(
                        {
                            "question": user_question
                        }
                    ).strip()

                    answer_source = (
                        "🧠 Source: General Knowledge (LLM)"
                    )

                else:

                    answer_source = (
                        "📄 Source: Uploaded PDF"
                    )

                    source_documents = compressed_docs

            else:

                if allow_general_knowledge:

                    answer = general_chain.invoke(
                        {
                            "question": user_question
                        }
                    ).strip()

                    answer_source = (
                        "🧠 Source: General Knowledge (LLM)"
                    )

                else:

                    answer = (
                        "Information not available "
                        "in the provided document."
                    )

                    answer_source = (
                        "📄 Source: Uploaded PDF"
                    )


    except Exception:

        answer = (
            "Sorry, I could not generate an answer. "
            "Please try again."
        )

        answer_source = (
            "⚠️ Answer generation failed"
        )

        st.error(
            "There was a problem connecting to the AI model."
        )


    # =====================================================
    # 28. DISPLAY ASSISTANT RESPONSE
    # =====================================================

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.caption(answer_source)


        # =================================================
        # 29. DISPLAY PDF SOURCES
        # =================================================

        if source_documents:

            st.markdown("#### 📚 PDF Sources")

            displayed_sources = set()

            for doc in source_documents:

                page_number = doc.metadata.get(
                    "page",
                    None
                )

                if page_number is not None:

                    page_number = int(page_number) + 1

                    source_label = (
                        f"Page {page_number}"
                    )

                else:

                    source_label = "Page number unavailable"


                if source_label not in displayed_sources:

                    displayed_sources.add(source_label)

                    st.write(f"📄 {source_label}")


    # =====================================================
    # 30. SAVE ASSISTANT MESSAGE
    # =====================================================

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer,
            "source": answer_source
        }
    )