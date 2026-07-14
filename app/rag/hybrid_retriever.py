from app.rag.bm25_retriever import search_bm25
from app.rag.retriever import search_documents
from app.rag.reranker import rerank_documents

def hybrid_search(query):
    bm25_results = search_bm25(query)

    chroma_results = search_documents(query)
    combined_results = bm25_results + chroma_results
    unique_results = []
    seen = set()
    for result in combined_results:
        content = result.page_content

        if content not in seen:
            seen.add(content)
            unique_results.append(result)

    reranked_results = rerank_documents(query, unique_results)

    return reranked_results[:5]

