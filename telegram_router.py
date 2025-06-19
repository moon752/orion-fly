import os, telebot
from dotenv import load_dotenv
load_dotenv()

from job_applicator import stop_loop, get_stats
from updater import self_update

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['ping'])
def handle_ping(msg):
    bot.reply_to(msg, "pong 🏓")

@bot.message_handler(commands=['status'])
def handle_status(msg):
    s = get_stats()
    txt = (f"📊 *ORION Status*\n• Jobs fetched: {s['jobs']}\n"
           f"• Applied: {s['applied']}\n• Errors: {s['errors']}")
    bot.reply_to(msg, txt, parse_mode="Markdown")

@bot.message_handler(commands=['stoploop'])
def handle_stop(msg):
    stop_loop()
    bot.reply_to(msg, "🛑 Bid loop stopped by command.")

@bot.message_handler(commands=['update'])
def handle_update(msg):
    bot.reply_to(msg, "🔁 Pulling latest code from GitHub…")
    result = self_update()
    bot.reply_to(msg, f"✅ Update result:\n{result}")

print("[ORION] Telegram control ready.")

from ai_builder.ai_build_manager import build_and_fix




@bot.message_handler(commands=['help'])
def handle_help(msg):
    bot.reply_to(msg, "/ping /status /stoploop /update /auto_build /profile")

@bot.message_handler(commands=['profile'])
def handle_profile(msg):
    email = os.getenv("ORION_FREELANCER_SELF_EMAIL","not‑set")
    bot.reply_to(msg, f"Current Freelancer email: {email}")



@bot.message_handler(commands=['status_check'])
def handle_status_check(msg):
    try:
        from ai_builder import ai_self_planner as planner
        bot.reply_to(msg, planner.build_roadmap())
    except Exception as e:
        bot.reply_to(msg, f"❌ Failed to scan: {e}")


@bot.message_handler(commands=['auto_build'])
def handle_auto_build(msg):
    from ai_builder.ai_build_manager import build_and_fix
    parts = msg.text.split(' ',1)
    task = parts[1] if len(parts)>1 else ''
    bot.reply_to(msg, "🔧 Starting AI build & repair…")
    ok = build_and_fix(lambda t: bot.reply_to(msg, t))
    if ok:
        bot.reply_to(msg, "✅ Build success. ORION will restart jobs in 30 min.")


bot.infinity_polling()
