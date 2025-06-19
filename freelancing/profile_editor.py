"""
Profile editor (stub) — logs in & updates bio.
Long‑term: implement platform‑specific editors.
"""
def login(email: str, password: str):
    print(f"🔐 [stub] login({email})")

def update_bio(new_bio: str):
    print(f"✏️  [stub] update_bio('{new_bio[:30]}…')")
