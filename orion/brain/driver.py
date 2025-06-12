from xvfbwrapper import Xvfb
import undetected_chromedriver.v2 as uc
from orion.utils.stealth import inject_stealth_headers
from orion.utils.proxy import get_random_proxy

def get_driver():
    vdisplay = Xvfb()
    vdisplay.start()
    options = uc.ChromeOptions()

    proxy = get_random_proxy()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)
    inject_stealth_headers(driver)
    return driver
