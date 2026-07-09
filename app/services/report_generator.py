def generate_report(
    query,
    health,
    failure_risk,
    priority,
    severity,
    recommendation
):

    report = f"""
========================================
      MACHINE MAINTENANCE REPORT
========================================

Query:
{query}

Health Score:
Score : {health["health_score"]}
Status: {health["status"]}

Failure Risk:
Score : {failure_risk["risk_score"]}
Level : {failure_risk["risk_level"]}

Priority:
Score : {priority["priority_score"]}
Level : {priority["priority_level"]}

Severity:
Score : {severity["severity_score"]}
Level : {severity["severity_level"]}

Recommendation:
{recommendation}

========================================
"""

    return report