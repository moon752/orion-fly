import random, os, requests

OPENROUTER_KEYS = [
    os.getenv("OPENROUTER_KEY_1"),
    os.getenv("OPENROUTER_KEY_2"),
    os.getenv("OPENROUTER_KEY_3"),
    # Add more keys here if needed
]

def chat_openrouter(messages, model="meta-llama/llama-3.1-70b-instruct:nitro"):
    for key in OPENROUTER_KEYS:
        try:
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://t.me/killbirdbot",
                "X-Title": "ORION",
            }
            data = {
                "model": model,
                "messages": messages,
                "provider": {
                    "sort": "throughput",
                    "allow_fallbacks": True,
                    "require_parameters": False,
                    "data_collection": "deny"
                }
            }
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                print(f"[OpenRouter] Key failed ({key[:10]}): {response.status_code} {response.text}")
        except Exception as e:
            print(f"[OpenRouter] Exception for key {key[:10]}: {e}")
    raise Exception("[ORION] All OpenRouter keys failed.")
