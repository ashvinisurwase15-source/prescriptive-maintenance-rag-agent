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

query = "What should I do when machine temperature is high?"

results = vector_store.similarity_search(
    query=query,
    k=2
)

print("\nTop Matching Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 50)