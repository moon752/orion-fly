import json, subprocess, pathlib
PATCH_VOTES = pathlib.Path("brain/patch_votes.json")
def apply_patch(p):
    try:
        subprocess.run(["git", "apply", p], check=True)
        print(f"✅ Applied {p}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Patch {p} failed:", e)
        return False
def main():
    if not PATCH_VOTES.exists(): return
    votes = json.loads(PATCH_VOTES.read_text())
    for patch, v in votes.items():
        if v >= 3 and pathlib.Path(patch).exists():
            if apply_patch(patch):
                subprocess.run(["git", "add", "."], check=False)
                subprocess.run(["git", "commit", "-m", f'🤖 auto-patch {patch}'], check=False)
                subprocess.run(["git", "push"], check=False)
if __name__ == "__main__":
    main()
