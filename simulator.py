import random
import json

def simulate_job(job):
    difficulty = random.uniform(0, 1)
    payout = job.get('pay', random.uniform(50, 200))
    hours = random.uniform(1, 10)
    score = (payout / hours) - (difficulty * 2)
    decision = 'ACCEPT' if score > 10 else 'REJECT'
    # Add AI auto-fix stub: simulate error detection & correction (dummy for now)
    fix_attempts = 0
    max_attempts = 3
    while fix_attempts < max_attempts:
        # Fake error detection (10% chance)
        error_detected = random.random() < 0.1
        if not error_detected:
            break
        fix_attempts += 1
    result = {
        'score': score,
        'decision': decision,
        'difficulty': difficulty,
        'payout': payout,
        'hours': hours,
        'fix_attempts': fix_attempts,
        'job_title': job.get('title', 'Unknown'),
        'job_id': job.get('id', 'N/A')
    }
    return result

def save_simulation_log(sim_results, filename='simulation_log.json'):
    try:
        with open(filename, 'a') as f:
            f.write(json.dumps(sim_results) + '\\n')
    except Exception as e:
        print(f'Error saving simulation log: {e}')
