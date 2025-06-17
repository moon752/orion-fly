
import os, time, requests, json
from dotenv import load_dotenv; load_dotenv()
keys=[k for k in os.getenv("FIREWORKS_KEYS","").split(",") if k]
models=["llama-v3-8b-instruct","mixtral-8x7b-instruct","starcoder2-15b"]
for k in keys:
    for m in models:
        try:
            r=requests.post("https://api.fireworks.ai/v1/chat/completions",
                headers={"Authorization":f"Bearer {k}"},
                json={"model":m,"messages":[{"role":"user","content":"Ping"}],
                      "max_tokens":5,"stream":False},
                timeout=20)
            r.raise_for_status()
            print(f"🔑{k[:8]} {m:22} 🧠",
                  json.loads(r.text)["choices"][0]["message"]["content"].strip())
        except Exception as e:
            print(f"🔑{k[:8]} {m:22} ❌",e)
        time.sleep(1)
