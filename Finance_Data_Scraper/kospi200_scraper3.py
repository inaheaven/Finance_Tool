import urllib.parse
import pandas as pd

MARKET_CODE_DICT = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt',
    'konex': 'konexMkt'
}

DOWNLOAD_URL = 'kind.krx.co.kr/corpgeneral/corpList.do'

def download_stock_codes(market=None, delisted=False):
    params = {'method': 'download'}

    if market.lower() in MARKET_CODE_DICT:
        params['marketType'] = MARKET_CODE_DICT[market]

    if not delisted:
        params['searchType'] = 13

    params_string = urllib.parse.urlencode(params)
    request_url = urllib.parse.urlunsplit(['http', DOWNLOAD_URL, '', params_string, ''])

    df = pd.read_html(request_url, header=0)[0]
    df.종목코드 = df.종목코드.map('{:06d}'.format)

    return df

kosdaq_stocks = download_stock_codes('kosdaq')
print(kosdaq_stocks.head())

from pandas_datareader import data

results = {}
for code in kosdaq_stocks.종목코드.head():
    results[code] = data.DataReader(code + '.KQ', 'yahoo', '2017-01-01', None)

df = pd.concat(results, axis=1)
df.loc[:, pd.IndexSlice[:, 'Adj Close']].tail()
print(df)