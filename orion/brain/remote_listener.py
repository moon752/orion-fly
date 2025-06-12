import time
import threading
import requests
import os
from orion.utils.telegram_notify import notify_admin

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
COMMAND_PREFIX = "/orion"

def handle_command(text):
    if text == "/orion status":
        notify_admin("✅ ORION is online and operational.")
    elif text.startswith("/orion summary"):
        from orion.monitor.dashboard import display_summary
        display_summary()
    elif text.startswith("/orion restart"):
        notify_admin("🔄 Restarting ORION process (simulated).")
        os.execv(__file__, ["python"] + sys.argv)
    else:
        notify_admin(f"⚠️ Unknown command received: {text}")

def telegram_listener():
    offset = None
    notify_admin("📡 ORION Remote Listener Activated.")
    while True:
        try:
            resp = requests.get(API_URL, params={"offset": offset}, timeout=30)
            if resp.status_code == 200:
                updates = resp.json().get("result", [])
                for update in updates:
                    offset = update["update_id"] + 1
                    message = update.get("message", {})
                    text = message.get("text", "")
                    if text.startswith(COMMAND_PREFIX):
                        handle_command(text.strip())
        except Exception as e:
            notify_admin(f"⚠️ Remote listener error: {e}")
        time.sleep(5)

def launch_remote_commands():
    threading.Thread(target=telegram_listener, daemon=True).start()
