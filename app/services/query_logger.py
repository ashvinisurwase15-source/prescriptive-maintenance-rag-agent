from datetime import datetime


def log_query(query, results_count):
    with open("query_logs.txt", "a") as file:
        file.write(
            f"{datetime.now()} | Query: {query} | Results: {results_count}\n"
        )