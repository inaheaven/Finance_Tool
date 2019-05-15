from bs4 import BeautifulSoup
import csv
import os
import re
import requests

BaseUrl = 'http://finance.naver.com/sise/entryJongmok.nhn?&page='


for i in range(1, 22, 1):
    try:
        url = BaseUrl + str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.find_all('td', {'class': 'ctg'})
        for item in items:
            txt = item.a.get('href')
            k = re.search('[\d]+',txt)
            if k:
                code = k.group()
                name = item.text
                data = code, name
                with open ('KOSPI200.csv', 'a') as f:
                    writer=csv.writer(f)
                    writer.writerow(data)
    except:
        pass
    finally:
        temp_for_sort = []
        with open('KOSPI200.csv', 'r') as in_file:
            for sort_line in in_file:
                temp_for_sort.append(sort_line)
        print(temp_for_sort)
        with open('KOSPI200.csv', 'w') as out_file:
            seen = set()
            for line in temp_for_sort:
                if line in seen: continue
                seen.add(line)
                out_file.write(line)

