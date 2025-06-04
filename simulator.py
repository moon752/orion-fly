import requests
import json

WOKWI_API_URL = "https://wokwi.com/api/v1/arduino/simulate"

def run_wokwi_simulation(arduino_code:str, circuit_json:str) -> dict:
    payload = {
        "files": {
            "sketch.ino": arduino_code,
            "circuit.json": circuit_json
        },
        "log": True,
        "timeout": 15
    }
    try:
        resp = requests.post(WOKWI_API_URL, json=payload, timeout=20)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def fix_code_with_ai(code:str, error:str) -> str:
    print(f"🤖 AI fixing code due to error: {error}")
    # TODO: Replace this stub with actual AI call to Ollama/OpenRouter
    fixed_code = code + "\\n// AI auto-fix applied\\n"
    return fixed_code

def auto_fix_simulation(arduino_code, circuit_json, max_attempts=3):
    for attempt in range(1, max_attempts+1):
        print(f"🛠️ Attempt #{attempt} to simulate and fix...")
        result = run_wokwi_simulation(arduino_code, circuit_json)
        if 'error' in result:
            print(f"❌ Simulation error: {result['error']}")
            arduino_code = fix_code_with_ai(arduino_code, result['error'])
            continue
        if result.get('status') == 'success':
            print("✅ Simulation success!")
            return result
        else:
            print("❌ Simulation failed, retrying...")
            arduino_code = fix_code_with_ai(arduino_code, "Unknown error, retrying...")
    return {"error": "Max attempts reached, simulation failed"}

def generate_human_summary(sim_result:dict) -> str:
    if 'error' in sim_result:
        return f"Simulation failed: {sim_result['error']}"
    return "Simulation passed: Arduino code and circuit work perfectly."

def save_simulation_output(sim_result:dict, filename="sim_output.json"):
    with open(filename, "w") as f:
        json.dump(sim_result, f, indent=2)
