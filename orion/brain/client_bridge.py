from orion.brain.farm_intel import log_earnings, report_top_sources
from orion.brain.self_learner import log_job
from orion.brain.chat_manager import start_client_chat, auto_negotiate
from orion.utils.telegram_notify import notify_admin

clients = [
    {"name": "JohnDoe", "job_value": 120},
    {"name": "StartupX", "job_value": 350},
    {"name": "AIDevInc", "job_value": 220}
]

def handle_incoming_clients():
    notify_admin("📡 ORION Client Bridge Online")
    for client in clients:
        start_client_chat(client["name"])
        final_value = auto_negotiate(client["name"], client["job_value"])
        log_job(client["name"], final_value)
        log_earnings("freelance_platform_X", final_value)
        notify_admin(f"💵 Job confirmed: {client[name]} | ${final_value}")

