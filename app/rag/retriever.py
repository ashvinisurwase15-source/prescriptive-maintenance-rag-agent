from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="maintenance_docs",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

def search_documents(query):
    results = vector_store.similarity_search(
        query=query,
        k=2
    )

    return results