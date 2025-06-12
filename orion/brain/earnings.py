import json
import os
from datetime import datetime

EARNINGS_FILE = "orion/storage/earnings.json"

def log_earning(platform, amount):
    if not os.path.exists(EARNINGS_FILE):
        with open(EARNINGS_FILE, "w") as f:
            json.dump({}, f)

    with open(EARNINGS_FILE, "r") as f:
        data = json.load(f)

    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        data[today] = {}

    if platform not in data[today]:
        data[today][platform] = 0

    data[today][platform] += amount

    with open(EARNINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_daily_total():
    if not os.path.exists(EARNINGS_FILE):
        return 0
    with open(EARNINGS_FILE, "r") as f:
        data = json.load(f)
    today = datetime.now().strftime("%Y-%m-%d")
    return sum(data.get(today, {}).values())
