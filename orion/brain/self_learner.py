import json
import os
from orion.utils.telegram_notify import notify_admin

DATA_FILE = "orion/storage/job_history.json"

def log_job(client_name, value, result="success"):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    history = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            history = json.load(f)
    history.append({"client": client_name, "value": value, "result": result})
    with open(DATA_FILE, "w") as f:
        json.dump(history[-100:], f, indent=2)  # keep latest 100 jobs

def analyze_history():
    if not os.path.exists(DATA_FILE):
        return {"total": 0, "avg": 0, "best_client": None}
    with open(DATA_FILE, "r") as f:
        history = json.load(f)
    total = sum(j["value"] for j in history)
    avg = total / len(history)
    top_client = max(history, key=lambda j: j["value"])["client"]
    return {"total": total, "avg": avg, "best_client": top_client}

def self_improve():
    stats = analyze_history()
    notify_admin(f"📊 ORION Self-Learning Report:\\nTotal Earned: ${stats[total]}\\nAvg Deal: ${int(stats[avg])}\\nTop Client: {stats[best_client]}")
