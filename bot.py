import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from orion.core.dispatcher import handle_command

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Your Telegram token stored in Replit secrets as BOT_TOKEN

if not BOT_TOKEN:
    raise ValueError("Missing BOT_TOKEN environment variable!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ORION is online and ready. Use /status or other commands.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("/"):
        response = await handle_command(text)
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("Send a command starting with /")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, handle_message))

    print("ORION bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
