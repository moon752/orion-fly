import os
import requests

token = os.environ.get("BOT_TOKEN")
chat_id = "7485198018"
message = "✅ ORION is live and secure on Replit!"

if not token:
    print("❌ BOT_TOKEN is missing. Add it in the Replit Secrets tab.")
    exit(1)

print("✅ BOT_TOKEN loaded.")
print("📤 Sending message to Telegram...")

url = f"https://api.telegram.org/bot{token}/sendMessage"
resp = requests.post(url, data={"chat_id": chat_id, "text": message})

print("📡 Response Status:", resp.status_code)
print("📩 Telegram Response:", resp.text)
