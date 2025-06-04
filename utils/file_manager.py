import os
import json

def save_job_data(job, filename):
    os.makedirs("jobs", exist_ok=True)
    with open(os.path.join("jobs", filename), "w") as f:
        json.dump(job, f, indent=2)
