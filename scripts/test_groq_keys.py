
import os, requests, json, time
from dotenv import load_dotenv; load_dotenv()
keys = [k for k in os.getenv("GROQ_KEYS","").split(",") if k]
for k in keys:
    print(f"🔑 Testing {k[:10]}…", end=" ")
    try:
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {k}"},
            json={
                "model":"llama3-8b-8192",       # ✅ safe Groq model
                "stream": False,
                "messages":[{"role":"user","content":"Ping"}],
                "max_tokens":5
            },
            timeout=20
        )
        r.raise_for_status()
        print("🧠", json.loads(r.text)["choices"][0]["message"]["content"].strip())
    except Exception as e:
        print("❌", e)
    time.sleep(1)
