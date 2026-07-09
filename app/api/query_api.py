from fastapi import APIRouter

from app.services.email_service import send_email
from app.models.query_request import QueryRequest
from app.rag.retriever import search_documents
from app.services.llm_recommendation import generate_llm_recommendation
from app.services.health_score import calculate_health_score
from app.services.failure_risk import predict_failure_risk
from app.services.priority_classifier import classify_priority
from app.services.severity_classifier import classify_severity
from app.services.machine_monitor import get_machine_status
from app.services.report_generator import generate_report

router = APIRouter()


@router.post("/query")
def query_documents(request: QueryRequest):

    results = search_documents(request.query)

    context = "\n".join(results)
    try:
        recommendation = generate_llm_recommendation(
            request.query,
            context
        )

    except Exception as e:
        recommendation = f"LLM service unavailable: {str(e)}"



    health = calculate_health_score(
        request.query
    )
    failure_risk = predict_failure_risk(
        request.query
    )
    priority = classify_priority(
        request.query
    )
    severity = classify_severity(
        request.query
    )
    machines = get_machine_status()
    report = generate_report(
        request.query,
        health,
        failure_risk,
        priority,
        severity,
        recommendation
    )
    send_email(
        receiver_email="ADITYALKHARADE@gmail.com",
        report=report
    )

    return {
        "query": request.query,
        "health": health,
        "failure_risk": failure_risk,
        "priority": priority,
        "severity": severity,
        "machines": machines,
        "recommendation": recommendation,
        "report": report,
        "results": results
    }