from app.rag.hybrid_retriever import hybrid_search

print("Starting Hybrid Search...")

results = hybrid_search("machine vibration")

print("Hybrid Search Finished!")

print("\n===== RERANKED RESULTS =====\n")

for i, doc in enumerate(results, start=1):
    print(f"Rank {i}")
    print(doc.page_content)
    print("-" * 50)