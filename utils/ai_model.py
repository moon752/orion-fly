"""
utils/ai_model.py – ORION unified AI wrapper

• Rotates through all stored OpenRouter keys
• Loads free‑model list at runtime from orion/data/free_models.json
• Falls back to Groq if OpenRouter fails
"""

import json, random, requests, pathlib

# --- API KEYS -------------------------------------------------------------
OPENROUTER_KEYS = [
    # NEW KEYS FIRST
    "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",
    "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",
    # EXISTING
    "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",
    "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",
    "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"
]

GROQ_KEYS = [
    "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",
    "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"
]

# --- MODEL LIST ----------------------------------------------------------
def load_free_models():
    fp = pathlib.Path("orion/data/free_models.json")
    if fp.exists():
        try:
            return json.loads(fp.read_text())
        except Exception:
            pass
    # fallback minimal list
    return [
        "openchat/openchat-3.5-1210",
        "mistralai/mistral-7b-instruct",
        "deepseek/deepseek-prover-v2"
    ]

# --- CHAT FUNCTIONS ------------------------------------------------------
def chat_openrouter(messages, model=None):
    key   = random.choice(OPENROUTER_KEYS)
    model = model or random.choice(load_free_models())
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model": model, "messages": messages},
        timeout=40
    )
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]

def chat_groq(messages, model="mixtral-8x7b-32768"):
    key = random.choice(GROQ_KEYS)
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model": model, "messages": messages},
        timeout=40
    )
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]

# --- Public shim ---------------------------------------------------------
class ai:
    @staticmethod
    def chat(messages):
        try:
            return chat_openrouter(messages)
        except Exception:
            return chat_groq(messages)  # last‑chance fallback
