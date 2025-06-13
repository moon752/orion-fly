# utils/ai_model.py – ORION AI wrapper (OpenRouter only)

import os, random, requests

OPENROUTER_KEYS = [
    "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",
    "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",
    "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",
    "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",
    "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",
]

def fetch_free_models():
    try:
        key = random.choice(OPENROUTER_KEYS)
        headers = {"Authorization": f"Bearer {key}"}
        res = requests.get("https://openrouter.ai/api/v1/models", headers=headers, timeout=20)
        data = res.json()
        return [m["id"] for m in data if m.get("id") and "free" in m.get("tags", [])]
    except Exception as e:
        return ["deepseek/deepseek-r1-0528-qwen3-8b:free"]  # fallback default

FREE_MODELS = fetch_free_models()

def chat_openrouter(messages, model=None):
    for _ in range(len(OPENROUTER_KEYS)):
        key = random.choice(OPENROUTER_KEYS)
        model = model or random.choice(FREE_MODELS)
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json={"model": model, "messages": messages},
                timeout=30
            )
            if response.status_code == 200:
                data = response.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "[OpenRouter error]")
        except Exception:
            continue
    return "[ORION: All OpenRouter keys failed]"

class ai:
    @staticmethod
    def chat(messages):
        return chat_openrouter(messages)
