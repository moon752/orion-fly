# ORION startup sequence (Phase 20)
import os
from utils.ai_model import ai
from utils.telegram import send_telegram
from brain.self_awareness import system_info

def check_llm():
    try:
        reply = ai.chat([{"role":"user","content":"Say LLM OK"}])
        return "🧠 LLM: OK" if "OK" in reply else f"⚠️ LLM unexpected: {reply[:30]}"
    except Exception as e:
        return f"❌ LLM ERROR — {str(e)[:60]}"

def boot():
    msg = (
        "⚙️ ORION Booted\n"
        f"{system_info()}\n"
        f"{check_llm()}\n"
        f"Admin Mode: {'ACTIVE' if os.getenv('ORION_ADMIN_SECRET') else 'DISABLED'}"
    )
    send_telegram(msg)
    print(msg)

if __name__ == "__main__":
    boot()
