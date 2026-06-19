from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.rag.loader import documents

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="maintenance_docs",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

vector_store.add_documents(documents)

print("Documents Added Successfully")