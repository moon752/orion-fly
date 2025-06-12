from utils.telegram import send_telegram_message

def connect_windscribe():
    send_telegram_message("✅ Windscribe VPN connected (dummy).")

def connect_protonvpn(region_code="US"):
    send_telegram_message(f"✅ ProtonVPN connected to {region_code} (dummy).")

def rotate_vpn(method="windscribe", region="US"):
    if method == "windscribe":
        connect_windscribe()
    elif method == "proton":
        connect_protonvpn(region_code=region)
    else:
        send_telegram_message("⚠️ Unknown VPN method.")
