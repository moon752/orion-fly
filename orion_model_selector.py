import os
import time
import requests
from collections import defaultdict

# Load key from secret env variable
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
if not OPENROUTER_KEY:
    raise EnvironmentError("Missing OPENROUTER_KEY environment variable.")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_KEY}",
    "Content-Type": "application/json"
}

RATE_LIMIT_SECONDS = 1  # Ensure we don't exceed 1 request/second

def rate_limited_request(method, url, **kwargs):
    time.sleep(RATE_LIMIT_SECONDS)
    response = requests.request(method, url, headers=HEADERS, timeout=10, **kwargs)
    response.raise_for_status()
    return response

def fetch_models():
    """Fetch list of free models."""
    url = "https://openrouter.ai/v1/models"
    try:
        response = rate_limited_request("GET", url)
        return response.json().get("data", [])
    except Exception as e:
        print(f"❌ Failed to fetch models: {e}")
        return []

def categorize_models(models):
    """Categorize models based on purpose."""
    categories = defaultdict(list)
    for model in models:
        name = model.get("name", "").lower()
        free = model.get("free", False)
        if not free:
            continue
        if any(kw in name for kw in ["code", "coder", "program"]):
            categories["coding"].append(model)
        elif any(kw in name for kw in ["chat", "gpt", "text", "writer"]):
            categories["writing"].append(model)
        else:
            categories["general"].append(model)
    return categories

current_model_indices = defaultdict(int)

def get_next_model_for_task(categories, task_type="general"):
    """Rotate through models per task type."""
    models = categories.get(task_type, []) or categories.get("general", [])
    if not models:
        raise RuntimeError(f"No models available for task type: {task_type}")
    idx = current_model_indices[task_type]
    current_model_indices[task_type] = (idx + 1) % len(models)
    return models[idx]["name"]

def call_openrouter_model(payload):
    """Call OpenRouter and get response."""
    try:
        response = rate_limited_request(
            "POST",
            "https://openrouter.ai/v1/chat/completions",
            json=payload
        )
        json_resp = response.json()
        if "choices" in json_resp:
            return json_resp["choices"][0]["message"]["content"]
        else:
            raise ValueError("Invalid response: missing 'choices'")
    except Exception as e:
        raise RuntimeError(f"OpenRouter call failed: {e}")

# MAIN FLOW
print("🔍 Fetching available models...")
models = fetch_models()
if not models:
    print("❌ No models found. Exiting.")
    exit(1)

categories = categorize_models(models)
print("✅ Models loaded and categorized:")
for cat, mods in categories.items():
    print(f"  {cat}: {len(mods)}")

task_type = "coding"  # Could be 'writing', 'general'
model = get_next_model_for_task(categories, task_type)
print(f"🚀 Using model: {model} for task: {task_type}")

payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Write Python code to reverse a string."}
    ]
}

response_text = call_openrouter_model(payload)
print("🧠 Model response:")
print(response_text)
