from fastapi import APIRouter
from app.models.query_request import QueryRequest
from app.rag.retriever import search_documents
from app.services.recommendation import generate_recommendation

router = APIRouter()

@router.post("/query")
def query_documents(request: QueryRequest):

    results = search_documents(request.query)

    recommendation = generate_recommendation(results)

    return {
        "query": request.query,
        "recommendation": recommendation,
        "results": results
    }