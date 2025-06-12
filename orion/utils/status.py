import time, platform

def get_system_status():
    return f"""
🛰️ Platform: {platform.system()}
📦 Time: {time.ctime()}
🧠 Running: True
"""
