
import os, random, json, time
import requests

GROQ_KEYS = os.getenv("GROQ_KEYS", "").split(",")
FIREWORKS_KEYS = os.getenv("FIREWORKS_KEYS", "").split(",")
HF_KEYS = os.getenv("HF_KEYS", "").split(",")

# Order of fallback
PROVIDERS = [
    ("groq", GROQ_KEYS),
    ("fireworks", FIREWORKS_KEYS),
    ("huggingface", HF_KEYS)
]

def ai(messages, max_tokens=1000, temperature=0.7):
    for provider, keys in PROVIDERS:
        for key in keys:
            try:
                if provider == "groq":
                    return call_groq(key, messages, max_tokens, temperature)
                elif provider == "fireworks":
                    return call_fireworks(key, messages, max_tokens, temperature)
                elif provider == "huggingface":
                    return call_huggingface(key, messages)
            except Exception as e:
                print(f"[{provider}] Failed with key {key[:6]}… — {e}")
    raise RuntimeError("All providers failed")

def call_groq(api_key, messages, max_tokens, temperature):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    body = {
        "model": "mixtral-8x7b-32768",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    r = requests.post(url, json=body, headers=headers, timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def call_fireworks(api_key, messages, max_tokens, temperature):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    body = {
        "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    r = requests.post(url, json=body, headers=headers, timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def call_huggingface(api_key, messages):
    prompt = messages[-1]["content"]
    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    r = requests.post(url, headers=headers, json={"inputs": prompt}, timeout=40)
    r.raise_for_status()
    result = r.json()
    return result[0]["generated_text"] if isinstance(result, list) else result["generated_text"]
