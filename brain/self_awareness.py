import shutil, platform, os, psutil

def check_resources():
    ram = psutil.virtual_memory()
    disk = shutil.disk_usage(".")
    print(f"🧠 RAM: {round(ram.total / 1e9, 2)} GB total, {round(ram.available / 1e9, 2)} GB free")
    print(f"💾 Disk: {round(disk.total / 1e9, 2)} GB total, {round(disk.used / 1e9, 2)} GB used")
    print(f"🖥️ Platform: {platform.system()} — {platform.release()}")

if __name__ == "__main__":
    print("📡 ORION Self-Awareness Check")
    check_resources()

import psutil, shutil, platform
def system_info():
    ram  = psutil.virtual_memory()
    disk = shutil.disk_usage(".")
    return (
        f"🧠 RAM: {round(ram.available/1e9,1)} GB free / {round(ram.total/1e9,1)} GB"
        f"\n💾 Disk: {round(disk.used/1e9,1)} GB used / {round(disk.total/1e9,1)} GB"
        f"\n🖥️ Platform: {platform.system()} {platform.release()}"
    )
