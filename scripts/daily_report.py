import psutil
import datetime
import requests

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Failed to send Telegram message:", e)

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = (
        f"*ORION Daily System Report*\n"
        f"🕒 Time: {now}\n"
        f"💻 CPU Usage: {cpu}%\n"
        f"🧠 RAM Usage: {ram.percent}% ({ram.used // (1024**2)}MB used / {ram.total // (1024**2)}MB total)\n"
        f"💾 Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB used / {disk.total // (1024**3)}GB total)\n"
    )
    return report

if __name__ == "__main__":
    report = get_system_stats()
    send_message(report)
