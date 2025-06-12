import os
import shutil
from datetime import datetime

SESSION_DIR = "orion/storage/sessions"

def save_session(account_id, driver):
    folder = os.path.join(SESSION_DIR, account_id)
    if not os.path.exists(folder):
        os.makedirs(folder)
    driver.save_screenshot(os.path.join(folder, "session.png"))

def backup_all():
    backup_dir = "orion/storage/backups/" + datetime.now().strftime("%Y-%m-%d_%H-%M")
    shutil.copytree("orion/storage", backup_dir)
