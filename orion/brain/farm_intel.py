import json
from datetime import datetime
from orion.utils.telegram_notify import notify_admin

FARM_LOG = "orion/storage/source_earnings.json"

def log_earnings(source, value):
    try:
        with open(FARM_LOG, "r") as f:
            data = json.load(f)
    except:
        data = {}
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        data[today] = {}
    if source not in data[today]:
        data[today][source] = 0
    data[today][source] += value
    with open(FARM_LOG, "w") as f:
        json.dump(data, f, indent=2)

def top_sources():
    try:
        with open(FARM_LOG, "r") as f:
            data = json.load(f)
    except:
        return []
    today = datetime.now().strftime("%Y-%m-%d")
    sources = data.get(today, {})
    return sorted(sources.items(), key=lambda x: -x[1])

def report_top_sources():
    sources = top_sources()
    if not sources:
        notify_admin("📉 No farming activity yet today.")
    else:
        lines = [f"{src}: ${val}" for src, val in sources]
        notify_admin("🌾 Top Job Sources Today:\\n" + "\\n".join(lines))
