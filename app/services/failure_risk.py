def predict_failure_risk(query: str):

    query = query.lower()

    risk_score = 0

    if "temperature" in query:
        risk_score += 40

    if "vibration" in query:
        risk_score += 40

    if "pressure" in query:
        risk_score += 20

    if risk_score >= 70:
        risk = "High"

    elif risk_score >= 40:
        risk = "Medium"

    else:
        risk = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk
    }