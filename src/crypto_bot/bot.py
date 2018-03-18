import telepot
import time
import os

from crypto_bot.scraper.scraper import scraper_func 
from telepot.loop import MessageLoop
from crypto_bot.data_service import get_currencies

bot = telepot.Bot(os.environ['your_bot_token'])


currencies = ['BITCOIN', 'ETHEREUM', 'LITECOIN', 'RIPPLE', 'BITCOIN CASH', 'MONERO', 'DASH', 'NEO', 'NANO', 'WAVES', 'SONM', 'ARK', 'BITCOIN', 'ETHEREUM', 'LITECOIN', 'RIPPLE', 'DASH', 'NEO', 'MONERO', 'WAVES', 'ARK', 'NANO', 'SONM']

def start(user,text='text'):
    bot.sendMessage(user,"I'll send you present value of cryptocurrency, please send me a name of cryptocurrency")


cmd_dict = {'/START':start}

def reply(user,text='text'):
    if text == 'start':
        start(user,text)
    if text in currencies:
        for i in get_currencies(text):
            bot.sendMessage(user,i)
    else:
        bot.sendMessage(user,"you sent something wrong!!!")

def handler(msg):
    user = msg['from']['id']
    text = msg['text'].upper()
    text_1 = text.split(' ')[0]
    print(text_1)
    run_this = cmd_dict.get(text_1, reply)
    print(run_this)
    run_this(user, text)
 
def run_bot():
    MessageLoop(bot, {'chat':handler}).run_as_thread()
    print("hello")
    while True:
        time.sleep(10)