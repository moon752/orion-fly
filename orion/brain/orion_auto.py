import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from orion.brain.driver import get_driver
from orion.utils.stealth import random_cookie_session
from orion.brain.delay import human_delay
from orion.brain.earnings import log_earning, get_daily_total
from orion.brain.scheduler import get_next_login_time
from orion.brain.storage import save_session, backup_all

def orion_autopilot(platform, account_id, earning=500):
    driver = get_driver()
    driver.get(f"https://{platform}.com/login")
    random_cookie_session(driver)
    human_delay("login")

    # Simulate login and work
    print(f"[+] Logged in to {platform} as {account_id}")
    human_delay("click")

    # Track earnings
    log_earning(platform, earning)
    print(f"[💸] Logged ${earning} earning on {platform}")

    # Save session
    save_session(account_id, driver)
    driver.quit()

    # Backup
    backup_all()

    # Next run time
    print("[🕑] Next login scheduled at:", get_next_login_time())
    print("[📊] Total earned today:", get_daily_total())

# Example call
orion_autopilot("freelancer", "lara.aiwriter")
