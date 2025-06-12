from orion.brain.ai_chat import generate_reply
from orion.brain.live_chat import send_live_msg

def handle_client_message(client_msg):
    reply = generate_reply(client_msg)
    send_live_msg(f"💬 Client said: {client_msg}\n🤖 ORION replies:\n{reply}")
    print("[AUTO-REPLY SENT]")

# Test
handle_client_message("Hi, can you build me a Telegram bot that handles crypto?")
