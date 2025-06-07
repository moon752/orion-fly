import requests

api_key = "sk-or-v1-your_actual_working_key_here"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek/deepseek-r1-0528:free",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": False
}

res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
print("Status:", res.status_code)
print("Body:", res.text)
