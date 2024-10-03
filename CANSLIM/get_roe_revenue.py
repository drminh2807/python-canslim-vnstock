from vnstock3 import Vnstock

def get_roe(ticker):
    stock = Vnstock().stock(symbol=ticker, source='VCI')
    ratio = stock.finance.ratio(period='year', lang='en')
    roe = ratio['Chỉ tiêu khả năng sinh lợi']['ROE (%)'][0]
    return roe

def get_revenue_quarterly(ticker):
    stock = Vnstock().stock(symbol=ticker, source='VCI')
    income_statement = stock.finance.income_statement(period='quarter', lang='en')
    revenue_list = income_statement['Revenue (Bn. VND)']
    return revenue_list

def get_revenue_annually(ticker):
    stock = Vnstock().stock(symbol=ticker, source='VCI')
    income_statement = stock.finance.income_statement(period='year', lang='en')
    revenue_list = income_statement['Revenue (Bn. VND)']
    return revenue_list
