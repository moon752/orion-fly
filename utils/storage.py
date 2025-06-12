import os
import json
from datetime import datetime, timedelta

BASE = "orion_data"
os.makedirs(BASE + "/tasks", exist_ok=True)
os.makedirs(BASE + "/cache", exist_ok=True)

def save_task(name, data):
    with open(f"{BASE}/tasks/{name}_{datetime.utcnow().timestamp()}.json", "w") as f:
        json.dump(data, f)

def load_tasks():
    files = os.listdir(BASE + "/tasks")
    result = {}
    for f in files:
        with open(f"{BASE}/tasks/" + f) as file:
            result[f] = json.load(file)
    return result

def rotate_cache(days_old=3):
    now = datetime.utcnow()
    for f in os.listdir(BASE + "/cache"):
        path = os.path.join(BASE + "/cache", f)
        if os.path.isfile(path):
            created = datetime.utcfromtimestamp(os.path.getctime(path))
            if now - created > timedelta(days=days_old):
                os.remove(path)
