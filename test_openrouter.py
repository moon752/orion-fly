import os
import requests

key = os.getenv("OPENROUTER_KEY_1")

res = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "deepseek/deepseek-coder:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        "max_tokens": 20
    }
)

print(res.status_code)
print(res.text)

