import json
import os

SECRETS_PATH = "orion/secrets/.secrets.json"

def load_secrets():
    """Loads secrets from the JSON file."""
    if not os.path.exists(SECRETS_PATH):
        return {}

    with open(SECRETS_PATH, "r") as f:
        return json.load(f)

def update_secret_store(new_data):
    """Updates or creates the secrets JSON file."""
    secrets = load_secrets()
    secrets.update(new_data)

    os.makedirs(os.path.dirname(SECRETS_PATH), exist_ok=True)
    with open(SECRETS_PATH, "w") as f:
        json.dump(secrets, f, indent=2)

    return True
