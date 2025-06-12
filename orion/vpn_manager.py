import os
import subprocess

def vpn_connect(country_code="US"):
    print(f"🌐 Connecting VPN to {country_code} via ProtonVPN CLI...")
    subprocess.run(["protonvpn", "connect", "--cc", country_code], check=False)
def vpn_disconnect():
    print("🌐 Disconnecting ProtonVPN...")
    subprocess.run(["protonvpn", "disconnect"], check=False)
