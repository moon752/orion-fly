import random, time
from orion.utils.telegram_notify import notify_admin
from orion.keys.api_keys import OPENROUTER_KEYS, GROQ_KEYS

api_state = {
    "openrouter": {"keys": OPENROUTER_KEYS.copy(), "current": 0},
    "groq": {"keys": GROQ_KEYS.copy(), "current": 0}
}

def get_next_key(provider):
    keys = api_state[provider]["keys"]
    current = api_state[provider]["current"]
    api_state[provider]["current"] = (current + 1) % len(keys)
    return keys[api_state[provider]["current"]]

def estimate_tokens(job_text):
    # Basic estimate: 1 token per 4 characters
    return max(100, int(len(job_text) / 4))

def select_best_key(job_text):
    needed = estimate_tokens(job_text)
    for provider in ["openrouter", "groq"]:
        keys = api_state[provider]["keys"]
        for key in keys:
            if simulate_quota_check(key, needed):
                notify_admin(f"🔑 Using {provider.upper()} key ending in {key[-6:]}")
                return provider, key
    notify_admin("❌ No keys available for job size.")
    raise Exception("API Exhausted")

def simulate_quota_check(key, needed_tokens):
    # In future: call quota endpoint
    # For now: assume every key can do 5x 500-token jobs
    return needed_tokens <= 500

def rotate_on_failure(provider):
    old = api_state[provider]["current"]
    new = (old + 1) % len(api_state[provider]["keys"])
    api_state[provider]["current"] = new
    notify_admin(f"🔁 Rotated {provider.upper()} key from {old} to {new}")
    return api_state[provider]["keys"][new]
