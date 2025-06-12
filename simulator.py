import json
import time
import random
import datetime

def load_earnings():
    try:
        with open("earnings.json", "r") as f:
            return json.load(f)
    except:
        return {"daily": [], "total": 0}

def save_earnings(data):
    with open("earnings.json", "w") as f:
        json.dump(data, f, indent=2)

def simulate_earning():
    amount = round(random.uniform(10, 100), 2)
    now = datetime.datetime.now().isoformat()
    return {"amount": amount, "timestamp": now}

def main():
    print("🧪 ORION Simulation Running...")
    data = load_earnings()
    new_earning = simulate_earning()
    data["daily"].append(new_earning)
    data["total"] += new_earning["amount"]
    save_earnings(data)
    print(f"💰 Simulated: $ {new_earning['amount']} | Total: $ {data['total']:.2f}")

if __name__ == "__main__":
    main()
