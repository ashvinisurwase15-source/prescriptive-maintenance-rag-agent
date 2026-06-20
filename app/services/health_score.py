def calculate_health_score(query: str):

    score = 100

    query = query.lower()

    if "temperature" in query:
        score -= 20

    if "vibration" in query:
        score -= 25

    if "pressure" in query:
        score -= 15

    if score >= 80:
        status = "Healthy"
    elif score >= 60:
        status = "Warning"
    else:
        status = "Critical"

    return {
        "health_score": score,
        "status": status
    }