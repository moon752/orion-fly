"""
Phase 8 – Self‑Healing, Self‑Upgrading Core (Clean Build)
• Logs errors, sends to Telegram
• Uses utils.ai_model.query_model (OpenRouter + Groq)
• Cleans AI patches (strips diff/markdown) before execution
• Rotates keys & obeys RPM limit via utils.ai_model
"""

import os, traceback, subprocess, time, json
from utils.telegram import send_telegram_message
from utils.ai_model import query_model
from utils.secret_store import save_secret

PATCH_DIR  = "orion/patches"
ERROR_LOG  = "orion/logs/errors.log"
os.makedirs(PATCH_DIR, exist_ok=True)
os.makedirs(os.path.dirname(ERROR_LOG), exist_ok=True)

# ── Error handling ────────────────────────────────────────────
def log_error(exc: Exception) -> str:
    txt = traceback.format_exc()
    with open(ERROR_LOG, "a") as f: f.write(f"{time.ctime()}\\n{txt}\\n")
    send_telegram_message(f"❌ ORION Error:\\n{txt}")
    return txt

# ── Patch cleaner & executor ──────────────────────────────────
def clean_patch(code: str) -> str:
    cleaned = []
    for ln in code.splitlines():
        ln_strip = ln.lstrip()
        if ln_strip.startswith(("```", "@@", "+", "- ", "-\t", "---", "+++")):
            continue
        cleaned.append(ln)
    return "\n".join(cleaned)

def apply_patch(patch_code: str) -> bool:
    patch_code = clean_patch(patch_code)

if not patch_code.strip() or patch_code.strip().startswith("#"):
    send_telegram_message("❌ Patch skipped — empty or comment‑only.")
    return False

    path = os.path.join(PATCH_DIR, "temp_patch.py")
    with open(path, "w") as f: f.write(patch_code)
    res = subprocess.run(["python3", path])
    if res.returncode == 0:
        send_telegram_message("✅ Patch applied successfully.")
        return True
    send_telegram_message("❌ Patch failed – invalid Python.")
    return False

# ── Telegram secret injection (/inject KEY=VALUE) ─────────────
def handle_telegram(cmd: str):
    if cmd.startswith("/inject "):
        try:
            k, v = cmd[8:].split("=", 1)
            save_secret(k.strip(), v.strip())
            send_telegram_message(f"✅ Secret `{k}` stored.")
        except Exception as e:
            log_error(e)

# ── MAIN test block ───────────────────────────────────────────
if __name__ == "__main__":
    try:
# raise RuntimeError("Simulated ORION crash (Phase 8 test).")
    except Exception as e:
        err = log_error(e)
        patch = query_model(f"Fix this Python error:\n{err}\nReturn a full patch file.")
        apply_patch(patch)
