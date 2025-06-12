import time
import threading
import json
import os
from orion.utils.telegram_notify import notify_admin

DASHBOARD_PATH = "orion/storage/dashboard.json"

# Create dashboard storage if not exists
os.makedirs(os.path.dirname(DASHBOARD_PATH), exist_ok=True)
if not os.path.exists(DASHBOARD_PATH):
    with open(DASHBOARD_PATH, "w") as f:
        json.dump({"stats": []}, f)

def update_dashboard(stat):
    with open(DASHBOARD_PATH, "r") as f:
        data = json.load(f)

    data["stats"].append(stat)

    with open(DASHBOARD_PATH, "w") as f:
        json.dump(data, f, indent=2)

def monitor_orion():
    while True:
        stat = {
            "timestamp": time.time(),
            "jobs_applied": len(os.listdir("orion/logs/applications")) if os.path.exists("orion/logs/applications") else 0,
            "errors": len(os.listdir("orion/logs/errors")) if os.path.exists("orion/logs/errors") else 0,
        }
        update_dashboard(stat)
        time.sleep(60 * 5)  # every 5 minutes

def display_summary():
    with open(DASHBOARD_PATH, "r") as f:
        data = json.load(f)
        stats = data["stats"][-1] if data["stats"] else {}

    summary = f"""
📊 ORION Global Dashboard
🕓 Last Update: {time.ctime(stats.get("timestamp", 0))}
🧠 Jobs Applied: {stats.get("jobs_applied", 0)}
❌ Errors: {stats.get("errors", 0)}
"""
    notify_admin(summary)

def launch_dashboard():
    threading.Thread(target=monitor_orion, daemon=True).start()
    notify_admin("📡 ORION Global Monitor Online")
