import os, requests, telegram
from flask import Flask, request

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" not in data: return "OK", 200

    user_msg = data["message"].get("text", "")
    print("📥", user_msg)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [{"role": "user", "content": user_msg}],
        "stream": False
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response_text = res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        response_text = f"❌ ORION error: {e}"

    bot.send_message(chat_id=CHAT_ID, text=response_text)
    return "OK", 200

@app.route("/start", methods=["GET"])
def start():
    bot.send_message(chat_id=CHAT_ID, text="🟢 ORION is online and ready.")
    return "Started", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
