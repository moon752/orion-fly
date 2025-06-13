import telebot, os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID  = os.getenv("TELEGRAM_CHAT_ID")
bot = telebot.TeleBot(BOT_TOKEN)

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
