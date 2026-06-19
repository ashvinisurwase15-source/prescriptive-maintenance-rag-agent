def generate_recommendation(results):

    if not results:
        return "No maintenance recommendation found."

    return f"Recommended Action: {results[0]}"