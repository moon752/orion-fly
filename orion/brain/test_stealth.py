from orion.brain.driver import get_driver
from orion.utils.stealth import random_cookie_session
import time

driver = get_driver()
driver.get("https://someplatform.com/login")

# Simulate stealth session
random_cookie_session(driver)
print("[+] Cookie session randomized.")

# Delay to simulate human activity
time.sleep(5)
print("[+] Done sleeping. Ready for next step.")
driver.quit()
