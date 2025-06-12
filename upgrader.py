import os
import requests
import json
import datetime
import time
from utils.telegram import send_telegram_message

GITHUB_REPO = "moon752/orion-fly"
MODULES = ["job_applicator.py", "freelance_monitor.py", "auto_reply.py"]
UPGRADE_LOG = "upgrade_log.json"
BACKUP_FOLDER = "backups"

def is_sunday():
    return datetime.datetime.today().weekday() == 6  # Sunday = 6

def log_upgrade(module, status):
    log = []
    if os.path.exists(UPGRADE_LOG):
        with open(UPGRADE_LOG, "r") as f:
            try:
                log = json.load(f)
            except:
                log = []
    log.append({
        "module": module,
        "status": status,
        "timestamp": datetime.datetime.now().isoformat()
    })
    with open(UPGRADE_LOG, "w") as f:
        json.dump(log, f, indent=2)

def restore_backup(name):
    backup_path = os.path.join(BACKUP_FOLDER, name)
    if os.path.exists(backup_path):
        with open(backup_path, "r") as f:
            with open(name, "w") as target:
                target.write(f.read())
        print(f"♻️ {name} restored from backup.")
    else:
        print(f"❌ No backup found for {name}.")

def download_module(name):
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/modules/{name}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(name, "w") as f:
                f.write(r.text)
            log_upgrade(name, "✅ Updated from GitHub")
            print(f"✅ {name} updated from GitHub.")
            send_telegram_message(f"🔄 ORION updated `{name}` from GitHub ✅")
        else:
            restore_backup(name)
            log_upgrade(name, "⚠️ GitHub 404 — fallback used")
            send_telegram_message(f"⚠️ GitHub missing `{name}`. Used backup.")
    except Exception as e:
        restore_backup(name)
        log_upgrade(name, f"⚠️ Exception — fallback used: {e}")
        send_telegram_message(f"🚨 Failed to update `{name}`: {e}")

def upgrade_all():
    print("🔁 Checking for module upgrades...")
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    for module in MODULES:
        download_module(module)

if __name__ == "__main__":
    if is_sunday():
        send_telegram_message("🧠 ORION Sunday Auto-Upgrade Started")
        upgrade_all()
    else:
        print("⏳ Not Sunday. Skipping auto-upgrade.")
