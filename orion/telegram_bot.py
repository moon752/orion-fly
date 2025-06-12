import telegram
from telegram.ext import Updater, MessageHandler, Filters
from orion.modules.admin_link_handler import handle_admin_command
from orion.modules.chat_handler import smart_reply
from orion.core.secrets_manager import load_secrets

secrets = load_secrets()
bot_token = secrets.get("TELEGRAM_BOT_TOKEN")

def handle_message(update, context):
    try:

        response = smart_reply(message.text)

        if response:

            context.bot.send_message(chat_id=update.effective_chat.id, text=response)

            return

    except Exception as e:

        context.bot.send_message(chat_id=update.effective_chat.id, text="I had trouble processing that.")
    message = update.message
    message_text = message.text.lower().strip() if message.text else ""

    if "#adminlink" in message_text:
        response = handle_admin_command(message_text)
        message.reply_text(response)

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
