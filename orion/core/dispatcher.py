import os
import json
import asyncio
from utils.telegram import send_message
from utils.models import ask_openrouter, ask_groq
from utils.storage import save_task, load_tasks, rotate_cache

COMMANDS = {}

def command(name):
    def wrapper(func):
        COMMANDS[name] = func
        return func
    return wrapper

@command("apply")
async def apply_job():
    from job_applicator import run_application
    await send_message("🚀 Applying to job...")
    await run_application()

@command("simulate")
async def simulate_task():
    task = "Design a Python script to scrape data from a freelance job site and summarize the results."
    await send_message("🧪 Simulating task...\n" + task)
    result = await ask_openrouter(task)
    await send_message("💡 Simulation result:\n" + result)
    save_task("simulation", {"task": task, "response": result})

@command("report")
async def report_status():
    tasks = load_tasks()
    summary = f"📊 Total tasks: {len(tasks)}\nLatest: {list(tasks)[-1] if tasks else 'None'}"
    await send_message(summary)

@command("reset")
async def reset_storage():
    for folder in ["orion_data/tasks", "orion_data/cache"]:
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
    await send_message("🧹 ORION memory and cache cleared.")

@command("upgrade")
async def upgrade_self():
    await send_message("🔄 Self-upgrade not yet implemented. (stub)")

async def handle_command(cmd: str):
    func = COMMANDS.get(cmd.strip("/"))
    if func:
        await func()
    else:
        await send_message(f"❌ Unknown command: \`{cmd}\`")
from orion.core.memory import get_memory, update_memory
from orion.utils.status import get_system_status

async def handle_command(command):
    if command == "/status":
        status = get_system_status()
        return status
    elif command.startswith("/remember "):
        key_value = command[len("/remember "):].split("=", 1)
        if len(key_value) == 2:
            key, value = key_value
            update_memory({key.strip(): value.strip()})
            return f"Remembered {key.strip()}"
        else:
            return "Usage: /remember key=value"
    elif command.startswith("/recall "):
        key = command[len("/recall "):].strip()
        memory = get_memory()
        return memory.get(key, f"No memory found for {key}")
    else:
        return "Unknown command"
