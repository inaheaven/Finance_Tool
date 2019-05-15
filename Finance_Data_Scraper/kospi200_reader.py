import glob
import os
import csv


file_names = [os.path.basename(x) for x in glob.glob('./kospi200/*.csv')]
tickers = []
prices = []
stock_prices = []
count = 0
num_of_stock = len(file_names)
for file_name in file_names:
    if count < num_of_stock:
        with open('./kospi200/'+file_names[count], 'r') as in_file:
            reader = csv.reader(in_file, delimiter=",")
            for price in reader:
                prices.append(price[1])
    count += 1
    stock_prices.append(prices)

print(stock_prices)

