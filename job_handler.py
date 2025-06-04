import os
import json
import random
from utils.telegram import send_telegram_message
from utils.file_manager import save_job_data
from job_types.code_runner import handle_code_job
from job_types.writer_runner import handle_writer_job

TEMPLATE_PROPOSALS = {
    "code": [
        "Hi! I'm a seasoned Python developer ready to tackle your project immediately. Let’s make it happen!",
        "Experienced with automation, APIs, and backend work. Can start now and deliver high quality!"
    ],
    "writing": [
        "I write high-quality, engaging content tailored to your needs. Fast turnaround, zero fluff.",
        "Skilled writer here! I can start right away and deliver polished content on time."
    ]
}

def detect_job_type(job):
    title = job.get("position", "").lower()
    description = job.get("description", "").lower()

    if "python" in title or "developer" in title or "backend" in description:
        return "code"
    elif "writer" in title or "content" in description or "copy" in description:
        return "writing"
    else:
        return "unknown"

def apply_to_job(job):
    job_type = detect_job_type(job)
    proposal = random.choice(TEMPLATE_PROPOSALS.get(job_type, ["I'd love to work on this project!"]))

    # Save job data
    job_id = job.get("id", f"job_{random.randint(1000,9999)}")
    save_job_data(job, f"job_{job_id}.json")

    # Simulate sending application (for now just Telegram)
    msg = f"📌 Applied to: {job.get('position')}\nType: {job_type}\nProposal: {proposal}"
    send_telegram_message(msg)

    # Route to job-specific handler
    if job_type == "code":
        handle_code_job(job)
    elif job_type == "writing":
        handle_writer_job(job)
    else:
        send_telegram_message("⚠️ Unknown job type. Skipped handler.")

    return True
