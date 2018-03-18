import threading
import logging
import time
from crypto_bot.main_scraper import update_db
from crypto_bot.bot import run_bot

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, filename='bot.log')

def start_everything():
    db_update_thread = threading.Thread(target=update_db)
    db_update_thread.start()
    logging.info("started scraper")

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    logging.info("started main bot loop")

