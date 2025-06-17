
"""Simple AI‑based job‑scorer for ORION."""

from utils.ai_model import smart_chat

def score_job(job: dict) -> float:
    """Return a float 0‑1 estimating how worthwhile the job is."""
    prompt = (
        "Rate this freelance job from 0 to 1 for ease, profit, and speed. "
        "Return ONLY the number.\n\n"
        f"Title: {job.get('title')}\n"
        f"Description: {job.get('description','')}"
    )
    reply = smart_chat([{"role": "user", "content": prompt}], temp=0.5)
    try:
        return max(0.0, min(1.0, float(str(reply).strip())))
    except Exception:
        return 0.0
