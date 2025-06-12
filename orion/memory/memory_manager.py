import json
import os

MEMORY_FILE = "orion/memory/long_term_memory.json"
session_memory = {}

def load_long_term_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_long_term_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

long_term_memory = load_long_term_memory()

def add_to_short_term(session_id, key, value):
    if session_id not in session_memory:
        session_memory[session_id] = {}
    session_memory[session_id][key] = value

def get_from_short_term(session_id, key):
    return session_memory.get(session_id, {}).get(key)

def add_to_long_term(key, value):
    long_term_memory[key] = value
    save_long_term_memory(long_term_memory)

def get_from_long_term(key):
    return long_term_memory.get(key)

def forget_long_term(key):
    if key in long_term_memory:
        del long_term_memory[key]
        save_long_term_memory(long_term_memory)
