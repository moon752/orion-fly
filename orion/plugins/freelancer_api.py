import requests

class FreelancerAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.freelancer.com/api"

    def search_jobs(self, query):
        # example endpoint (adjust as per real API docs)
        url = f"{self.base_url}/projects/0.1/projects/active"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def submit_proposal(self, project_id, proposal_text, bid):
        url = f"{self.base_url}/projects/0.1/projects/{project_id}/bids"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"description": proposal_text, "bid": bid}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    # Add messaging, milestones etc similarly
