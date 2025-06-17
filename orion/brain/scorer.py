"""ORION job‑scoring helper — returns float 0‑1."""

import re
from utils.ai_model import smart_chat

def score_job(job: dict, temp: float = 0.4) -> float:
    """Ask LLM to give a 0‑1 score. If parsing fails, return 0.0."""
    prompt = (
        "Rate this freelance job from 0 to 1 and **return only the number**.\n"
        f"Title: {job.get('title')}\n"
        f"Description: {job.get('description', '')}"
    )
    reply = smart_chat([{"role": "user", "content": prompt}], temp=temp)
    match = re.search(r"\d*\.\d+|\d+", str(reply))
    if match:
        try:
            return max(0.0, min(1.0, float(match.group())))
        except ValueError:
            pass
    return 0.0
