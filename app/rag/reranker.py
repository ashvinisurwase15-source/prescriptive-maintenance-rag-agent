def rerank_documents(query, documents):
    query_words = set(query.lower().split())

    scored_docs = []

    for doc in documents:
        content_words = set(doc.page_content.lower().split())

        score = len(query_words.intersection(content_words))

        scored_docs.append((score, doc))

    scored_docs.sort(reverse=True, key=lambda x: x[0])

    return [doc for score, doc in scored_docs]