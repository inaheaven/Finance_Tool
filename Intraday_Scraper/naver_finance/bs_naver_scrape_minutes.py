
import os
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import timedelta
import datetime

base_url = 'http://finance.naver.com/item/sise_time.nhn?'
df = pd.read_csv('./KOSPI.csv', 'r', header=None, delimiter=',', dtype='str')
for df_index, df_row in df.iterrows():

    stockCode = df_row.iloc[0]
    daily_trade = pd.DataFrame(columns=['Date', 'Time', 'Price', 'Change', 'Total Volume'])
    for dates_index in range(0, 4):
        date = datetime.datetime.today() - datetime.timedelta(days=dates_index)
        date = date.strftime("%Y%m%d")
        marketclosetime = date + "16"

        if not os.path.exists('./naver_data/' + stockCode + "/"):
            os.makedirs('./naver_data/' + stockCode + "/")

        if not os.path.exists('./naver_data/' + stockCode + "/" + date + ".csv"):
            pg_url = '{url}&code={code}&thistime={time}&page={page}'.format(url=base_url, code=stockCode, time=marketclosetime, page=1)
            dayPriceHtml = urlopen(pg_url)
            dayPriceSource = BeautifulSoup(dayPriceHtml.read(), "html.parser")
            dayPricePageNavigation = dayPriceSource.find_all("table", align="center")
            dayPriceMaxPageSection = dayPricePageNavigation[0].find_all("td", class_="pgRR")
            if len(dayPriceMaxPageSection) != 0:
                print("STOCK CODE:", stockCode, marketclosetime, "- Downloading")
                dayPriceMaxPageNum = int(dayPriceMaxPageSection[0].a.get('href').split('page=')[1])
            else:
                print("STOCK CODE:", stockCode, marketclosetime, "- Not Available")
                continue
            day_list = []
            for page in range(dayPriceMaxPageNum, 0, -1):
                print("Current Page:", page)
                price_url = '{url}&code={code}&thistime={time}&page={page}'.format(url=base_url, code=stockCode, time=marketclosetime, page=page+1)
                html = urlopen(price_url)
                source = BeautifulSoup(html.read(), "html.parser")
                srlists = source.find_all("tr")
                isCheckNone = None
                for i in range(1, len(srlists) - 1):
                    if (srlists[i].span != isCheckNone):
                        time = srlists[i].find_all("td", align="center")[0].text
                        price = int(srlists[i].find_all("td", class_="num")[0].text.replace(",", ""))
                        volume = int(srlists[i].find_all("td", class_="num")[4].text.replace(",", ""))
                        change = int(srlists[i].find_all("td", class_="num")[5].text.replace(",", ""))
                        row = [date, time, price, change, volume]
                        day_list.append(row)
            daily_trade = daily_trade.append(pd.DataFrame(day_list, columns=['Date', 'Time', 'Price', 'Change', 'Total Volume']), ignore_index=True)
            daily_trade = daily_trade.sort_values(by=['Date', 'Time'], ascending=True)
            print("Completed")
        else:
            print("STOCK CODE:", stockCode, marketclosetime, "- Already Exists")
        daily_trade.to_csv('./naver_data/' + stockCode + "/" + date + ".csv")
