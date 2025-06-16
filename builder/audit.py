"""
builder.audit
-------------
Finds Python files that are empty, extremely short, or still contain TODO / stub markers.
Returns a list of relative paths.
"""

from pathlib import Path
import re

ROOTS = [
    "core", "builder", "freelance", "tasks", "storage",
    "reports", "dashboard", "sim", "security", "utils"
]

def find_targets() -> list[str]:
    targets: list[str] = []
    for root in ROOTS:
        for p in Path(root).rglob("*.py"):
            txt = p.read_text(errors="ignore")
            if (
                not txt.strip()                # completely empty
                or len(txt) < 40               # too short / stub
                or re.search(r"TODO|pass\\s+#\\s*stub|#\\s*🚧", txt)
            ):
                targets.append(str(p))
    return sorted(targets)

if __name__ == "__main__":
    print("\n".join(find_targets()) or "✅ No gaps detected.")
