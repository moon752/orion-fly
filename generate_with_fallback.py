import os
import requests
import time
import random

# Load keys from Replit secrets
openrouter_keys = [
    os.getenv("OPENROUTER_KEY_1"),
    os.getenv("OPENROUTER_KEY_2"),
    os.getenv("OPENROUTER_KEY_3")
]
groq_keys = [
    os.getenv("GROQ_KEY_1"),
    os.getenv("GROQ_KEY_2")
]

# Filter out missing keys
openrouter_keys = [k for k in openrouter_keys if k]
groq_keys = [k for k in groq_keys if k]

def generate_with_fallback(prompt):
    # Try OpenRouter keys first
    for key in openrouter_keys:
        response = try_openrouter(prompt, key)
        if response:
            return f"✅ OpenRouter:\\n{response}"
        time.sleep(1)  # to respect 10 reqs / 10 sec

    # Then try Groq
    for key in groq_keys:
        response = try_groq(prompt, key)
        if response:
            return f"✅ Groq:\\n{response}"
        time.sleep(1)

    return "❌ All models failed."

def try_openrouter(prompt, key):
    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-coder:free",
                "messages": [
                    {"role": "system", "content": "You are a helpful freelance assistant."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 400
            },
            timeout=15
        )
        data = res.json()
        return data["choices"][0]["message"]["content"] if "choices" in data else None
    except Exception as e:
        return None

def try_groq(prompt, key):
    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mixtral-8x7b-32768",
                "messages": [
                    {"role": "system", "content": "You are a helpful freelance assistant."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 400
            },
            timeout=15
        )
        data = res.json()
        return data["choices"][0]["message"]["content"] if "choices" in data else None
    except Exception as e:
        return None
