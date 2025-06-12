import time
from orion.utils.telegram_notify import notify_admin

def start_client_chat(client_name):
    notify_admin(f"💬 Chat started with client: {client_name}")
    time.sleep(2)  # simulate chat delay
    notify_admin(f"📝 Chat with {client_name} complete. Proposal sent.")

def auto_negotiate(client_name, job_value):
    notify_admin(f"🤝 Negotiating with {client_name} for ${job_value}")
    time.sleep(1)
    agreed_value = int(job_value * 0.95)  # offer slight discount
    notify_admin(f"✅ Deal closed at ${agreed_value} with {client_name}")
    return agreed_value

