#!/bin/bash

echo "🔄 ORION: Self-Upgrading & Launching..."

# 1. Pull latest from GitHub
git pull

# 2. Rebuild openrouter_utils.py
echo "⚙️ Updating brain: openrouter_utils.py"
cat > openrouter_utils.py << 'EOT'
from openrouter import query_openrouter

def filter_jobs(jobs):
    good_jobs = []
    for job in jobs:
        prompt = f"Is this job worth applying to? Job title: {job['title']}, Description: {job['description']}. Reply YES or NO."
        answer = query_openrouter(prompt)
        if 'yes' in answer.lower():
            good_jobs.append(job)
    return good_jobs

def generate_cover_letter(job):
    prompt = f"Write a professional cover letter for this job: {job['title']}, {job['description']}, using the name David Muigai."
    return query_openrouter(prompt)

def choose_and_apply_jobs(jobs):
    filtered = filter_jobs(jobs)
    for job in filtered:
        letter = generate_cover_letter(job)
        print(f"🚀 Applying to {job['title']}")
        print(f"📝 Cover Letter:\n{letter}")
EOT

# 3. Rebuild logger.py
echo "⚙️ Updating memory: logger.py"
mkdir -p logs
cat > logger.py << 'EOT'
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
EOT

# 4. Rebuild daily_report.py
echo "⚙️ Updating report system: daily_report.py"
cat > daily_report.py << 'EOT'
from logger import LOG_FILE
import json
from telegram_utils import send_telegram_message
from datetime import datetime

def send_daily_report():
    try:
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    today = datetime.utcnow().date()
    today_apps = [d for d in data if datetime.fromisoformat(d['timestamp']).date() == today]

    total_jobs = len(today_apps)
    total_earnings = sum(d['earnings'] for d in today_apps)

    msg = f"📊 ORION Daily Report:\nJobs Applied: {total_jobs}\nEarnings: $${total_earnings:.2f}"
    send_telegram_message(msg)

if __name__ == '__main__':
    send_daily_report()
EOT

# 5. Launch ORION
echo "🚀 Launching autonomous_applicator.py"
python autonomous_applicator.py

# 6. Send Report
echo "📤 Sending daily report"
python daily_report.py

echo "✅ ORION full run complete."
