from utils.telegram import send_telegram_message

def handle_writer_job(job):
    title = job.get("position")
    desc = job.get("description")

    send_telegram_message(f"📝 Starting Writing Task: {title}\n\n{desc[:500]}...")
    # TODO: Add content generation + save draft
