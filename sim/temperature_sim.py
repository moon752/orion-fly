import json, time, random
from datetime import datetime

def run_temperature_sim():
    readings = [round(random.uniform(18.0, 35.0), 2) for _ in range(10)]
    time.sleep(2)

    result = {
        "timestamp": datetime.now().isoformat(),
        "readings": readings,
        "avg_temp": round(sum(readings)/len(readings), 2),
        "status": "normal" if max(readings) < 40 else "alert"
    }

    out_file = f"sim/temp_output_{int(time.time())}.json"
    with open(out_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"[SIM] Temperature output saved to {out_file}")

if __name__ == "__main__":
    run_temperature_sim()
