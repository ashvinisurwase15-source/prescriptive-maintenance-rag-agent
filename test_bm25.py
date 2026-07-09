from app.rag.bm25_retriever import search_bm25

results = search_bm25("machine vibration")

print("\n===== BM25 RESULTS =====\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print(result.page_content)
    print("-" * 50)