import os, requests, time, re
from collections import deque
from dotenv import load_dotenv
load_dotenv()

OR_KEYS    = os.getenv("OPENROUTER_KEYS","").split(",")
GROQ_KEYS  = os.getenv("GROQ_KEYS","").split(",")
OR_MODEL   = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-coder:free")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")
RPM_LIMIT  = int(os.getenv("OPENROUTER_RPM", "30"))  # safe limit per key

timestamp_queue = deque(maxlen=RPM_LIMIT)

def _rate_limit_sleep():
    if len(timestamp_queue) == RPM_LIMIT:
        delta = time.time() - timestamp_queue[0]
        if delta < 60:
            time.sleep(60 - delta)

def _strip(text):
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    if "```" in text:
        parts = re.findall(r"```(?:python)?(.*?)```", text, re.S)
        if parts:
            return parts[0].strip()
    return text.strip()


def query_model(prompt, retries=3):
    # 1) GROQ first
    for _ in range(retries):
        for key in [k.strip() for k in GROQ_KEYS if k.strip()]:
            try:
                r = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                    json={"model": GROQ_MODEL,"messages":[{"role":"user","content":prompt}]},
                    timeout=45
                )
                if r.status_code==200 and "choices" in r.json():
                    return _strip(r.json()["choices"][0]["message"]["content"])
            except Exception: pass
    # 2) OpenRouter fallback (rate‑limited)
    for _ in range(retries):
        for key in [k.strip() for k in OR_KEYS if k.strip()]:
            _rate_limit_sleep()
            try:
                r = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                    json={"model": OR_MODEL,"messages":[{"role":"user","content":prompt}]},
                    timeout=45
                )
                if r.status_code==200 and "choices" in r.json():
                    timestamp_queue.append(time.time())
                    return _strip(r.json()["choices"][0]["message"]["content"])
            except Exception: pass
    return "# all keys failed"
"
