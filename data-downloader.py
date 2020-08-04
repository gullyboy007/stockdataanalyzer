import os
import pandas as pd
import yfinance as yf
from datetime import date , timedelta


df = pd.read_csv('NSE-EQ-SYMBOLS.csv')

sym = []
sym = df['SYMBOL'].tolist()



def data_downloader(symbol):
    path = '/home/abhineet/py_files/PyPortfolioBuilder/stockdataanalyzer/nse-onemin-data'
    startTime = date(2020, 7, 1)
    nextTime = startTime + timedelta(days=+6)
    

    while(startTime <= date.today()):

        strTime = str(startTime)
        strNextTime = str(nextTime)
        if strTime[5] == '0' :
            strTime = strTime[:5] + strTime[6:]
        if strTime[8] == '0' :
            strTime = strTime[:8] + strTime[9:]
        if strNextTime[5] == '0' :
            strNextTime = strNextTime[:5] + strNextTime[6:]
        if strNextTime[8] == '0' :
            strNextTime = strNextTime[:8] + strNextTime[9:]            


        for i in range(0,len(symbol)):
            try:
                tickerData = yf.download(symbol[i]+'.NS',start=strTime, end=strNextTime, interval='1m')
                file_name = symbol[i] + '.txt'
                filePath = os.path.join(path,file_name)
                if os.path.exists(filePath):
                    append_write = 'a' # append if already exists
                else:
                    append_write = 'w' # make a new file if not
                try:

                    with open(filePath,append_write) as outfile:
                        tickerData.to_string(outfile, header=False)
                    outfile.close()
                except:
                    print("Error in Txt")
                    continue    
            except:
                print("Error in Symbol")
                continue
        startTime = startTime + timedelta(days=+6)
    print("End of Program")    
        
data_downloader(symbol=sym)
