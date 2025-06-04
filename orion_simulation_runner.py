import json
from simulator import auto_fix_simulation, save_simulation_output, generate_human_summary
from simulation_mocks import run_unity_simulation, run_pyserial_simulation
from job_fetcher import fetch_jobs
from telegram_utils import send_telegram_message

def run_orion_simulation_cycle():
    print("🔍 Fetching jobs for simulation...")
    jobs = fetch_jobs()
    if not jobs:
        print("No jobs found.")
        return

    for job in jobs:
        print(f"🤖 Running simulation for job: {job.get('title')}")
        arduino_code = job.get("arduino_code", "// default empty code")
        circuit_json = job.get("circuit_json", "{}")

        sim_result = auto_fix_simulation(arduino_code, circuit_json)
        save_simulation_output(sim_result, f"sim_output_{job.get('id','0')}.json")

        unity_result = run_unity_simulation(job)
        pyserial_result = run_pyserial_simulation(arduino_code)

        summary = generate_human_summary(sim_result)
        summary += f"\nUnity Simulation: {unity_result.get('status')}"
        summary += f"\npySerial Simulation: {pyserial_result.get('status')}"

        send_telegram_message(f"Simulation report for job '{job.get('title')}':\n{summary}")

if __name__ == "__main__":
    run_orion_simulation_cycle()
