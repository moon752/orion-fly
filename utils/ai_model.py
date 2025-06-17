
"""ORION LLM wrapper: Groq primary, Together fallback."""
import os, time, random, requests

# === KEYS ===
GROQ_KEYS = [k for k in os.getenv("GROQ_KEYS", "").split(",") if k]
TOGETHER_KEY = os.getenv("TOGETHER_API_KEY")

# === Simple throttle (1 req/sec per key) ===
_last_hit = {}
def _throttle(key):
    now = time.time()
    if key in _last_hit and now - _last_hit[key] < 1:
        time.sleep(1 - (now - _last_hit[key]))
    _last_hit[key] = time.time()

# === Groq call ===
def _call_groq(key, messages, temp):
    _throttle(key)
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": "mixtral-8x7b-32768",
            "messages": messages,
            "temperature": temp,
            "stream": False,
            "max_tokens": 512
        },
        timeout=40
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

# === Together call ===
def _call_together(messages, temp, model="llama-2-70b-chat"):
    r = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={"Authorization": f"Bearer {TOGETHER_KEY}"},
        json={
            "model": model,
            "messages": messages,
            "temperature": temp,
            "max_tokens": 512,
            "stream": False
        },
        timeout=40
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

# === Public helper ===
def smart_chat(messages, temp=0.7):
    # 1) Groq rotation
    for k in GROQ_KEYS:
        try:
            return _call_groq(k, messages, temp)
        except Exception:
            continue
    # 2) Together fallback
    if TOGETHER_KEY:
        return _call_together(messages, temp)
    raise RuntimeError("All providers failed (Groq & Together)")
