# orion_phase8_core.py

# Phase 8: Self-Healing, Self-Upgrading, Self-Research Core

import traceback
import subprocess
import os
from utils.telegram import send_telegram_message
from utils.secret_store import save_secret
from utils.ai_model import query_model  # Wraps OpenRouter or Groq

ERROR_LOG = "orion/logs/errors.log"
PATCH_DIR = "orion/patches"

# --- 1. Error Handler ---
def log_error(e):
    error_text = traceback.format_exc()
    os.makedirs(os.path.dirname(ERROR_LOG), exist_ok=True)
    with open(ERROR_LOG, "a") as f:
        f.write(error_text + "\n")
    send_telegram_message(f"❌ ORION Error:\n{error_text}")
    return error_text

# --- 2. Self-Research (using AI model) ---
def self_research(error_text):
    prompt = f"ORION failed with the following error:\n\n{error_text}\n\nGenerate a patch or fix for this problem in Python."
    return query_model(prompt)

# --- 3. Patch Application Logic ---
def apply_patch(patch_code):
    os.makedirs(PATCH_DIR, exist_ok=True)
    patch_path = os.path.join(PATCH_DIR, "temp_patch.py")
    with open(patch_path, "w") as f:
        f.write(patch_code)
    result = subprocess.run(["python3", patch_path])
    if result.returncode == 0:
        send_telegram_message("✅ Patch applied successfully.")
        return True
    else:
        send_telegram_message("❌ Patch failed during execution.")
        return False

# --- 4. Telegram Secret Injection (/inject KEY=VALUE) ---
def handle_telegram_command(cmd):
    if cmd.startswith("/inject "):
        try:
            key, value = cmd.replace("/inject ", "").split("=", 1)
            save_secret(key.strip(), value.strip())
            send_telegram_message(f"✅ Injected `{key}` successfully.")
        except Exception as e:
            log_error(e)

# --- Main simulation for test ---
if __name__ == "__main__":
    try:
        raise RuntimeError("Simulated ORION crash in test phase.")
    except Exception as e:
        error_info = log_error(e)
        fix_code = self_research(error_info)
        apply_patch(fix_code)
