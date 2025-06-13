import sys, os; sys.path.append(os.path.abspath("."))  # Add root to import utils
import os, json, time, pathlib
from utils.telegram import send_telegram_message

DB = pathlib.Path("orion/data/dashboard.json")
DB.parent.mkdir(parents=True, exist_ok=True)

def load():
    if DB.exists(): return json.loads(DB.read_text())
    return {"stats": []}

def save(data):
    DB.write_text(json.dumps(data, indent=2))

def snapshot():
    data = load()
    stats = {
        "ts": time.time(),
        "jobs_applied": len(list(pathlib.Path("orion/logs/applications").glob("*.log"))) if pathlib.Path("orion/logs/applications").exists() else 0,
        "errors": len(list(pathlib.Path("orion/logs/errors.log").open())) if pathlib.Path("orion/logs/errors.log").exists() else 0,
    }
    data["stats"].append(stats)
    save(data)
    send_telegram_message(f"📊 ORION Dashboard • Jobs: {stats['jobs_applied']} • Errors: {stats['errors']}")
    print("Dashboard updated.")

if __name__ == "__main__":
    snapshot()
