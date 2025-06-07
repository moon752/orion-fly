
import os
import requests

key = os.getenv("OPENROUTER_KEY_1")  # Make sure this is set in your env

try:
    res = requests.get(
        "https://openrouter.ai/api/v1/models",
        headers={"Authorization": f"Bearer {key}"},
        timeout=10
    )
    res.raise_for_status()
    models = res.json().get("data", [])
    print("✅ Free OpenRouter models:")
    for m in models:
        if "(free)" in m.get("description", "").lower() or "free" in m.get("name", "").lower():
            print("-", m["name"])
except Exception as e:
    print("❌ Error fetching models:", e)

