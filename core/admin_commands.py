import os, hmac, hashlib
SECRET = os.getenv("ORION_ADMIN_SECRET","moonpower2025").encode()
def valid(sig,cmd): return hmac.compare_digest(sig, hmac.new(SECRET, cmd.encode(), hashlib.sha256).hexdigest())
