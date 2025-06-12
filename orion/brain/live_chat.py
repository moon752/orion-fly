import telegram
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_token")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "your_chat_id")

def send_live_msg(text):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)
