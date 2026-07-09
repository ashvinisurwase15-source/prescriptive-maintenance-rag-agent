from rank_bm25 import BM25Okapi

from app.rag.loader import load_documents
from app.rag.chunker import split_documents


def create_bm25_index():
    documents = load_documents()
    chunks = split_documents(documents)

    tokenized_chunks = [
        chunk.page_content.lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)

    return bm25, chunks


def search_bm25(query, top_k: int = 3):
    bm25, chunks = create_bm25_index()

    query_tokens = query.lower().split()

    results = bm25.get_top_n(
        query_tokens,
        chunks,
        n=top_k
    )

    return results