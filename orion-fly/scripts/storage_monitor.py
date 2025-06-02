import os
import subprocess
import requests

token = os.environ.get("BOT_TOKEN")
chat_id = "7485198018"
threshold_percent = 80  # alert if disk usage goes above this %

if not token:
    print("❌ BOT_TOKEN missing.")
    exit(1)

# Get disk usage for root "/"
df_output = subprocess.getoutput("df -h /")
usage_line = df_output.splitlines()[1]
used_percent_str = usage_line.split()[4]  # e.g. '45%'
used_percent = int(used_percent_str.strip('%'))

if used_percent >= threshold_percent:
    message = f"⚠️ WARNING: Disk usage is at {used_percent}%!\n\nDetails:\n{df_output}"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(url, data={"chat_id": chat_id, "text": message})
    print(f"Alert sent with status {resp.status_code}")
else:
    print(f"Disk usage is safe at {used_percent}%. No alert sent.")
