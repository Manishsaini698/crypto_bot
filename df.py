import requests
from bs4 import BeautifulSoup

link = ["https://cryptowp.com"]

def worker(i):
    res = requests.get(i)
    soup = bs4.BeautifulSoup(res.content, 'lxml')
    para = soup.

def scraper_func():
    url = "https://cryptowp.com/" 
    source_code = requests.get(url)                
    plain_text = source_code.text                
    soup = BeautifulSoup(plain_text,'html.parser')  
    currencies = []
    for k in soup.findAll(class_="cryptowp-coin-name"):
        name = k.string
        currencies.append(name.upper())
    values = []
    for v in soup.findAll(class_="cryptowp-coin-price-total"):
        value = v.string
        values.append(value)
    crypto_dict = {}
    for i in range(len(currencies)):
        crypto_dict[currencies[i]] = '$' + values[i]  
    return(crypto_dict)

