
import sys, os, time
sys.path.insert(0, os.path.abspath('.'))

from job_applicator import fetch_jobs, apply_to_job
from orion.brain.scorer import score_job

jobs = fetch_jobs()
print(f"🔍 fetched {len(jobs)} jobs")

for j in jobs:
    s = score_job(j)
    decision = "APPLY" if s >= 0.5 else "skip"
    print(f"{decision:5} | score {s:.2f} | {j['title']}")
    if s >= 0.5:
        apply_to_job(j)
        time.sleep(1)
