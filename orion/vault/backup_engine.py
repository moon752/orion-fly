import os
import time
import hashlib
import json
from datetime import datetime
from orion.utils.telegram_notify import notify_admin

VAULT_PATH = "orion/storage/vault/"
os.makedirs(VAULT_PATH, exist_ok=True)

def hash_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def create_snapshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_file = f"{VAULT_PATH}orion_backup_{timestamp}.json"
    data = {
        "timestamp": timestamp,
        "jobs": os.listdir("orion/logs/applications") if os.path.exists("orion/logs/applications") else [],
        "errors": os.listdir("orion/logs/errors") if os.path.exists("orion/logs/errors") else []
    }
    with open(snapshot_file, "w") as f:
        json.dump(data, f, indent=2)

    hash_val = hash_file(snapshot_file)
    notify_admin(f"🗂️ Backup created: {snapshot_file}\n🔐 SHA256: {hash_val}")
    return snapshot_file

def trigger_backup_if_needed(job_count):
    if job_count % 20 == 0:
        create_snapshot()
