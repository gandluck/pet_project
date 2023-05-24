import ccxt

# api = '4XkpJbSLy1KKlXYIde9cPqgKhgmbu3jM7uI0AEmqJlo7GHatVoyICyY6QIeEIhWI'
# secret = 'ojy9LbIVaWYayIzPDJ8UNhujUGvLebP8MI5zlRbiUsdfK0CwYni1e0DliDDPPfGv'

def check_api_keys(api, secret):
    exchange_id = 'binance'
    exchange_class = getattr(ccxt, exchange_id)
    exchange: ccxt.binance = exchange_class({
        'apiKey': api,
        'secret': secret
    })
    try:
        if exchange.fetch_balance():
            return True
    except:
        return False


