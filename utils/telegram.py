import os, requests, textwrap

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(text: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("🔔 Telegram env vars missing — cannot send message.")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text[:4096]})
