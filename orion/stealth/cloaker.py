import random
import time
from orion.utils.telegram_notify import notify_admin

def random_typing_delay(min_delay=0.1, max_delay=0.3):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

def random_profile_description():
    templates = [
        "Experienced AI engineer with a passion for automation and clean code.",
        "Seasoned freelancer with 5+ years in Python, AI, and backend systems.",
        "Detail-oriented developer skilled in AI, chatbots, and web scraping.",
        "Professional coder delivering high-quality work in automation and AI.",
        "AI & data wizard available for quick turnarounds and complex tasks.",
    ]
    return random.choice(templates)

def cloak_identity(account_id):
    notify_admin(f"🕵️ Cloaking identity for {account_id}...")
    time.sleep(1)
    new_bio = random_profile_description()
    notify_admin(f"🪄 Bio updated for {account_id}: {new_bio}")
    time.sleep(1)
    notify_admin(f"✅ Anti-detection protocol active for {account_id}")

def stealth_check_cycle():
    notify_admin("🔍 ORION Cloaking Monitor Active")
    while True:
        time.sleep(600)
        notify_admin("🕶️ Stealth mode is running normally.")
