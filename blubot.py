import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = telegram.Bot(token=bot_token)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Halo! Selamat datang di bot Telegram saya.")


def puisi(update, context):
    text_puisi = "Ini adalah contoh puisi"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_puisi)


def pantun(update, context):
    text_pantun = "Ini adalah contoh pantun"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_pantun)

def bimtek(update, context):
    text_bimtek = "Pilih Tanggal Bimtek yang ingin dilihat \n /pantun"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_bimtek)

def echo(update, context):
    message = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message)
    print(f"pesan dari user: {message}")


updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('puisi', puisi))
dispatcher.add_handler(CommandHandler('pantun', pantun))
dispatcher.add_handler(CommandHandler('bimtek', bimtek))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()