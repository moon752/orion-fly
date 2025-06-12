import os
import importlib.util
import json

FILES_TO_CHECK = [
    "orion/core/secrets_manager.py",
    "orion/telegram_bot.py",
    "orion/modules/admin_link_handler.py",
    "orion/secrets/.secrets.json"
]

MODULES_TO_IMPORT = [
    "orion.core.secrets_manager",
    "orion.telegram_bot",
    "orion.modules.admin_link_handler"
]

SECRETS_PATH = "orion/secrets/.secrets.json"

def check_files():
    print("=== Checking Required Files ===")
    all_good = True
    for f in FILES_TO_CHECK:
        if os.path.isfile(f):
            size = os.path.getsize(f)
            if size > 10:
                print(f"[OK] File exists and size >10 bytes: {f}")
            else:
                print(f"[WARN] File exists but size too small (<10 bytes): {f}")
                all_good = False
        else:
            print(f"[MISSING] File not found: {f}")
            all_good = False
    print()
    return all_good

def try_import(module_name):
    print(f"=== Importing module: {module_name} ===")
    try:
        importlib.import_module(module_name)
        print(f"[OK] Imported {module_name} successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to import {module_name}: {e}")
        return False

def check_modules():
    all_good = True
    for mod in MODULES_TO_IMPORT:
        if not try_import(mod):
            all_good = False
    print()
    return all_good

def check_secrets():
    print("=== Checking secrets loading ===")
    try:
        from orion.core.secrets_manager import load_secrets
        secrets = load_secrets()
        if not secrets:
            print("[WARN] Secrets loaded but empty")
            return False
        else:
            print(f"[OK] Secrets loaded with keys: {list(secrets.keys())}")
            if "TELEGRAM_BOT_TOKEN" in secrets:
                print(f"[OK] TELEGRAM_BOT_TOKEN found in secrets")
            else:
                print(f"[MISSING] TELEGRAM_BOT_TOKEN missing in secrets")
                return False
            return True
    except Exception as e:
        print(f"[ERROR] Exception while loading secrets: {e}")
        return False

def main():
    print("=== ORION Project Verification Script ===\n")

    files_ok = check_files()
    modules_ok = check_modules()
    secrets_ok = check_secrets()

    print("=== SUMMARY ===")
    if files_ok and modules_ok and secrets_ok:
        print("[SUCCESS] All checks passed! Ready to proceed.")
    else:
        print("[FAIL] Some checks failed. Fix the above errors before continuing.")

if __name__ == "__main__":
    main()
