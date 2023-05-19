#Script sebelum lebaran
import os
from dotenv import load_dotenv
import telegram
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

#Inisiasi Menu
menu = []
#Inisiasi Sub Menu
submenu = []
load_dotenv()
#Token Telegram
bot_token = os.getenv('BOT_TOKEN')
bot = telegram.Bot(token=bot_token)
#Token OPENAPI
openaitoken = os.getenv('OPENAI_TOKEN')
openai.api_key = openaitoken

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Halo! Selamat datang di BLU-Bot Telegram versi 0.1, we regulate simpler for better services. Silahkan pilih menu di bawah ini : \n \n /bimtek - Info Bimtek PPKBLU \n /user - Pendaftaran user BIOS \n /webservice - Info pengembangan webservice \n \n Silahkan langsung chat untuk menggunakan fitur chatbot secara umum menggunakan fasilitas OPENAI"
                             )

def bimtek(update, context):
    text_bimtek = "Pilih Tema Bimtek yang ingin dilihat : \n /integrasi \n /refreshment \n /matrat"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_bimtek)

def refreshment(update,context):
    text_refreshment = "Materi bimtek Refreshment BIOS dapat dilihat pada alamat : https://sites.google.com/view/refreshment-bios"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_refreshment)

def integrasi(update,context):
    text_integrasi = "Materi bimtek Integrasi Data dapat dilihat pada alamat : https://sites.google.com/view/integrasidata"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_integrasi)

def matrat(update,context):
    text_matrat = "Materi bimtek Maturity Rating dapat dilihat pada alamat : https://sites.google.com/view/workshop-bios"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_matrat)

def user(update,context):
    text_user = "Pendaftaran user BIOS untuk Satker BLU : https://sites.google.com/view/refreshment-bios/pendaftaranuser"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_user)

def webservice(update,context):
    text_webservice = "Panduan pengembangan BLU dapat dilihat pada : https://bit.ly/PanduanWebserviceBIOS \n Untuk join ke dalam grup Discord pengembangan webservice : https://bit.ly/DiscordWSBLU \n Info lebih lanjut mengenai webservice : /infows"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_webservice)

def infows(update,context):
    text_infows = "Webservice BIOS adalah penghubung antara aplikasi BIOS G2 dengan sistem eksternal (Satker BLU), layanan komunikasi untuk berinteraksi dan berbagi data memanfaatkan web service API (Application Programming Interface). Dengan memanfaatkan layanan komunikasi ini, sistem lain dalam hal ini yang dimiliki dan/atau akan dikembangkan Satker BLU dapat menyampaikan data sesuai kebutuhan Proses Bisnis BIOS G2. Layanan ini bersifat dua arah dengan format komunikasi menggunakan JSON. \n Proses permintaan pengembangan dapat dilakukan melalui aplikasi BIOS melalui menu Webservice - Pengajuan Development Webservice, lalu klik Request Secret Key"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_infows)

# def echo(update, context):
#     message = update.message.text
#     context.bot.send_message(
#         chat_id=update.effective_chat.id, text=message)
#     print(f"pesan dari user: {message}")
def echo(update: Update, context: CallbackContext):
    message = update.message.text

    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response back to the user
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('refreshment', refreshment))
dispatcher.add_handler(CommandHandler('integrasi', integrasi))
dispatcher.add_handler(CommandHandler('matrat', matrat))
dispatcher.add_handler(CommandHandler('bimtek', bimtek))
dispatcher.add_handler(CommandHandler('user', user))
dispatcher.add_handler(CommandHandler('webservice', webservice))
dispatcher.add_handler(CommandHandler('infows', infows))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()