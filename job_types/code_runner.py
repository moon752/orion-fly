from utils.telegram import send_telegram_message

def handle_code_job(job):
    title = job.get("position")
    desc = job.get("description")

    send_telegram_message(f"⚙️ Starting Code Task: {title}\n\n{desc[:500]}...")
    # TODO: Add code generation + output saving
