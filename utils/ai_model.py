
import os, random, requests, time

GROQ_KEYS       = [k for k in os.getenv("GROQ_KEYS","").split(",") if k]
FIREWORKS_KEYS  = [k for k in os.getenv("FIREWORKS_KEYS","").split(",") if k]
HF_KEYS         = [k for k in os.getenv("HF_KEYS","").split(",") if k]
SCHNELL_KEY     = os.getenv("SCHNELL_API_KEY","")   # NEW provider

def call_groq(key, messages, temp):
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization":f"Bearer {key}"},
        json={"model":"mixtral-8x7b-32768","messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def call_fireworks(key, messages, temp):
    r = requests.post(
        "https://api.fireworks.ai/inference/v1/chat/completions",
        headers={"Authorization":f"Bearer {key}"},
        json={"model":"accounts/fireworks/models/mixtral-8x7b-instruct","messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def call_hf(key, messages):
    prompt = messages[-1]["content"]
    r = requests.post(
        "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        headers={"Authorization":f"Bearer {key}"},
        json={"inputs":prompt}, timeout=40)
    r.raise_for_status()
    out = r.json()
    return out[0]["generated_text"] if isinstance(out,list) else out["generated_text"]

def call_schnell(messages, temp):
    """Free Schnell Llama‑Vision 11B / FLUX.1 endpoint"""
    key = SCHNELL_KEY
    if not key: raise RuntimeError("No Schnell key")
    r = requests.post(
        "https://api.schnell.ai/v1/chat/completions",
        headers={"Authorization":f"Bearer {key}"},
        json={"model":"flux.llama-vision-11b","messages":messages,"temperature":temp},
        timeout=40)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def ai(messages, temperature=0.7):
    # 1) Groq keys
    for k in GROQ_KEYS:
        try: return call_groq(k, messages, temperature)
        except Exception as e: print("[groq]", e)

    # 2) Fireworks keys
    for k in FIREWORKS_KEYS:
        try: return call_fireworks(k, messages, temperature)
        except Exception as e: print("[fw]", e)

    # 3) Schnell (single key)
    try: return call_schnell(messages, temperature)
    except Exception as e: print("[schnell]", e)

    # 4) HuggingFace keys
    for k in HF_KEYS:
        try: return call_hf(k, messages)
        except Exception as e: print("[hf]", e)

    raise RuntimeError("All providers failed")
