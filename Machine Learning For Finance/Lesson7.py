import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def symbol_to_path(symbol, base_dir="Data/data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_tmp = pd.read_csv(symbol_to_path(symbol), usecols=['Date', 'Adj Close'], index_col='Date', parse_dates=True,
                             na_values=['NaN'])
        df_tmp = df_tmp.rename(columns={'Adj Close': symbol})
        df = df.join(df_tmp)
        df = df.dropna(subset=['SPY'])
        print(df)
    return df


def plot_data(df, title="STOCK PRICE"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0,:] = 0
    return daily_returns

def test_run():
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title= "Daily Returns")

    daily_returns.hist()

    plt.show()

    # daily_returns['SPY'].hist(bins=20, label='SPY')
    # daily_returns['XOM'].hist(bins=20, label='XOM')
    # plt.legend(loc='upper right')
    # plt.show()
    # print("kurtosis", daily_returns.kurtosis())
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    beta_xom, alpha_xom = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    plt.plot(daily_returns['SPY'], beta_xom*daily_returns['SPY'] + alpha_xom, '-', color = 'r')
    plt.show()


    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_gld, alpha_gold = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    plt.plot(daily_returns['SPY'], beta_gld*daily_returns['SPY'] + alpha_gold, '-', color = 'r')
    plt.show()

    print(daily_returns.corr(method='pearson'))
if __name__ == "__main__":
    test_run()

