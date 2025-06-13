from random import randint, uniform

def simulate(job):
    win = round(uniform(0.3, 0.9), 2)
    payout = randint(5, 200)
    cost = randint(1, 10)
    profit = round(payout * win - cost, 2)
    print(f"[SIM] {job:<10} | win {win*100:>3}% | profit: ${profit}")
if __name__ == "__main__":
    for jt in ("Python", "Web", "Writing", "AI"):
        simulate(jt)
