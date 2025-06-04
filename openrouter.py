import requests
import os

# Default model
DEFAULT_MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"

def query_openrouter(prompt, model=DEFAULT_MODEL):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENROUTER_API_KEY in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/moon752/orion-fly",
        "X-Title": "ORION Autonomous Agent",
        "Content-Type": "application/json"
    }

    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are ORION, a skilled freelance AI agent."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code != 200:
        raise RuntimeError(f"OpenRouter API error: {response.text}")

    return response.json()["choices"][0]["message"]["content"]
