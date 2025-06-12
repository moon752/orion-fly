
import requests
import time
import os

API_KEY = os.getenv("CAPTCHA_API_KEY")  # 2Captcha API Key

def solve_recaptcha_v2(site_key, page_url):
    print("🧠 Solving CAPTCHA...")
    url = "http://2captcha.com/in.php"
    params = {
        "key": API_KEY,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": page_url,
        "json": 1
    }
    r = requests.post(url, data=params).json()
    if r["status"] != 1:
        return None
    captcha_id = r["request"]

    for _ in range(30):
        res = requests.get("http://2captcha.com/res.php", params={
            "key": API_KEY,
            "action": "get",
            "id": captcha_id,
            "json": 1
        }).json()
        if res["status"] == 1:
            return res["request"]
        time.sleep(5)

    return None

