import random

def run_orion_once(hive_id):
    # Placeholder logic for an ORION job cycle
    print(f"💼 Hive #{hive_id} is applying to a job...")
    if random.random() < 0.05:
        raise Exception("Simulated hive error!")
