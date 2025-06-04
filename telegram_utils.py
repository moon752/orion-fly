import requests

# Replace with your actual Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "8140849713:AAFrbl-VYiJdIXen9TP3Jolv8ge5ZmnM0P4"
CHAT_ID = "7485198018"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        res = requests.post(url, json=payload)
        if res.status_code != 200:
            print("Failed to send Telegram message:", res.text)
    except Exception as e:
        print("Telegram error:", str(e))
