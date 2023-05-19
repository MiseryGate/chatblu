from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import openai
import os

# Set up Telegram bot
bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

# Set up OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the function to handle messages
def handle_message(update: Update, context: CallbackContext):
    message = update.message.text

    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response back to the user
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the Telegram updater
updater = Updater(token=os.environ["TELEGRAM_TOKEN"], use_context=True)
dispatcher = updater.dispatcher

# Register the message handler function
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import openai
import os

# Set up Telegram bot
bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

# Set up OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the function to handle messages
def handle_message(update: Update, context: CallbackContext):
    message = update.message.text

    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response back to the user
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the Telegram updater
updater = Updater(token=os.environ["TELEGRAM_TOKEN"], use_context=True)
dispatcher = updater.dispatcher

# Register the message handler function
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
