from orion.core.secrets_manager import update_secret_store
import json

def handle_admin_command(text):
    try:
        if not text.startswith("#adminlink"):
            return "[ORION] Not an admin command."

        data_str = text.replace("#adminlink", "").strip()
        data_json = json.loads(data_str)

        update_secret_store(data_json)
        return "[ORION] 🔐 Secrets updated successfully."

    except Exception as e:
        return f"[ORION ERROR] Could not update secrets: {str(e)}"
