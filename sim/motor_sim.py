import json, time
from datetime import datetime

def run_simulation():
    with open("sim/sensor_input.json", "r") as f:
        inputs = json.load(f)

    speed = inputs.get("motor_speed", 0)
    duration = inputs.get("duration_sec", 5)
    print(f"[SIM] Motor running at {speed} RPM for {duration} seconds...")
    time.sleep(duration)

    result = {
        "timestamp": datetime.now().isoformat(),
        "motor_speed": speed,
        "duration": duration,
        "status": "success" if speed <= 3000 else "overload"
    }

    output_file = f"sim/sim_output_{int(time.time())}.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"[SIM] Output saved to {output_file}")

if __name__ == "__main__":
    run_simulation()
