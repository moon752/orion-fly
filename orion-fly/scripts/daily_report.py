import os
import subprocess
import requests

token = os.environ.get("BOT_TOKEN")
chat_id = "7485198018"

if not token:
    print("❌ BOT_TOKEN is missing.")
    exit(1)

# Get disk usage
disk_usage = subprocess.getoutput("df -h /")

# Get uptime
uptime = subprocess.getoutput("uptime -p")

message = f"📊 Daily System Report:\n\nDisk Usage:\n{disk_usage}\n\nUptime:\n{uptime}"

url = f"https://api.telegram.org/bot{token}/sendMessage"
resp = requests.post(url, data={"chat_id": chat_id, "text": message})

print(f"Report sent with status {resp.status_code}")
