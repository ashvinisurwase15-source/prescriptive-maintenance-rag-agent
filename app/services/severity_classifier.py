def classify_severity(query: str):

    query = query.lower()

    score = 0

    if "temperature" in query:
        score += 25

    if "vibration" in query:
        score += 25

    if "pressure" in query:
        score += 20

    if "shutdown" in query:
        score += 40

    if score >= 80:
        severity = "Critical"

    elif score >= 50:
        severity = "High"

    elif score >= 25:
        severity = "Medium"

    else:
        severity = "Low"

    return {
        "severity_score": score,
        "severity_level": severity
    }