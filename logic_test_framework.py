import subprocess
import json

def run_motor_sim():
    print("Running motor_sim.py...")
    subprocess.run(["python3", "motor_sim.py"], check=True)

def run_temperature_sim():
    print("Running temperature_sim.py...")
    subprocess.run(["python3", "temperature_sim.py"], check=True)

def run_api_mock_server():
    print("Starting api_mock_server.py in background...")
    subprocess.Popen(["python3", "api_mock_server.py"])

def run_web_scrape_sim():
    print("Running web_scrape_sim.py...")
    subprocess.run(["python3", "web_scrape_sim.py"], check=True)

def load_sensor_input():
    print("Loading sensor_input.json...")
    with open("sensor_input.json", "r") as f:
        data = json.load(f)
    print(f"Sensor input data: {data}")

def main():
    run_api_mock_server()
    run_motor_sim()
    run_temperature_sim()
    run_web_scrape_sim()
    load_sensor_input()
    print("All simulations completed!")

if __name__ == "__main__":
    main()
