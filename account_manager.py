from vpn_manager import rotate_vpn
from utils.telegram import send_telegram_message

ACCOUNTS = [
    {"email": "lara.aiwriter@gmail.com", "platform": "freelancer", "vpn": "US"},
    {"email": "alpha.dev@pm.me", "platform": "freelancer", "vpn": "UK"},
    {"email": "neon.writer@protonmail.com", "platform": "freelancer", "vpn": "CA"},
    {"email": "droid.ghost@tutanota.com", "platform": "freelancer", "vpn": "DE"},
    {"email": "orion.core@pm.me", "platform": "freelancer", "vpn": "AU"},
]

def login_all_accounts():
    for acc in ACCOUNTS:
        send_telegram_message(f"🔁 Switching VPN for {acc['email']}")
        rotate_vpn(method="proton", region=acc['vpn'])
        send_telegram_message(f"🔐 Ready to log in to {acc['platform']} as {acc['email']}")

def rotate_and_apply_all():
    for acc in ACCOUNTS:
        rotate_vpn(method="proton", region=acc['vpn'])
        send_telegram_message(f"🚀 Job apply logic ready for {acc['email']} (stub mode)")
