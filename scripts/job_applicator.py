import os
import requests
import random
from utils.telegram import send_message
from utils.llm import generate_cover_letter
from scripts.fetch_jobs import fetch_remoteok_jobs

KEYWORDS = ["python", "automation", "AI", "machine learning", "backend"]

def is_relevant(job_title):
    return any(keyword.lower() in job_title.lower() for keyword in KEYWORDS)

def apply_to_jobs():
    send_message("🧠 Starting job matcher + cover letter generator...")
    jobs = fetch_remoteok_jobs()
    for job in jobs:
        title = job['title']
        company = job['company']
        url = job['url']
        if is_relevant(title):
            message = f"🎯 Applying to: *{title}* at *{company}*\n🔗 {url}"
            send_message(message)
            cover_letter = generate_cover_letter(title, company)
            send_message(f"📝 Generated Cover Letter:\n\n{cover_letter}")
            break  # apply to only one for now

if __name__ == "__main__":
    apply_to_jobs()
