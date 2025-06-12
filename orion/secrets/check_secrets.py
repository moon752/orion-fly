import json
import os

json_paths = [
    "orion/secrets/.secrets.json",
    "orion/secret_data.json"
]

required_fields = {
    "orion/secrets/.secrets.json": [
        "TELEGRAM_BOT_TOKEN", "OPENROUTER_KEYS", "GROQ_KEYS", "PAYMENT_METHODS"
    ],
    "orion/secret_data.json": [
        "freelancer", "fiverr", "guru", "workana", "openrouter_keys"
    ]
}

missing = {}

for path in json_paths:
    if not os.path.exists(path):
        missing[path] = ["❌ File not found"]
        continue

    with open(path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            missing[path] = ["❌ Invalid JSON format"]
            continue

    path_missing = []
    for key in required_fields[path]:
        if key not in data:
            path_missing.append(f"❌ Missing: {key}")
    if path_missing:
        missing[path] = path_missing

if missing:
    print("🔐 Secrets check FAILED:\n")
    for path, issues in missing.items():
        print(f"File: {path}")
        for issue in issues:
            print("  -", issue)
    exit(1)
else:
    print("✅ All secrets and tokens found. ORION is secure and ready.")
