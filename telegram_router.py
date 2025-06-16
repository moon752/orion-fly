import telebot, os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID  = os.getenv("TELEGRAM_CHAT_ID")
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['auto_build'])
def handle_auto_build(msg):
    if str(msg.chat.id)!=CHAT_ID: return
    bot.send_message(CHAT_ID,"🔍 Auto‑build started…")
    from builder import find_targets
    targets=find_targets()
    if not targets:
        bot.send_message(CHAT_ID,"✅ Nothing to build.")
        return
    from builder.gen_patch import main as build
    for t in targets: build(t)
    from builder.apply_and_push import main as push
    push()
    bot.send_message(CHAT_ID,"🚀 Auto‑build complete & pushed.")

@bot.message_handler(commands=['auto_build'])
def handle_auto_build(message):
    if str(message.chat.id) != CHAT_ID: return
    from builder.audit import find_gaps
    missing = find_gaps()
    if not missing:
        bot.send_message(CHAT_ID,"✅ All phases present.")
        return
    bot.send_message(CHAT_ID,f"🔨 Building {len(missing)} missing modules...")
    for path in missing.values():
        from builder.gen_patch import make_patch
        diff = make_patch(path)
        bot.send_message(CHAT_ID,f"Patch ready: {diff}")
    from builder.apply_and_push import main as apply
    apply()
    bot.send_message(CHAT_ID,"🚀 Auto‑build finished & pushed!")

@bot.message_handler(commands=['cmd'])
def cmd(msg):
    if str(msg.chat.id) != CHAT_ID: return
    try:
        result = eval(msg.text.replace('/cmd ','') , globals())
        bot.send_message(CHAT_ID,f"✅ CMD:\n{result}")
    except Exception as e:
        bot.send_message(CHAT_ID,f"❌ CMD error:\n{e}")

@bot.message_handler(commands=['think'])
def think(msg):
    idea = msg.text.replace('/think ','')
    with open('brain/agent_ideas.txt','a') as f: f.write(idea+'\n')
    bot.send_message(CHAT_ID,f"🧠 Idea logged:\n{idea}")

@bot.message_handler(commands=['start','hello'])
def hello(msg): bot.send_message(msg.chat.id,"👋 ORION online.")

if __name__ == "__main__":
    print("🤖 ORION Telegram router running…")
    bot.infinity_polling()
