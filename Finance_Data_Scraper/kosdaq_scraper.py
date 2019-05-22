import urllib.parse
import pandas as pd
import csv
import pandas_datareader.data as web
import datetime

MARKET_CODE_DICT = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt',
    'konex': 'konexMkt'
}

DOWNLOAD_URL = 'kind.krx.co.kr/corpgeneral/corpList.do'
PORTAL = 'yahoo'
start_date = datetime.datetime(2008, 1, 1)
end_date = datetime.datetime(2019, 12, 31)


def download_stock_codes(market=None, delisted=False):
    try:
        params = {'method': 'download'}

        if market.lower() in MARKET_CODE_DICT:
            params['marketType'] = MARKET_CODE_DICT[market]

        if not delisted:
            params['searchType'] = 13
        params_string = urllib.parse.urlencode(params)
        request_url = urllib.parse.urlunsplit(['http', DOWNLOAD_URL, '', params_string, ''])
        df = pd.read_html(request_url, header=0)[0]
        df.종목코드 = df.종목코드.map('{:06d}'.format)
        df.to_csv('./KOSDAQ.csv', sep='\t', encoding='utf-8')
        return df

    except Exception as e:
        print('Errors While Scraping Index Data: ' + str(e))

    finally:
        temp_for_sort = []
        with open('./KOSDAQ.csv', 'rt', encoding='utf-8') as in_file:
            for sort_line in in_file:
                temp_for_sort.append(sort_line)
        temp_for_sort.sort()
        with open('./KOSDAQ.csv', 'w') as out_file:
            seen = set()
            for line in temp_for_sort:
                if line in seen:
                    continue
                else:
                    if not line == None:
                        seen.add(line)
                sorted(seen)
                out_file.write(line)

    print("Scraping Stock Index Data Completed.")



def stock_price_data(stocks, start_date, end_date):
    results = {}
    for code in kosdaq_stocks.종목코드:
        ticker = code+'.KQ'
        try:
            gs = web.DataReader(ticker, PORTAL, start_date, end_date)
            print("ticker:", ticker)
            gs['Adj Close'].to_csv('./kosdaq/{}.csv'.format(ticker), header=False)
        except Exception as e:
            print("Scarping Price Data of ", ticker, "is not accessible")
            pass
    # df = pd.concat(results, axis=1)
    # df.loc[:, pd.IndexSlice[:, 'Adj Close']].tail()
    # print(df)


kosdaq_stocks = download_stock_codes('kosdaq')
print(len(kosdaq_stocks))

# stock_price_data(kosdaq_stocks, start_date, end_date)
# print("KOSDAQ Scraping Completed.")