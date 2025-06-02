import requests

TELEGRAM_BOT_TOKEN = "8140849713:AAFrbl-VYiJdIXen9TP3Jolv8ge5ZmnM0P4"
TELEGRAM_CHAT_ID = "7485198018"

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
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print("Failed to send message:", e)

if __name__ == "__main__":
    send_message("Hello from ORION bot! 🚀")
