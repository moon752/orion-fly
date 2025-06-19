"""
Very lightweight VPN/Proxy rotator.
Usage:
    from core.vpn_manager import rotate
    proxy = rotate()
"""
import itertools, os, random

PROXIES = [
    # format user:pass@host:port or just host:port
    "138.68.60.8:8080",
    "user:pass@51.158.68.68:8811",
]
_cycle = itertools.cycle(PROXIES)

def rotate(randomize: bool = False) -> str:
    """Return next proxy (round‑robin or random)."""
    if randomize:
        return random.choice(PROXIES)
    return next(_cycle)
