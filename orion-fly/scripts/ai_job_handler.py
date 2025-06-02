import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def summarize_job(title, company, url):
    # Basic summary (you’ll later upgrade this with real AI like Ollama or OpenAI)
    return f"🔥 *{title}* at *{company}*\n🔗 {url}"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, data=payload)
    return r.status_code == 200

def run():
    print("Fetching jobs...")
    res = requests.get("https://remoteok.com/api")
    if res.status_code != 200:
        print(f"❌ Failed to fetch jobs: {res.status_code}")
        return

    jobs = res.json()[1:6]  # Limit to top 5 jobs
    for job in jobs:
        title = job.get("position", "No Title")
        company = job.get("company", "Unknown")
        url = f"https://remoteok.com{job.get('url', '')}"
        summary = summarize_job(title, company, url)
        print(summary)
        send_to_telegram(summary)

if __name__ == "__main__":
    run()
