import random

def simulate_job(job):
    # Simulate difficulty (1-10), payout, and time (hours)
    difficulty = random.randint(1, 10)
    payout = int(job.get("salary", "0").replace("$", "").replace(",", "") or random.randint(50, 500))
    time_required = random.randint(1, 12)

    score = (payout / time_required) - (difficulty * 2)
    status = "ACCEPT" if score > 10 else "REJECT"

    return {
        "difficulty": difficulty,
        "payout": payout,
        "time_hours": time_required,
        "score": round(score, 2),
        "decision": status
    }
