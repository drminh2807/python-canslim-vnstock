from vnstock3 import Vnstock

def get_quarterly_eps(ticker):
    return get_eps(ticker, 'quarter')

def get_annually_eps(ticker):
    return get_eps(ticker, 'year')

def get_eps(ticker, period):
    stock = Vnstock().stock(symbol=ticker, source='VCI')
    ratio = stock.finance.ratio(period=period, lang='en')
    result = ratio['Chỉ tiêu định giá']['EPS (VND)'][:5]
    return list(reversed(result))
