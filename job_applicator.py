import os
import time
import requests
import traceback
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(msg: str):
    try:
        requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            params={"chat_id": TELEGRAM_CHAT_ID, "text": msg},
            timeout=10
        )
    except Exception:
        print("Failed to send message to Telegram")
        traceback.print_exc()


def apply_to_job(job):
    # Simulated job application logic
    print(f"Applying to: {job['title']}")
    return True


def main():
    jobs = [
        {"title": "Python Developer", "id": 1},
        {"title": "API Integrator", "id": 2}
    ]

    successful = 0
    failed = 0

    for job in jobs:
        try:
            if apply_to_job(job):
                successful += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            send_telegram(f"❌ Failed to apply to {job['title']}: {e}")

    summary = f"✅ Job applications done.\nSuccess: {successful}\nFailed: {failed}"
    send_telegram(summary)


if __name__ == "__main__":
    main()
