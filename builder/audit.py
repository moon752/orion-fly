"""
builder.audit
-------------
Returns a list of Python files that need attention (empty, very short, or marked TODO/stub).
"""

from pathlib import Path
import re

EXCLUDE_NAMES = {"__init__.py", "telegram_router.py"}

def find_targets() -> list[str]:
    targets = []
    for file in Path(".").rglob("*.py"):
        if (
            file.name not in EXCLUDE_NAMES
            and "site-packages" not in str(file)
        ):
            txt = file.read_text(errors="ignore")
            if (
                not txt.strip()                       # empty file
                or len(txt) < 40                      # too short
                or re.search(r"TODO|pass\\s+#\\s*stub|#\\s*🚧", txt)
            ):
                targets.append(str(file))
    return targets

if __name__ == "__main__":
    print("\n".join(find_targets()) or "✅ No gaps detected.")
