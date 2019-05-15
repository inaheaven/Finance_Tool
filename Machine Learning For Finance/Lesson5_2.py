import pandas as pd
import matplotlib.pyplot as plt
import os


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


def normalize_data(df):
    return df / df.ix[0, :]


def plot_data(df, title="STOCK PRICE"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    plot_data(df.ix[start_index: end_index, columns], title="STOCK PRICE")


def test_run():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    print("df", df)
    # df = normalize_data(df)

    # plot_selected(df, ['GOOG', 'SPY', 'IBM', 'GLD'], '2010-01-01', '2010-05-01')
    # print("MEAN", df.mean())
    # print("MEDIAN", df.median())
    # print("STD", df.std())

    ax = df['SPY'].plot(title="SPY ROLLING MEAN", label='SPY')
    rm_SPY = df['SPY'].rolling(20).mean()
    rm_SPY.plot(label="Rolling mean", ax = ax)

    ax.set_xlabel("DATE")
    ax.set_ylabel("PRICE")
    ax.legend(loc="upper left")
    plt.show()

if __name__ == '__main__':
    test_run()