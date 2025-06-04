from logger import LOG_FILE
import json
from telegram_utils import send_telegram_message
from datetime import datetime

def send_daily_report():
    try:
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    today = datetime.utcnow().date()
    today_apps = [d for d in data if datetime.fromisoformat(d['timestamp']).date() == today]

    total_jobs = len(today_apps)
    total_earnings = sum(d['earnings'] for d in today_apps)

    msg = f"📊 ORION Daily Report:\nJobs Applied: {total_jobs}\nEarnings: $${total_earnings:.2f}"
    send_telegram_message(msg)

if __name__ == '__main__':
    send_daily_report()
