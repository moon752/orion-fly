import json, os

def load_data(filename):
    path = f'orion/storage/{filename}'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    with open(f'orion/storage/{filename}', 'w') as f:
        json.dump(data, f, indent=2)
