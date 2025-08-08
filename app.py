print("Bot is running...")
import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def start(update, context):
    update.message.reply_text("👋 Hello! Bot is working.")

def main():
    TOKEN = "8304683093:AAEj7w-On9532Y_650KPbmQUBc8u31qb48o"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
