def classify_priority(query: str):

    query = query.lower()

    score = 0

    if "temperature" in query:
        score += 30

    if "vibration" in query:
        score += 30

    if "pressure" in query:
        score += 20

    if "shutdown" in query:
        score += 40

    if score >= 80:
        priority = "Urgent"

    elif score >= 60:
        priority = "High"

    elif score >= 30:
        priority = "Medium"

    else:
        priority = "Low"

    return {
        "priority_score": score,
        "priority_level": priority
    }