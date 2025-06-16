import subprocess, sys, pathlib, textwrap, os, json
def run():
    try:
        subprocess.run(["python","-m","pip","install","--quiet","flake8"], check=False)
        subprocess.run(["flake8","."], check=True)
        for py in pathlib.Path(".").rglob("*.py"):
            subprocess.run([sys.executable,"-m","py_compile",str(py)], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ tests failed:", e)
        return False
if __name__=="__main__":
    print(json.dumps({"ok":run()}))
