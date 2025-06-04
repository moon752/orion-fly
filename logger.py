import json
from datetime import datetime

LOG_FILE = 'logs/applications_log.json'

def log_application(job, status, earnings=0):
    try:
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "job_title": job['title'],
        "status": status,
        "earnings": earnings
    }
    data.append(entry)

    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=2)
