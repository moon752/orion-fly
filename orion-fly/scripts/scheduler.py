import time
import subprocess

while True:
    print("Running auto_apply.py ...")
    subprocess.run(["python3", "scripts/auto_apply.py"])
    print("Waiting 6 hours until next run...")
    time.sleep(6 * 3600)  # 6 hours
