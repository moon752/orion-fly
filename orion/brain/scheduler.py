import datetime
import random

def get_next_login_time():
    now = datetime.datetime.now()
    hour = random.randint(6, 22)
    minute = random.randint(0, 59)
    next_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if next_time < now:
        next_time += datetime.timedelta(days=1)
    return next_time
