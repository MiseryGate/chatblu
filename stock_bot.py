import requests
import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to retrieve stock prices
def get_stock_price(symbol):
    api_key = 'YOUR_YAHOO_FINANCE_API_KEY_HERE'
    url = f'https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['price']

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a stock price bot! Send me a stock symbol, and I'll tell you the current price.")

# Define a function to handle the /stock command
def stock(update, context):
    symbol = context.args[0]
    price = get_stock_price(symbol)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"The price of {symbol} is {price}.")

# Define a function to handle user inputs
def add_stock(update, context):
    symbol = update.message.text.upper()
    user_id = update.message.chat_id
    conn = sqlite3.connect('stock_bot.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stocks VALUES (?, ?)", (user_id, symbol))
    conn.commit()
    conn.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Thanks, I've added {symbol} to your list of stocks.")

# Define a function to handle the /mystocks command
def my_stocks(update, context):
    user_id = update.message.chat_id
    conn = sqlite3.connect('stock_bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT symbol FROM stocks WHERE user_id=?", (user_id,))
    symbols = cursor.fetchall()
    conn.close()
    if symbols:
        symbol_list = '\n'.join([symbol[0] for symbol in symbols])
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your saved stocks:\n{symbol_list}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You haven't saved any stocks yet.")

# Set up the bot
updater = Updater(token='YOUR_TELEGRAM_API_TOKEN_HERE', use_context=True)
dispatcher = updater.dispatcher

# Add handlers for the /start, /stock, and message commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('stock', stock))
dispatcher.add_handler(MessageHandler(Filters.text, add_stock))
dispatcher.add_handler(CommandHandler('mystocks', my_stocks))

# Set up the database
conn = sqlite3.connect('stock_bot.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS stocks (user_id INTEGER, symbol TEXT)")
conn.commit()
conn.close()

# Start the bot
updater.start_polling()
updater.idle()

#Baru tanggal 15 Mei 2023
import telegram
import openai
import yfinance as yf

# Replace YOUR_BOT_TOKEN with your actual bot token obtained from BotFather
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Replace YOUR_OPENAI_API_KEY with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.info['regularMarketPrice']
    return price

def handle_message(update, context):
    message = update.message.text
    last_symbol = context.user_data.get('last_symbol')
    if message.lower() == 'last':
        if last_symbol:
            price = get_stock_price(last_symbol)
            response = f"The price of {last_symbol} is {price:.2f}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No symbol found. Please enter a symbol first.")
    elif message.lower() == 'help':
        response = "Enter a stock symbol to retrieve its price. Type 'last' to retrieve the price of the last symbol queried."
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        context.user_data['last_message'] = message
        openai_response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=f"What is the current price of {message.upper()}?",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        price = get_stock_price(message.upper())
        response = f"{openai_response.choices[0].text.strip()} The price of {message.upper()} is {price:.2f}"
        context.user_data['last_symbol'] = message.upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def get_stock(update, context):
    symbol = update.message.text.upper()
    try:
        price = get_stock_price(symbol)
        response = f"The price of {symbol} is {price:.2f}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    except:
        handle_error(update, context)

def handle_error(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oops! Something went wrong. Please try again later.")

if __name__ == '__main__':
    from telegram.ext import Updater, MessageHandler, Filters

    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^/[a-zA-Z]+'), get_stock))
    updater.start_polling()
    updater.idle()