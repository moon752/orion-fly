import os, random, requests, json, datetime
from utils.telegram import send_telegram_message

# 🔐 Group-aware OpenRouter keys (2 from same account)
KEY_GROUPS = {
    "main": [
        "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",
        "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"
    ],
    "friend1": [
        "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",
        "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"
    ]
}
ALL_KEYS = [key for group in KEY_GROUPS.values() for key in group]

# 🧠 Groq fallback keys
GROQ_KEYS = [
    "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",
    "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"
]

def select_openrouter_key():
    group = random.choice(list(KEY_GROUPS.values()))
    return random.choice(group)

def extract_code(text):
    if "```python" in text: return text.split("```python")[1].split("```")[0].strip()
    if "```" in text: return text.split("```")[1].strip()
    return text.strip()

def call_openrouter(prompt):
    key = select_openrouter_key()
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers={
        "Authorization": f"Bearer {key}", "Content-Type":"application/json"
    }, json={
        "model":"deepseek/deepseek-coder:free",
        "messages":[{"role":"user","content":prompt}]
    })
    return r.json()

def call_groq(prompt):
    key = random.choice(GROQ_KEYS)
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers={
        "Authorization": f"Bearer {key}", "Content-Type":"application/json"
    }, json={
        "model":"llama3-70b-8192",
        "messages":[{"role":"user","content":prompt}]
    })
    return r.json()

def smart_enhance(file):
    with open(file) as f: original = f.read()
    prompt = f"Enhance this ORION module for intelligence, safety, and error handling:\n```python\n{original}```"
    
    try:
        js = call_openrouter(prompt)
        content = js.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise Exception("OpenRouter failed.")
        new_code = extract_code(content)
    except:
        js = call_groq(prompt)
        content = js.get("choices", [{}])[0].get("message", {}).get("content", "")
        new_code = extract_code(content)

    if new_code.strip():
        with open(file, "w") as f: f.write(new_code)
        send_telegram_message(f"🔁 `{file}` enhanced successfully via AI")
    else:
        send_telegram_message(f"❌ `{file}` enhancement failed (empty response)")

if __name__ == "__main__":
    MODULES = ["job_applicator.py", "freelance_monitor.py", "auto_reply.py"]
    for m in MODULES:
        if os.path.exists(m): smart_enhance(m)
