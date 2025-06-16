
import os, requests, time, random, datetime

# Load keys from environment (Replit Secrets / Railway Variables)
GROQ_KEYS     = [k for k in os.getenv("GROQ_KEYS","").split(",") if k]
FIRE_KEYS     = [k for k in os.getenv("FIREWORKS_KEYS","").split(",") if k]
HF_KEYS       = [k for k in os.getenv("HF_KEYS","").split(",") if k]
TOGETHER_KEY  = os.getenv("TOGETHER_API_KEY","")

# Simple per‑key throttle — one call per second
_LAST_HIT = {}

def _throttle(key):
    now = time.time()
    if key in _LAST_HIT and now - _LAST_HIT[key] < 1.0:
        time.sleep(1.0 - (now - _LAST_HIT[key]))
    _LAST_HIT[key] = time.time()

# ------------- Provider Calls -----------------
def _call_groq(key, messages, temp):
    _throttle(key)
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model":"mixtral-8x7b-32768","messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def _call_fire(key, messages, temp):
    _throttle(key)
    r = requests.post(
        "https://api.fireworks.ai/inference/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model":"accounts/fireworks/models/mixtral-8x7b-instruct",
              "messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def _call_together(messages, temp):
    if not TOGETHER_KEY:
        raise RuntimeError("No Together key set")
    _throttle(TOGETHER_KEY)
    r = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={"Authorization": f"Bearer {TOGETHER_KEY}"},
        json={"model":"mistralai/Mixtral-8x7B-Instruct-v0.1",
              "messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def _call_hf(key, messages):
    _throttle(key)
    r = requests.post(
        "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        headers={"Authorization": f"Bearer {key}"},
        json={"inputs": messages[-1]["content"]},
        timeout=40)
    r.raise_for_status()
    data = r.json()
    return data[0]["generated_text"] if isinstance(data, list) else data["generated_text"]

# ------------- Master Router ------------------
def ai(messages, temperature=0.7):
    # 1) Groq
    for k in GROQ_KEYS:
        try: return _call_groq(k, messages, temperature)
        except Exception as e: print("[groq]", e)

    # 2) Fireworks
    for k in FIRE_KEYS:
        try: return _call_fire(k, messages, temperature)
        except Exception as e: print("[fw]", e)

    # 3) Together
    try:
        return _call_together(messages, temperature)
    except Exception as e:
        print("[together]", e)

    # 4) Hugging Face
    for k in HF_KEYS:
        try: return _call_hf(k, messages)
        except Exception as e: print("[hf]", e)

    # 5) Local stub (never fails)
    now = datetime.datetime.utcnow().isoformat()
    print("⚠️  All providers failed — returning stub.")
    return f"# Stub generated {now}\nprint('ORION local stub reply')"
