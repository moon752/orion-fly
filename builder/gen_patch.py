import pathlib, textwrap, json, time
from utils.ai_model import ai

PROMPT_TMPL = textwrap.dedent("""
You are ORION code‑generator. Create a complete, clean Python {kind} file at {path}.
If it's a module, include functions, docstrings, main guard.
No TODOs, no pass stubs. Make it production‑ready but lightweight.
""")

def generate(path: str)->str:
    kind="module" if path.endswith(".py") else "data file"
    prompt=PROMPT_TMPL.format(kind=kind,path=path)
    code = ai([{"role":"user","content":prompt}])
    return code or "# AI generation failed"

def write_file(path:str,content:str):
    p=pathlib.Path(path); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content)

def main(path):
    code = generate(path)
    write_file(path, code)
    print(f"✅ generated {path}")

if __name__=="__main__":
    import sys
    main(sys.argv[1])
