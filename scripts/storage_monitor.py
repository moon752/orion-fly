import shutil
import requests

TELEGRAM_BOT_TOKEN = "8140849713:AAFrbl-VYiJdIXen9TP3Jolv8ge5ZmnM0P4"
TELEGRAM_CHAT_ID = "7485198018"
LIMIT_MB = 5000  # 5GB

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload).raise_for_status()
    except Exception as e:
        print("Telegram message failed:", e)

def check_storage(path="/data/data/com.termux/files/home"):
    total, used, free = shutil.disk_usage(path)
    used_mb = used // (1024 * 1024)
    if used_mb > LIMIT_MB:
        send_message(f"⚠️ Storage alert! Used: {used_mb} MB exceeds limit of {LIMIT_MB} MB.")

if __name__ == "__main__":
    check_storage()
