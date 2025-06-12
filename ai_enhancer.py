import os
import json
import datetime
import requests
from utils.telegram import send_telegram_message

OPENROUTER_KEYS = [
    "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",
    "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",
    "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"
]

MODELS = [
    "microsoft/phi-4-reasoning-plus",
    "deepseek/deepseek-prover-v2",
    "qwen/qwen3-14b",
    "nvidia/llama-3.1-nemotron-ultra-253b-v1"
]

TARGET_FILES = ["job_applicator.py", "freelance_monitor.py", "auto_reply.py"]
BACKUP_FOLDER = "backups"
ENHANCEMENT_LOG = "ai_upgrade_log.json"

def rotate_key():
    return OPENROUTER_KEYS[int(datetime.datetime.now().timestamp()) % len(OPENROUTER_KEYS)]

def send_to_ai(filename, content):
    prompt = f"Improve this ORION module with better logic, AI handling, and clean error-proof code:\n\n```python\n{content}\n```"
    headers = {
        "Authorization": f"Bearer {rotate_key()}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODELS[0],
        "messages": [
            {"role": "system", "content": "You are an expert AI developer."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        new_code = result['choices'][0]['message']['content']
        return extract_code(new_code)
    except Exception as e:
        print(f"❌ AI enhancement failed for {filename}: {e}")
        return None

def extract_code(text):
    # Extract code block from AI response
    if "```python" in text:
        return text.split("```python")[1].split("```")[0].strip()
    elif "```" in text:
        return text.split("```")[1].strip()
    return text.strip()

def backup_file(filename):
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    with open(filename, "r") as f:
        with open(os.path.join(BACKUP_FOLDER, filename), "w") as b:
            b.write(f.read())

def log_enhancement(file, status):
    log = []
    if os.path.exists(ENHANCEMENT_LOG):
        with open(ENHANCEMENT_LOG, "r") as f:
            try:
                log = json.load(f)
            except:
                log = []
    log.append({
        "file": file,
        "status": status,
        "timestamp": datetime.datetime.now().isoformat()
    })
    with open(ENHANCEMENT_LOG, "w") as f:
        json.dump(log, f, indent=2)

def enhance_all():
    send_telegram_message("⚙️ ORION AI Enhancement Phase Started")
    for file in TARGET_FILES:
        try:
            with open(file, "r") as f:
                original_code = f.read()
            backup_file(file)
            enhanced = send_to_ai(file, original_code)
            if enhanced:
                with open(file, "w") as f:
                    f.write(enhanced)
                print(f"✅ AI upgraded {file}")
                log_enhancement(file, "Enhanced ✅")
                send_telegram_message(f"🚀 AI upgraded `{file}` successfully.")
            else:
                log_enhancement(file, "Failed ❌")
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")
            log_enhancement(file, f"Failed with error: {e}")

if __name__ == "__main__":
    enhance_all()
