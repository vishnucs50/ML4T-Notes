from operator import index

import numpy as np
import pandas as pd

import os
import matplotlib.pyplot as plt

def sybmol_loc(symbol, base_dir = '../VK-ML4TFa24/data'):
    #return the path to the CSV
    return os.path.join(base_dir, f'{symbol[0]}.csv')

def create_df(symbol, date_range):
    df = pd.read_csv(sybmol_loc(symbol), index_col='Date', parse_dates=True, na_values='nan', usecols=['Date', 'Adj Close'])
    df_adjusted = pd.DataFrame(index = date_range)
    df_adjusted = df_adjusted.join(df)
    return df_adjusted.dropna(how='any')

def test_run():
    symbol = ['SPY']
    start_date = '2012-01-01'
    end_date = '2012-12-31'
    date_series = pd.date_range(start_date, end_date)
    df = create_df(symbol, date_series)
    return df

# calculate rolling mean of the df
def rolling_mean(df):
    days = 21
    return df.rolling(window=days).mean().dropna(how='any')
# calculate rolling std of the df
def rolling_std(df):
    days = 21
    return df.rolling(window=days).std().dropna(how='any')

if __name__ == '__main__':
    df = test_run()
    #Create a df that contains rolling mean
    rmean_df = rolling_mean(df)
    #create a df that contains rolling std
    rstd_df = rolling_std(df)
    std_upper_bound = rmean_df + rstd_df * 2

    std_lower_bound = rmean_df - rstd_df * 2

# This retains the axis
    ax = df.plot(title='SPY - rolling mean', color = 'blue', label = 'SPY', figsize = (10,6))

    rmean_df.plot(ax=ax, label = 'rolling mean', color = 'red')
    std_lower_bound.plot(ax=ax, label = 'std lower bound', color = 'yellow')
    std_upper_bound.plot(ax=ax, label = 'std upper bound', color = 'pink')

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc = 'upper left')
    plt.show()






