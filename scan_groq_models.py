
import os
import requests

groq_keys = [os.getenv("GROQ_KEY_1"), os.getenv("GROQ_KEY_2")]
groq_models = ["mixtral-8x7b-32768", "llama3-70b-8192", "gemma-7b-it"]

for key in filter(None, groq_keys):  # skip None keys
    for model in groq_models:
        try:
            res = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": "ping"}],
                    "max_tokens": 5
                },
                timeout=10
            )
            if res.status_code == 200:
                print(f"✅ Available: {model}")
            else:
                print(f"❌ Not available: {model} ({res.status_code})")
        except Exception as e:
            print(f"⚠️ Error testing {model}: {e}")

