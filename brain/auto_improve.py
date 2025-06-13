"""
ORION Auto‑Improver  (Phase19 core)

Usage:
    python3 brain/auto_improve.py                # LLM decides what to improve
    python3 brain/auto_improve.py <file_or_task> # you specify focus
"""
import pathlib, sys, datetime, difflib, json, os
from utils.ai_model import ai

UPGRADE_DIR = pathlib.Path("brain/upgrades"); UPGRADE_DIR.mkdir(parents=True, exist_ok=True)
TIMESTAMP   = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")

def choose_file():
    py_files = [p for p in pathlib.Path(".").rglob("*.py")
                if not str(p).startswith((".__", "brain/upgrades", "venv", ".pythonlibs"))]
    return max(py_files, key=lambda p: p.stat().st_mtime)  # last modified

def build_prompt(file_path, extra=None):
    header = f"ORION code base self‑improvement task. Today's UTC {datetime.datetime.utcnow()}.\n"
    if file_path:
        code = pathlib.Path(file_path).read_text()
        header += f"--- FILE:{file_path} BELOW ---\n{code}\n--- END FILE ---\n"
        header += "Suggest a unified‑diff patch that improves performance, security, or readability."
    else:
        header += f"Task: {extra}\nSuggest code changes, specify target file(s) and provide patches."
    return header

def query_llm(prompt):
    return ai.chat([
        {"role":"system","content":"You are ORION's senior software engineer."},
        {"role":"user","content":prompt}
    ])

def save_patch(diff_text):
    patch_path = UPGRADE_DIR / f"patch_{TIMESTAMP}.diff"
    patch_path.write_text(diff_text)
    return patch_path

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    target_file = arg if arg and pathlib.Path(arg).is_file() else None
    prompt = build_prompt(target_file, extra=arg if not target_file else None)
    print("🤖 Requesting improvement ideas from LLM...")
    diff_text = query_llm(prompt)
    patch_path = save_patch(diff_text)
    print(f"✅ Patch saved to {patch_path}")
    print("Next step: /cmd git apply", patch_path, "   or review manually.")

if __name__ == "__main__":
    main()
