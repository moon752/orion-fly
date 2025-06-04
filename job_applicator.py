from job_fetcher import fetch_remoteok_jobs
from job_handler import apply_to_job

jobs = fetch_remoteok_jobs()
for job in jobs:
    apply_to_job(job)
