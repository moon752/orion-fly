import requests

def fetch_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers)
        jobs = res.json()[1:]  # Skip first metadata item
        return jobs[:10]  # Limit to first 10 for now
    except Exception as e:
        return []
