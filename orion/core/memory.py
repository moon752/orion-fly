from orion.utils.storage import load_data, save_data

def get_memory():
    return load_data("memory.json")

def update_memory(new_data):
    data = get_memory()
    data.update(new_data)
    save_data("memory.json", data)
