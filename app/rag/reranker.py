from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(query, documents):
    pairs = []

    for doc in documents:
        pairs.append((query, doc.page_content))

    scores = model.predict(pairs)

    scored_documents = list(zip(scores, documents))

    scored_documents.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for score, doc in scored_documents]