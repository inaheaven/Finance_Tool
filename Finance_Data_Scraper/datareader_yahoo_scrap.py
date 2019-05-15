import pandas_datareader.data as web
import datetime
import pandas as pd


StartDate = datetime.datetime(1990, 1, 1)
EndDate = datetime.datetime(2018, 12, 31)
gs = web.DataReader("005930.KS", "yahoo")
gs.to_csv("005930_KS.csv")

pd.set_option('display.max_columns', 26)
print(gs)


StartDate = datetime.datetime(2019, 1, 1)
EndDate = datetime.datetime(2019, 3, 31)
gs = web.DataReader("005930.KS", "yahoo")
gs.to_csv("005930_KS_TEST.csv")

pd.set_option('display.max_columns', 26)
print(gs)

# ma30 = gs['Adj Close'].rolling(window=30).mean()
# gs.insert(len(gs.columns), "MA30", ma30)
#
# import matplotlib.pyplot as plt
# plt.plot(gs['Adj Close'], label="Adj Close")
# plt.plot(gs['MA30'], label="MA30")
# plt.show()
# print(gs.info)
