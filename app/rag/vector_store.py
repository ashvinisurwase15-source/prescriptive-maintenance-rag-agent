from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

documents = [
    "Machine temperature exceeds 100°C. Check cooling fan. Inspect airflow. Reduce machine load.",
    "If vibration is critical, inspect bearings and tighten loose components.",
    "Immediate maintenance required when machine temperature reaches 110°C."
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="maintenance_docs",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

vector_store.add_texts(documents)

print("Documents Added Successfully")