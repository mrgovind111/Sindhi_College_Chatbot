import json
import os

LOG_FILE = "data/question_log.json"


def log_question(question):
    """Save a question to the log file."""
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append(question.lower().strip())

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)


def get_stats():
    """Return total count and top questions."""
    if not os.path.exists(LOG_FILE):
        return 0, []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    total = len(logs)

    counts = {}
    for q in logs:
        counts[q] = counts.get(q, 0) + 1

    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return total, top


def clear_logs():
    """Wipe all logged questions."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)