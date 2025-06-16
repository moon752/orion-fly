"""
Unified AI wrapper for ORION
Providers (free‐tier rotation):
• Fireworks AI (fw_…)
• Hugging Face Inference Endpoints (hf_…)
• Generic alt keys (HBg…, cye…)
• Groq fallback
Rate-limit: 1 req/sec per key
"""
\1
# --- Load keys from environment (Replit Secrets / Railway Variables) ---
GROQ_KEYS = os.getenv("GROQ_KEYS", "").split(",")
FIREWORKS_KEYS = os.getenv("FIREWORKS_KEYS", "").split(",")
HF_KEYS = os.getenv("HF_KEYS", "").split(",")


FIRE_KEYS = [k.strip() for k in os.getenv("FIREWORKS_KEYS","").split(",") if k.strip()]
HF_KEYS   = [k.strip() for k in os.getenv("HF_KEYS","").split(",") if k.strip()]
ALT_KEYS  = [k.strip() for k in os.getenv("ALT_KEYS","").split(",") if k.strip()]
GROQ_KEYS = [k.strip() for k in os.getenv("GROQ_KEYS","").split(",") if k.strip()]

_LAST_HIT = {}  # key → ts

def _throttle(key):
    now = time.time()
    if key in _LAST_HIT and now - _LAST_HIT[key] < 1.0:
        time.sleep(1.0 - (now - _LAST_HIT[key]))
    _LAST_HIT[key] = time.time()

# ---------- Fireworks ----------
def chat_fireworks(messages, model="accounts/fireworks/models/mixtral-8x7b-instruct"):
    for key in FIRE_KEYS:
        try:
            _throttle(key)
            r = requests.post(
                "https://api.fireworks.ai/inference/v1/chat/completions",
                headers={"Content-Type":"application/json","Authorization":f"Bearer {key}"},
                json={"model":model,"messages":messages},
                timeout=40
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"[FW fail] {e}")
    return None

# ---------- Hugging Face ----------
def chat_hf(messages, model="HuggingFaceH4/zephyr-7b-beta"):
    for key in HF_KEYS:
        try:
            _throttle(key)
            r = requests.post(
                f"https://api-inference.huggingface.co/models/{model}",
                headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                json={"inputs":messages[-1]["content"]},
                timeout=40
            )
            if r.status_code == 200:
                return r.json()[0]["generated_text"]
        except Exception as e:
            print(f"[HF fail] {e}")
    return None

# ---------- Alt provider (dummy echo) ----------
def chat_alt(messages):
    for key in ALT_KEYS:
        try:
            _throttle(key)
            # this is a placeholder; replace with real endpoint if needed
            return "[ALT provider not yet implemented]"
        except Exception:
            continue
    return None

# ---------- Groq fallback ----------
def chat_groq(messages, model="mixtral-8x7b-32768"):
    for key in GROQ_KEYS:
        try:
            _throttle(key)
            r = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                json={"model":model,"messages":messages},
                timeout=40
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"[Groq fail] {e}")
    return None

# ---------- Master router ----------
def ai(messages, model=None):
    for fn in (chat_fireworks, chat_hf, chat_alt, chat_groq):
        reply = fn(messages, model) if model else fn(messages)
        if reply: return reply
    raise RuntimeError("All providers failed")
