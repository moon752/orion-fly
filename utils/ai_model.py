import random, os, requests

OPENROUTER_KEYS = [
    os.getenv("OPENROUTER_KEY_1"),
    os.getenv("OPENROUTER_KEY_2"),
    os.getenv("OPENROUTER_KEY_3"),
    # Add more keys here if needed
]


def chat_openrouter(messages, model="deepseek/deepseek-prover-v2"):
    import os, requests, random
    key = os.getenv("OPENROUTER_API_KEY") or random.choice([k for k in OPENROUTER_KEYS if k])
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": model,
        "messages": messages,
        "provider": { "sort": "throughput" }
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body, timeout=40)
    if r.status_code != 200:
        print(f"[OpenRouter ERROR] {r.status_code}: {r.text[:120]}")
        return None
    data = r.json()
    if "choices" not in data:
        print(f"[OpenRouter Missing Choices] {data}")
        return None
    return data["choices"][0]["message"]["content"]
            else:
                print(f"[OpenRouter] Key failed ({key[:10]}): {response.status_code} {response.text}")
        except Exception as e:
            print(f"[OpenRouter] Exception for key {key[:10]}: {e}")
    raise Exception("[ORION] All OpenRouter keys failed.")
ai = chat_openrouter
