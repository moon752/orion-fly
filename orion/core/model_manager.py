import itertools
import time

class ModelManager:
    def __init__(self, api_keys, models):
        self.api_keys = api_keys
        self.models = models
        self.key_cycle = itertools.cycle(api_keys)
        self.model_cycle = itertools.cycle(models)
        self.last_call_time = 0

    def get_next(self):
        # Simple rate limiter: max 1 call per 1s (adjust as needed)
        now = time.time()
        if now - self.last_call_time < 1:
            time.sleep(1 - (now - self.last_call_time))
        self.last_call_time = time.time()
        return next(self.key_cycle), next(self.model_cycle)
