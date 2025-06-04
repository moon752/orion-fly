import requests

API_KEY = "sk-or-v1-0e41a5b878301552f4c0"  # replace with your actual OpenRouter key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://github.com/moon752/orion-fly",
    "X-Title": "ORION",
    "Content-Type": "application/json"
}

MODELS = [
    "microsoft/phi-4-reasoning-plus",
    "deepseek/deepseek-prover-v2",
    "qwen/qwen3-14b",
    "nvidia/llama-3.1-nemotron-ultra-253b-v1"
]

def try_model(model, prompt):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            print(f"[✅ {model}]: {reply}")
            return True
        else:
            print(f"[💥 ERROR] {model}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[💥 ERROR] {model}: {e}")
        return False

if __name__ == "__main__":
    prompt = "What is the future of AI in business?"
    for model in MODELS:
        if try_model(model, prompt):
            break
    else:
        print("[❌ All models failed]")
