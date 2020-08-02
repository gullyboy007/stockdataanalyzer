import os
import pandas as pd
import yfinance as yf
from datetime import date , timedelta


df = pd.read_csv('NSE-EQ-SYMBOLS.csv')

sym = []
sym = df['SYMBOL'].tolist()



def data_downloader(symbol):
    path = '/home/abhineet/py_files/PyPortfolioBuilder/stockdataanalyzer/nse-onemin-data'
    startTime = date(2020, 7, 3)
    nextTime = startTime + timedelta(days=+6)
    print(startTime)
    print(nextTime)

    while(startTime <= date.today()):

        for i in range(0,len(symbol)):
            try:
                tickerData = yf.download(symbol[i]+'.NS',start='2020-7-3', end='2020-7-6', interval='1m')
                file_name = symbol[i] + '.txt'
                filePath = os.path.join(path,file_name)
                if os.path.exists(filePath):
                    append_write = 'a' # append if already exists
                else:
                    append_write = 'w' # make a new file if not
                with open(filePath,append_write) as outfile:
                    df.to_string(outfile)
                outfile.close()
            except:
                print("error in except")
                continue
        startTime = startTime + timedelta(days=+6)
        
data_downloader(symbol=sym)
