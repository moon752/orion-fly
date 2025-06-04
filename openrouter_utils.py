
import random
from telegram_utils import send_telegram_message
from openrouter import query_openrouter

def choose_and_apply_jobs(jobs):
    summary = ""
    for job in jobs:
        title = job.get('position', '')
        tags = job.get('tags', [])
        description = job.get('description', '')

        prompt = f"""
You are ORION, an elite AI freelancer.
Job Title: {title}
Tags: {tags}
Description: {description}

Decide:
1. Is this job a good match for your skills (Python, AI, automation)?
2. If yes, write a short custom application message.
3. If no, say "Skip".

Respond ONLY with the application or "Skip".
"""

        response = query_openrouter(prompt).strip()

        if "skip" in response.lower():
            continue

        message = f"""🧠 **Applied for Job**

💼 Title: {title}
🏷️ Tags: {', '.join(tags)}
📨 Message:
{response}

✅ Status: Sent
"""
        send_telegram_message(message)
        summary += f"✅ Applied to: {title}\n"

    return summary if summary else "🤷 ORION skipped all jobs this round."
