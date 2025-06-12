import random
import time

def human_delay(action="default"):
    delays = {
        "login": (3, 7),
        "click": (1, 3),
        "scroll": (2, 5),
        "default": (4, 8)
    }
    delay_range = delays.get(action, delays["default"])
    delay = random.uniform(*delay_range)
    print(f"[Delay] Sleeping for {delay:.2f}s for {action}")
    time.sleep(delay)
