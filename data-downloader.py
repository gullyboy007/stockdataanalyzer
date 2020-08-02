import os
import pandas as pd
import yfinance as yf


df = pd.read_csv('NSE-EQ-SYMBOLS.csv')

sym = []
sym = df['SYMBOL'].tolist()


def data_downloader(symbol):
    path = '/home/abhineet/py_files/PyPortfolioBuilder/nse_data'

    for i in range(0,len(symbol)):
        try:
            tickerData = yf.download(symbol[i]+'.NS'start="2020-7-20", end="2020-7-24", interval='1m')
            file_name = symbol[i] + '.csv'
            if tickerData['Open'][-1] > 30:
                tickerData.to_csv(os.path.join(path,file_name))
            else:
                print("error in else")
                continue
        except:
            print("error in except")
            continue
data_downloader(symbol=sym)
