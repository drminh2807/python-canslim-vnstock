from typing import List
from get_stock_df import get_stock_df
from visualize_stocks_quarterly import visualize_stocks_quarterly
from visualize_stocks_annually import visualize_stocks_annually
import fire
from vnstock3 import Vnstock
def main(*tickers: List[str]):
    """
    Returns analytics using the CANSLIM method.
    :param tickers: A list of stock tickers or group HOSE, VN30, VNMidCap, VNSmallCap, VNAllShare, VN100, ETF, HNX, HNX30, HNXCon, HNXFin, HNXLCap, HNXMSCap, HNXMan, UPCOM, FU_INDEX.
    :return: analytics using the CANSLIM method.
    """    
    available_groups = ['HOSE', 'VN30', 'VNMidCap', 'VNSmallCap', 'VNAllShare', 'VN100', 'ETF', 'HNX', 'HNX30', 'HNXCon', 'HNXFin', 'HNXLCap', 'HNXMSCap', 'HNXMan', 'UPCOM', 'FU_INDEX']
    
    if tickers[0] in available_groups:
        tickers_list = Vnstock().stock(symbol='FPT', source='VCI').listing.symbols_by_group(tickers[0])
    else:
        tickers_list = tickers

    if len(tickers_list) == 0:
        print("Usage: python CANSLIM/main.py analyze <ticker> <ticker> <ticker> ...")
        return

    try:        
        stock_df = get_stock_df(tickers_list)
        print(stock_df)
      
        # Select good stocks
        # You can set your good_stocks_criteria here
        good_stocks_criteria = 20 # 20% increase
        good_stocks = stock_df[(stock_df['EPS%'] > good_stocks_criteria)
                                & (stock_df['REV%'] > good_stocks_criteria)]
        
        print('\nAnalyzing...\n')

        if good_stocks['TICKER'].count() > 0:
            print('----------GOOD STOCKS----------')            
            print(good_stocks)       
            print()     

            visualize_stocks_quarterly(good_stocks['TICKER'].tolist())
            visualize_stocks_annually(good_stocks['TICKER'].tolist())

            save = input('Do you want to save CSV (y/n) ? ')
            if save.lower() == 'y':
                good_stocks.to_csv('./python_good_stocks_df.csv', index=False)
                print('----------SAVED !!!----------')
            else:
                print('----------OK----------')
        else:
            print('----------NO GOOD STOCKS----------')
    except:
        pass 


if __name__ == '__main__':
  fire.Fire({
    'analyze': main
    })
