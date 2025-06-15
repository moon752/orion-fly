import random, json
SAMPLES=[{"type":"write","prompt":"Blog about AI"},{"type":"code","prompt":"Fibonacci"}]
def generate(): return json.dumps(random.choice(SAMPLES))
if __name__=="__main__": print(generate())
