import os
from dotenv import load_dotenv

load_dotenv()

SECRETS_FILE = ".env"

def save_secret(key, value):
    with open(SECRETS_FILE, "a") as f:
        f.write(f"\n{key}={value}")
    os.environ[key] = value
