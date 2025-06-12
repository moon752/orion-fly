import random
import time
from selenium.webdriver.chrome.webdriver import WebDriver

def random_user_agent():
    return random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
        "Mozilla/5.0 (X11; Linux x86_64)...",
    ])

def random_cookie_session(driver: WebDriver):
    # Fake cookies for stealth (example cookies)
    fake_cookies = [
        {"name": "sessionid", "value": str(random.randint(100000,999999)), "domain": ".com"},
        {"name": "auth_token", "value": "token_" + str(random.randint(1000,9999)), "domain": ".com"},
    ]
    for cookie in fake_cookies:
        try:
            driver.add_cookie(cookie)
        except Exception:
            pass  # Happens if you're not on a valid domain yet

    time.sleep(random.uniform(2, 5))  # Simulate human delay

def inject_stealth_headers(driver: WebDriver):
    user_agent = random_user_agent()
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
