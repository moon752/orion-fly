import requests
import os

BOT_TOKEN = "8140849713:AAFrbl-VYiJdIXen9TP3Jolv8ge5ZmnM0P4"
CHAT_ID = "7485198018"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")
