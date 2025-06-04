import time
from job_fetcher import fetch_jobs
from openrouter_utils import choose_and_apply_jobs

print("🔁 ORION starting up...")

def run_loop():
    while True:
        print("🔍 Fetching jobs...")
        jobs = fetch_jobs()
        print(f"📦 {len(jobs)} jobs found.")

        if jobs:
            print("🧠 Choosing and applying to jobs...")
            choose_and_apply_jobs(jobs)
        else:
            print("⏸️ No jobs found, waiting...")

        print("⏳ Sleeping for 1 hour...")
        time.sleep(3600)

if __name__ == "__main__":
    run_loop()
