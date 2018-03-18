import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def put_currencies(crypto_dict):
    for key in crypto_dict:
        r.hmset(key, crypto_dict[key])

def get_currencies(currency):
    a = []
    a.append(r.hget('cryptowp.com',currency.upper()))
    return a
