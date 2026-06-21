from fastapi import APIRouter

from app.models.query_request import QueryRequest
from app.rag.retriever import search_documents
from app.services.llm_recommendation import generate_llm_recommendation
from app.services.health_score import calculate_health_score
from app.services.failure_risk import predict_failure_risk
from app.services.priority_classifier import classify_priority

router = APIRouter()


@router.post("/query")
def query_documents(request: QueryRequest):

    results = search_documents(request.query)

    context = "\n".join(results)

    recommendation = "LLM temporarily disabled for testing"

    health = calculate_health_score(
        request.query
    )
    failure_risk = predict_failure_risk(
        request.query
    )
    priority = classify_priority(
        request.query
    )

    return {
        "query": request.query,
        "health": health,
        "failure_risk": failure_risk,
        "priority": priority,
        "recommendation": recommendation,
        "results": results
    }