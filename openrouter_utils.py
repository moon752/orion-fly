from telegram_utils import send_telegram_message
from simulator import simulate_job, save_simulation_log
import json

simulation_summary = {
    'total_jobs': 0,
    'accepted': 0,
    'rejected': 0,
    'total_fix_attempts': 0
}

def choose_and_apply_jobs(jobs):
    global simulation_summary
    simulation_summary['total_jobs'] = len(jobs)
    for job in jobs:
        sim = simulate_job(job)
        save_simulation_log(sim)
        simulation_summary['total_fix_attempts'] += sim['fix_attempts']

        # Telegram logs for simulation
        message = (
            f"🧠 Simulation Result for job '{sim['job_title']}':\n"
            f"Score: {sim['score']:.2f}\n"
            f"Decision: {sim['decision']}\n"
            f"Difficulty: {sim['difficulty']:.2f}\n"
            f"Payout: ${sim['payout']:.2f}\n"
            f"Hours Est.: {sim['hours']:.2f}\n"
            f"Fix Attempts: {sim['fix_attempts']}\n"
        )
        send_telegram_message(message)

        if sim['decision'] == 'REJECT':
            simulation_summary['rejected'] += 1
            print(f'❌ Rejected job: {sim["job_title"]} | Score: {sim["score"]:.2f}')
            continue

        simulation_summary['accepted'] += 1
        print(f'✅ Accepted job: {sim["job_title"]} | Score: {sim["score"]:.2f}')

        # Here add your existing application logic with AI to apply to job...

def print_simulation_summary():
    global simulation_summary
    summary = (
        f"📊 Simulation Summary:\n"
        f"Total Jobs: {simulation_summary['total_jobs']}\n"
        f"Accepted: {simulation_summary['accepted']}\n"
        f"Rejected: {simulation_summary['rejected']}\n"
        f"Total Auto-Fix Attempts: {simulation_summary['total_fix_attempts']}\n"
    )
    print(summary)
    send_telegram_message(summary)
