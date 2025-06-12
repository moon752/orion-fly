from orion.brain.driver import get_driver
from orion.utils.stealth import random_cookie_session
from orion.brain.delay import human_delay
from orion.brain.platform_knowledge import get_platform_intel

driver = get_driver()
driver.get("https://freelancer.com/login")
random_cookie_session(driver)
human_delay("login")
intel = get_platform_intel("freelancer")
print("[+] Platform Knowledge:", intel)
driver.quit()
