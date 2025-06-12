import logging
import time
import random
from job_fetcher import fetch_remoteok_jobs
from job_handler import apply_to_job
from logger import log_info, log_error, log_warning

# Set up logging with a rotating log file
logging.basicConfig(
    filename='orion.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Intelligent Job Eligibility Criteria
def is_job_eligible(job):
    """Check if a job is eligible for retry"""
    # Add more eligibility criteria as needed
    eligible_criteria = [
        job.get('title'),
        job.get('url'),
        job.get('description'),  # add more criteria as needed
    ]
    return all(eligible_criteria)

# Improved Job Processing with Retry Mechanism
def process_job(job):
    """Process a single job"""
    max_attempts = 3
    retry_delay = 5  # seconds
    retry_backoff = 1.5  # exponential backoff factor

    for attempt in range(max_attempts):
        try:
            apply_to_job(job)
            log_info(f"Applied to job: {job['title']}")
            return True
        except Exception as e:
            log_warning(f"Error applying to job: {job['title']} (attempt {attempt+1}/{max_attempts}).")
            if attempt < max_attempts - 1:  # not the last attempt
                retry_delay *= retry_backoff
                             f"Retrying in {int(retry_delay)} seconds...")
                time.sleep(retry_delay)
                log_error(f"Failed to apply to job: {job['title']} after {max_attempts} attempts.")
return False

# Enhanced Job Processing with Randomization
def process_jobs(jobs):
    """Process a list of jobs"""
    job_results = {'successful': 0, 'failed': 0, 'skipped': 0}

    # Shuffle the job list to avoid sequential failures
    shuffled_jobs = jobs

    for job in shuffled_jobs:
        if not is_job_eligible(job):
            log_info(f"Skipped ineligible job: {job}")
            job_results['skipped'] += 1
            continue

        if process_job(job):
            job_results['successful'] += 1
        else:
            job_results['failed'] += 1

    summary = f"Applied successfully: {job_results['successful']}, Failed: {job_results['failed']}, Skipped: {job_results['skipped']}"
    log_info(summary)

def main():
    """Main entry point of the ORION module"""
    jobs = fetch_remoteok_jobs()

    if not jobs:
        log_info("No jobs found.")
        return

    log_info("Processing jobs...")
    process_jobs(jobs)
    log_info("Job processing completed.")

if __name__ == "__main__":
        main()