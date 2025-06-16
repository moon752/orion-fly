import os, requests
def send_telegram(msg):
    token=os.getenv("TELEGRAM_BOT_TOKEN"); chat=os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat: print("[TG] missing token/chat"); return
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id":chat,"text":msg[:4096]})
