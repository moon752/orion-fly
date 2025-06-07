import os
import time
import requests
import random

# Load keys from environment (stored in Replit secrets or system ENV)
api_keys = list(filter(None, [
    os.getenv("OPENROUTER_KEY"),
    os.getenv("OPENROUTER_KEY_2"),
    os.getenv("OPENROUTER_KEY_3")
]))

if not api_keys:
    raise EnvironmentError("❌ No OpenRouter API keys found in environment.")

# Randomly select a key for this request
api_key = random.choice(api_keys)

# Set model here (can rotate or randomize if needed)
model = "deepseek/deepseek-r1-0528:free"  # ✅ free & working
# model = "mistralai/mixtral-8x7b-instruct:free"  # another free option

# Build headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/moon752/orion-fly",  # Required by OpenRouter
    "X-Title": "ORION Agent"
}

# Build payload
payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": "What is 9 + 10?"}
    ]
}

try:
    print(f"🟡 Testing model: {model}")
    print(f"🔑 Using key: {api_key[:10]}...")

    # POST to OpenRouter
    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers, json=payload, timeout=15)
    response.raise_for_status()

    # Parse response
    data = response.json()
    if "choices" in data and data["choices"]:
        reply = data["choices"][0]["message"]["content"]
        print("🟢 Model replied:")
        print(reply)
    else:
        print("⚠️ Unexpected response format:")
        print(data)

except requests.exceptions.RequestException as req_err:
    print(f"❌ Request error: {req_err}")
    try:
        print(f"📩 Response: {response.text}")
    except:
        pass
except Exception as err:
    print(f"❌ General error: {err}")
