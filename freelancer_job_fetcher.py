import requests
from bs4 import BeautifulSoup
import time

def fetch_freelancer_jobs(query="python", max_results=10):
    url = f"https://www.freelancer.com/jobs/{query}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch jobs from Freelancer.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    job_cards = soup.select("div.JobSearchCard-item")[:max_results]
    for card in job_cards:
        title = card.select_one("a.JobSearchCard-primary-heading-link")
        description = card.select_one("p.JobSearchCard-primary-description")
        link = title["href"] if title else "#"

        jobs.append({
            "title": title.text.strip() if title else "No title",
            "description": description.text.strip() if description else "No description",
            "link": "https://www.freelancer.com" + link
        })

    return jobs

if __name__ == "__main__":
    print("🔍 Fetching Freelancer jobs...\\n")
    jobs = fetch_freelancer_jobs("python", max_results=5)
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job[\"title\"]}")
        print(f"   {job[\"description\"]}")
        print(f"   🔗 {job[\"link\"]}\\n")
        time.sleep(0.3)
