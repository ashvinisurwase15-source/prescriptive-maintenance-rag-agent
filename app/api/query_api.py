from fastapi import APIRouter

from app.models.query_request import QueryRequest

from app.rag.hybrid_retriever import hybrid_search

from app.services.llm_recommendation import generate_llm_recommendation
from app.services.health_score import calculate_health_score
from app.services.failure_risk import predict_failure_risk
from app.services.priority_classifier import classify_priority
from app.services.severity_classifier import classify_severity
from app.services.report_generator import generate_report
from app.services.email_service import send_email

router = APIRouter()


@router.post("/query")
def query_documents(request: QueryRequest):

    # Step 1: Hybrid Search
    results = hybrid_search(request.query)

    # Step 2: Convert Documents into text
    context = "\n".join([doc.page_content for doc in results])

    # Step 3: LLM Recommendation
    try:
        recommendation = generate_llm_recommendation(
            request.query,
            context
        )
    except Exception as e:
        recommendation = f"LLM service unavailable: {str(e)}"

    # Step 4: Health Score
    health = calculate_health_score(request.query)

    # Step 5: Failure Risk
    failure_risk = predict_failure_risk(request.query)

    # Step 6: Priority
    priority = classify_priority(request.query)

    # Step 7: Severity
    severity = classify_severity(request.query)

    # Step 9: Generate Report
    report = generate_report(
        request.query,
        health,
        failure_risk,
        priority,
        severity,
        recommendation
    )

    # Step 10: Send Email
    try:
        send_email(
            receiver_email="ADITYALKHARADE@gmail.com",
            report=report
        )
    except Exception as e:
        print(f"Email Error: {e}")

    # Step 11: Return Response
    return {
        "query": request.query,
        "health": health,
        "failure_risk": failure_risk,
        "priority": priority,
        "severity": severity,
        "recommendation": recommendation,
        "report": report,
        "results": [doc.page_content for doc in results]
    }