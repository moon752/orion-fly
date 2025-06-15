import json, random

TEMPLATES = [
    {"type":"write","prompt":"Blog about AI"},
    {"type":"code","prompt":"Python Fibonacci"},
    {"type":"design","prompt":"Logo for bakery"}
]

def generate_task():
    return json.dumps(random.choice(TEMPLATES))

if __name__ == "__main__":
    for _ in range(3):
        print(generate_task())
