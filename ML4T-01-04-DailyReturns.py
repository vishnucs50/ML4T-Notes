from cProfile import label

import pandas as pd
import os
import matplotlib.pyplot as plt
from numpy.core.defchararray import title


def sybmol_loc(symbol, base_dir = '../VK-ML4TFa24/data/'):
    #return the path to the CSV
    return os.path.join(base_dir, f'{symbol}.csv')

def create_df(symbol, date_range):
    # df = pd.read_csv(sybmol_loc(symbol), index_col='Date', parse_dates=True, na_values='nan', usecols=['Date', 'Adj Close'])
    df_adjusted = pd.DataFrame(index = date_range)
    # df_adjusted = df_adjusted.join(df)

    for items in symbol:
        df_temp = pd.read_csv(sybmol_loc(items), index_col = 'Date', usecols = ['Date', 'Close'], parse_dates = True, na_values='nan')
        df_temp = df_temp.rename(columns = {'Close': items})
        df_adjusted = df_adjusted.join(df_temp)
    return df_adjusted.dropna(how='any')

def daily_returns(dataframe):
    daily_returns = dataframe.copy()
    daily_returns[1:] = (dataframe[1:]/dataframe[:-1].values) - 1
    # print(daily_returns)
    return daily_returns

def test_run():
    symbol = ['SPY', 'XOM']
    start_date = '2012-07-01'
    end_date = '2012-07-31'
    date_series = pd.date_range(start_date, end_date)
    df = create_df(symbol, date_series)
    df2 = daily_returns(df)
    daily_returns(df)
    return df, df2


if __name__ == '__main__':
    df, daily_returns = test_run()

    plt.figure(figsize=(15, 6))
    df.plot(title = 'SPY-XOM')

    plt.figure(figsize=(15,6))
    daily_returns.plot(title = 'Daily returns')
    plt.ylim(-0.015, 0.020)
    plt.show()