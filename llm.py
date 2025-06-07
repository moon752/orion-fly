import os
import random
import requests
import sseclient

# Free models to rotate
MODELS = [
    "deepseek/deepseek-r1-0528:free",
    "mistralai/mixtral-8x7b-instruct:free",
    "google/gemma-7b-it:free",
]

# Load keys from ENV
API_KEYS = list(filter(None, [
    os.getenv("OPENROUTER_KEY"),
    os.getenv("OPENROUTER_KEY_2"),
    os.getenv("OPENROUTER_KEY_3")
]))

if not API_KEYS:
    raise EnvironmentError("❌ No OpenRouter API keys found.")

def ask_orion(prompt, prefill=None, stream=False):
    for model in MODELS:
        api_key = random.choice(API_KEYS)
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/moon752/orion-fly",
            "X-Title": "ORION Agent"
        }

        messages = []
        if prefill:
            messages.append({"role": "assistant", "content": prefill})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": model,
            "messages": messages,
            "stream": stream
        }

        print(f"🔍 Trying model: {model} | 🔑 Key: {api_key[:10]}...")

        try:
            if stream:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                         headers=headers, json=payload, stream=True, timeout=30)
                client = sseclient.SSEClient(response)
                full_reply = ""
                for event in client.events():
                    if event.data == "[DONE]":
                        break
                    try:
                        chunk = eval(event.data)
                        delta = chunk["choices"][0]["delta"].get("content", "")
                        full_reply += delta
                        print(delta, end="", flush=True)
                    except Exception:
                        pass
                print("\n✅ Done streaming.")
                return full_reply

            else:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                         headers=headers, json=payload, timeout=30)
                response.raise_for_status()
                data = response.json()
                reply = data["choices"][0]["message"]["content"]
                finish_reason = data["choices"][0].get("finish_reason", "unknown")
                print(f"🟢 Finish Reason: {finish_reason}")
                return reply

        except requests.RequestException as err:
            print(f"❌ Error using {model}: {err}")
            continue

    raise RuntimeError("🚨 All models failed. Check network or keys.")

# Example test
if __name__ == "__main__":
    result = ask_orion("What is 9 + 10?", prefill="Sure, the answer is", stream=False)
    print("🧠 ORION says:", result)
