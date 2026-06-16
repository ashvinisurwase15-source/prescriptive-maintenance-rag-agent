from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to existing ChromaDB collection
vector_store = Chroma(
    collection_name="maintenance_docs",
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

# User query
query = "What should be done if machine temperature exceeds 100 degrees?"

# Retrieve top 2 similar documents
results = vector_store.similarity_search(query, k=2)

print("\nQuery:")
print(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results, start=1):
    print(f"Document {i}:")
    print(doc.page_content)
    print("-" * 50)