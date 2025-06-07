import os
import requests
import time
from collections import deque
from threading import Lock

MAX_REQUESTS = 10
TIME_WINDOW = 10

class RateLimiter:
    def __init__(self):
        self.calls = deque()
        self.lock = Lock()
        
    def allow(self):
        with self.lock:
            now = time.time()
            while self.calls and now - self.calls[0] > TIME_WINDOW:
                self.calls.popleft()
            if len(self.calls) < MAX_REQUESTS:
                self.calls.append(now)
                return True
            return False

openrouter_keys = [os.getenv(f"OPENROUTER_KEY_{i}") for i in range(1, 10)]
groq_keys = [os.getenv(f"GROQ_KEY_{i}") for i in range(1, 10)]

openrouter_keys = [k for k in openrouter_keys if k]
groq_keys = [k for k in groq_keys if k]

openrouter_rate_limiters = {k: RateLimiter() for k in openrouter_keys}
groq_rate_limiters = {k: RateLimiter() for k in groq_keys}

def fetch_openrouter_models(key):
    try:
        res = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers={"Authorization": f"Bearer {key}"}, timeout=10)
        res.raise_for_status()
        data = res.json()
        return [model['name'] for model in data.get('data', [])]
    except Exception as e:
        print(f"[OpenRouter] Failed to fetch models: {e}")
        return []

def fetch_groq_models(key):
    try:
        res = requests.get(
            "https://api.groq.com/openai/v1/models",
            headers={"Authorization": f"Bearer {key}"}, timeout=10)
        res.raise_for_status()
        data = res.json()
        return [model['id'] for model in data.get('data', [])]
    except Exception as e:
        print(f"[Groq] Failed to fetch models: {e}")
        return []

openrouter_models = []
for key in openrouter_keys:
    models = fetch_openrouter_models(key)
    if models:
        openrouter_models = models
        break

groq_models = []
for key in groq_keys:
    models = fetch_groq_models(key)
    if models:
        groq_models = models
        break

def can_call_api(key, limiters):
    return limiters[key].allow()

def try_openrouter(prompt, key, model):
    if not can_call_api(key, openrouter_rate_limiters):
        print(f"[OpenRouter] Rate limit hit for key {key[:8]}...")
        return None
    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful freelance assistant."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 400
            }, timeout=15)
        data = res.json()
        if res.status_code == 200 and "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            print(f"[OpenRouter] API error: {data.get('error', data)}")
            return None
    except Exception as e:
        print(f"[OpenRouter] Exception: {e}")
        return None

def try_groq(prompt, key, model):
    if not can_call_api(key, groq_rate_limiters):
        print(f"[Groq] Rate limit hit for key {key[:8]}...")
        return None
    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful freelance assistant."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 400
            }, timeout=15)
        data = res.json()
        if res.status_code == 200 and "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            print(f"[Groq] API error: {data.get('error', data)}")
            return None
    except Exception as e:
        print(f"[Groq] Exception: {e}")
        return None

def generate_with_fallback(prompt):
    for key in openrouter_keys:
        for model in openrouter_models:
            response = try_openrouter(prompt, key, model)
            if response:
                return f"✅ OpenRouter [{model}]:\n{response}"
            time.sleep(1)
    for key in groq_keys:
        for model in groq_models:
            response = try_groq(prompt, key, model)
            if response:
                return f"✅ Groq [{model}]:\n{response}"
            time.sleep(1)
    return "❌ All models failed or rate limits hit."

if __name__ == "__main__":
    print(generate_with_fallback("What's the best way to automate freelance work with AI?"))
