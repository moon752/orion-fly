import requests
import time
from freelancer_job_fetcher import fetch_freelancer_jobs

OPENROUTER_API_KEY = "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"  # 🔐 Your real key

def generate_cover_letter(job_title, job_description):
    prompt = f"""You are a skilled freelancer. Write a short, professional proposal to apply for this job:

Title: {job_title}
Description: {job_description}

Your tone should be confident, concise, and human-sounding.
"""
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-coder:free",
            "messages": [
                {"role": "system", "content": "You are a helpful freelance assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 400
        }
    )

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error generating cover letter: {e}"

if __name__ == "__main__":
    print("🤖 Fetching jobs and generating proposals...\n")
    jobs = fetch_freelancer_jobs("python", max_results=3)
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']}")
        print(f"   🔗 {job['link']}")
        print(f"   🧠 Generating cover letter...")
        cover_letter = generate_cover_letter(job["title"], job["description"])
        print(f"   📄 Proposal:\n{cover_letter}\n")
        time.sleep(1)
