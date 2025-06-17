
"""Debug runner: fetch jobs, score, decide, report."""
import json, time
from job_applicator import fetch_jobs, apply_to_job
from orion.brain.scorer import score_job

jobs = fetch_jobs()
print(f"🔍 Fetched {len(jobs)} jobs.")

applied = 0
for j in jobs:
    s = score_job(j)
    status = "🚀 APPLY" if s >= 0.5 else "⏭️ SKIP"
    print(f"{status}  score={s:.2f}  title={j.get('title')[:60]}")
    if s >= 0.5:
        apply_to_job(j)
        applied += 1
        time.sleep(1)   # polite delay
print(f"✅ Done. Applied to {applied} job(s).")
