import random, time
from fake_useragent import UserAgent
from functools import wraps
import backoff

def human_delay(min_sec=2, max_sec=5):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def backoff_handler(details):
    print(f"[!] Retrying after error: {details['exception']}")

def retry_on_exception(exception):
    return backoff.on_exception(
        backoff.expo,
        exception,
        max_tries=5,
        on_backoff=backoff_handler
    )

def random_cookie_session(driver):
    import uuid
    session_id = str(uuid.uuid4())
    driver.delete_all_cookies()
    driver.add_cookie({"name": "session_id", "value": session_id})
