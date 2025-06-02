import random
from utils.telegram import send_message

def generate_cover_letter(role, company):
    return f"""Dear {company} team,

I am excited to apply for the {role} position. With strong experience in AI, automation, and software engineering, I bring creativity and precision to every project. I’m confident I’d add value to your team from day one.

Looking forward to hearing from you.

Best regards,  
David Muigai
"""

def auto_apply():
    # Simulated job data (replace this with real fetched jobs later)
    jobs = [
        {"role": "Backend Developer", "company": "Acme Inc"},
        {"role": "Video Editor", "company": "Vision Studio"},
        {"role": "Python Engineer", "company": "DevCore"}
    ]
    job = random.choice(jobs)
    cover_letter = generate_cover_letter(job["role"], job["company"])

    send_message(f"📄 *Application Draft for {job['role']} at {job['company']}*\n\n```\n{cover_letter}\n```")

if __name__ == "__main__":
    auto_apply()
