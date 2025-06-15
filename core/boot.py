import sys
import os
sys.path.append(os.path.abspath("."))
import psutil
import platform
from utils.ai_model import ai

def check_llm():
    try:
        reply = ai([{"role": "user", "content": "Say LLM OK"}])
        if not reply:
            return "❌ LLM returned no response."
        return "🧠 LLM: OK" if "OK" in reply else f"⚠️ LLM unexpected: {reply[:30]}"
    except Exception as e:
        return f"❌ LLM ERROR — {e}"

# System info
def get_system_status():
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    os_info = platform.platform()
    return (
        f"🧠 RAM: {round(ram.available / 1e9, 1)} GB free / {round(ram.total / 1e9, 1)} GB\n"
        f"💾 Disk: {round(disk.used / 1e9, 1)} GB used / {round(disk.total / 1e9, 1)} GB\n"
        f"🖥️ Platform: {os_info}"
    )

print("⚙️ ORION Booted")
print(get_system_status())
print(check_llm())
