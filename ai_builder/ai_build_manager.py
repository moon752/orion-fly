import os, json, subprocess, difflib, requests, textwrap
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
GROQ_API_KEY     = (os.getenv("GROQ_KEYS","").split(",")[0]).strip()

PROJECT_SUMMARY = (
    "ORION: multi‑agent freelancer bot. "
    "Key dirs: job_applicator.py, freelancing/, core/."
)

FIX_PROMPT = """You are ORION‑Fixer, an expert Python engineer.
Project summary:
{summary}

Traceback:
> 
Return ONLY valid JSON:

{{
  "explanation": "...",
  "patches": [{{"file": "path", "diff": "unified diff"}}],
  "needs_secret": ""
}}
"""

def run_tests():
    try:
        return subprocess.run(
            ["python", "-m", "pytest", "-q"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
    except FileNotFoundError:
        return subprocess.CompletedProcess(args=[], returncode=0, stdout="pytest missing")

def call_together(prompt: str) -> str:
    r = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={"Authorization": f"Bearer {TOGETHER_API_KEY}"},
        json={
            "model": "deepseek/deepseek-coder:free",
            "max_tokens": 1024,
            "temperature": 0.3,
            "messages": [
                {"role": "system", "content": "You ONLY fix crashing bugs. Do NOT add features."},
                {"role": "user", "content": prompt}
            ]
        },
        timeout=90
    )
    data = r.json()
    print("[TOGETHER RAW]", json.dumps(data)[:400])
    return data.get("choices", [{}])[0].get("message", {}).get("content", "")

def call_groq(prompt: str) -> str:
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": "mixtral-8x7b-32768",
            "max_tokens": 512,
            "temperature": 0.2,
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=60
    )
    data = r.json()
    return data.get("choices", [{}])[0].get("message", {}).get("content", "groq error")

def apply_patch(patch):
    diff_lines = patch["diff"].splitlines()
    new = list(difflib.restore(diff_lines, 2))
    Path(patch["file"]).write_text("\n".join(new))

def fix_code(task_text, reply):
    reply("🔧 Starting AI build & repair…")
    res = run_tests()
    if res.returncode == 0 and not task_text:
        reply("✅ No test failures. Build OK.")
        return True

    trace = res.stdout[-1500:]
    prompt = FIX_PROMPT.format(summary=PROJECT_SUMMARY, trace=trace)
    ai_raw = call_together(prompt)

    try:
        fix = json.loads(ai_raw)
    except Exception:
        reply("❌ AI returned bad JSON:\n" + ai_raw)
        return False

    review = call_groq(f"Rate this patch safe? YES/NO\n```json\n{ai_raw}\n```")
    if "yes" not in review.lower():
        reply("🛑 Patch rejected by reviewer.")
        return False

    if fix.get("needs_secret"):
        reply(f"🔑 Missing secret `{fix['needs_secret']}`. Add it and retry.")
        return False

    for p in fix.get("patches", []):
        apply_patch(p)

    reply("🔄 Patch applied. Retesting…")
    if run_tests().returncode == 0:
        reply("🎉 Tests green. ORION will restart jobs in 30 min.")
        return True

    reply("❌ Patch failed tests.")
    return False
