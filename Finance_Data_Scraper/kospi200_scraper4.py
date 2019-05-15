import urllib.parse
import pandas as pd

MARKET_CODE_DICT = {
    'kospi' : 'stockMkt',
    'kosdaq' : 'kosdaqMkt',
    'konex' : 'konexMkt'
}

DOWNLOAD_URL = 'kind.krx.co.kr/corpgeneral/corpList.do'

def stock_codes(market=None, delisted=False):
    params = {'method':'download'}

    if market.lower() in MARKET_CODE_DICT:
        params['marketType'] = MARKET_CODE_DICT[market]
        
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 12, 31)

gs = web.DataReader("078930.KS", "yahoo", start, end)
print(gs['High'])
gs.info()



ma30 = gs['Adj Close'].rolling(window=30).mean()
print(ma30.tail(10))
gs.insert(len(gs.columns), "MA30", ma30)


import matplotlib.pyplot as plt
plt.plot(gs['Adj Close'])
plt.plot(gs['MA30'], label = "MA30")
plt.show()
print(gs.info())