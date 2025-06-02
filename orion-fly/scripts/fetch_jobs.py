import requests

API_URL = "https://remoteok.com/api"  # Simpler, more reliable for now

def fetch_jobs():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        jobs = response.json()

        print("Top 5 remote jobs:\n")
        for job in jobs[1:6]:  # skip the first item (metadata)
            print(f"💼 {job['position']} at {job['company']}")
            print(f"🔗 https://remoteok.com{job['url']}")
            print("-" * 40)

    except Exception as e:
        print(f"❌ Failed to fetch jobs: {e}")

if __name__ == "__main__":
    fetch_jobs()
