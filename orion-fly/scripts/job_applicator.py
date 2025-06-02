import sys, os; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import os
from utils.telegram import send_message

def generate_cover_letter(job_title, company):
    return f"""
Dear {company} Team,

I am writing to express my strong interest in the {job_title} role at {company}. With a deep passion for remote work and a proven ability to deliver high-quality results, I believe I would be an excellent fit for your team.

Thank you for considering my application. I look forward to the opportunity to contribute.

Best regards,  
ORION
"""

def main():
    jobs = [
        {"title": "Video Editor and Content Creator", "company": "Ritual"},
        {"title": "Senior React Native SDK Engineer", "company": "Nami ML"},
    ]

    for job in jobs:
        letter = generate_cover_letter(job["title"], job["company"])
        send_message(f"📝 Cover Letter for *{job['title']}* at *{job['company']}*:\n\n{letter}")

if __name__ == "__main__":
    main()
