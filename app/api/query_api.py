from fastapi import APIRouter

from app.models.query_request import QueryRequest
from app.rag.retriever import search_documents
from app.services.llm_recommendation import generate_llm_recommendation

router = APIRouter()


@router.post("/query")
def query_documents(request: QueryRequest):

    results = search_documents(request.query)

    context = "\n".join(results)

    recommendation = generate_llm_recommendation(
        request.query,
        context
    )

    return {
        "query": request.query,
        "recommendation": recommendation,
        "results": results
    }