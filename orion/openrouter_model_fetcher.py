import requests, os, json, pathlib
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv("OPENROUTER_KEY_1")
URL = "https://openrouter.ai/api/v1/models"
OUT = pathlib.Path("orion/data/free_models.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

def fetch():
    res = requests.get(URL, headers={"Authorization":f"Bearer {KEY}"})
    res.raise_for_status()
    free = []
    for m in res.json().get("data", []):
        if m.get("pricing", {}).get("request") == "0":
            free.append({
                "id": m["id"],
                "name": m["name"],
                "context": m["context_length"],
                "tokenizer": m["architecture"].get("tokenizer"),
                "params": m.get("supported_parameters", [])
            })
    OUT.write_text(json.dumps(free, indent=2))
    print(f"✅ Saved {len(free)} free models to {OUT}")

if __name__ == "__main__":
    fetch()
