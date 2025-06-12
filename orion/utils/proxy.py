import random

PROXIES = [
    "http://proxyuser:proxypass@proxy1.example.com:8000",
    "http://proxyuser:proxypass@proxy2.example.com:8000",
    "http://proxyuser:proxypass@proxy3.example.com:8000"
]

def get_random_proxy():
    return random.choice(PROXIES)
