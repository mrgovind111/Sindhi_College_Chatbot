# Load the college file once when the app starts
with open("data/college_info.txt", "r", encoding="utf-8") as f:
    COLLEGE_TEXT = f.read()

# Split into chunks by blank lines
CHUNKS = [c.strip() for c in COLLEGE_TEXT.split("\n\n") if c.strip()]


def get_context(question):
    """Return the chunks most relevant to the question (simple keyword match)."""
    q_words = set(question.lower().split())

    scored = []
    for chunk in CHUNKS:
        chunk_words = set(chunk.lower().split())
        score = len(q_words & chunk_words)
        if score > 0:
            scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    top = [chunk for _, chunk in scored[:3]]

    if not top:
        return COLLEGE_TEXT[:1500]  # fallback: first part of the file

    return "\n\n".join(top)