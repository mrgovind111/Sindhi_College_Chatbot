import json
import os

LOG_FILE = "data/question_log.json"
FEEDBACK_FILE = "data/feedback_log.json"


def _ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")


def _load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------------- Question logging ----------------
def log_question(question):
    _ensure_data_dir()
    logs = _load_json(LOG_FILE)
    logs.append(question.lower().strip())
    _save_json(LOG_FILE, logs)


def get_stats():
    logs = _load_json(LOG_FILE)
    total = len(logs)

    counts = {}
    for q in logs:
        counts[q] = counts.get(q, 0) + 1

    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return total, top


def clear_logs():
    _save_json(LOG_FILE, [])


# ---------------- Feedback ----------------
def log_feedback(question, answer, rating):
    """rating: 'up' or 'down'"""
    _ensure_data_dir()
    entries = _load_json(FEEDBACK_FILE)
    entries.append({
        "question": question,
        "answer": answer,
        "rating": rating
    })
    _save_json(FEEDBACK_FILE, entries)


def get_feedback_stats():
    entries = _load_json(FEEDBACK_FILE)
    total = len(entries)
    up = sum(1 for e in entries if e.get("rating") == "up")
    down = sum(1 for e in entries if e.get("rating") == "down")
    return total, up, down


def clear_feedback():
    _save_json(FEEDBACK_FILE, [])
# ---------------- Admission Enquiries ----------------
ADMISSION_FILE = "data/admissions.json"


def log_admission(name, phone, email, course, message):
    _ensure_data_dir()
    entries = _load_json(ADMISSION_FILE)
    entries.append({
        "name": name,
        "phone": phone,
        "email": email,
        "course": course,
        "message": message
    })
    _save_json(ADMISSION_FILE, entries)


def get_admissions():
    return _load_json(ADMISSION_FILE)


def clear_admissions():
    _save_json(ADMISSION_FILE, [])