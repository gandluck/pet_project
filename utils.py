import ccxt

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


