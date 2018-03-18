import time
from crypto_bot.scraper.scraper import scraper_func
from crypto_bot.data_service import put_currencies

large_dict = {}
def prep_db():
    large_dict['cryptowp.com'] = scraper_func()
    put_currencies(large_dict)

    
def update_db():
    while True:
        prep_db()
        time.sleep(36_000)