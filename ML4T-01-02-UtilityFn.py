import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir = '../VK-ML4TFa24/data'):
    return os.path.join(base_dir, f'{symbol}.csv')

def get_data(symbols, dates):
    df =pd.DataFrame(index = dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col = 'Date', usecols= ['Date', 'Adj Close'],
                              parse_dates=True, na_values = ['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp)
        df = df.dropna(how='any')
    return df

if __name__ == '__main__':
    symbols = ['AAPL', 'IBM', 'GOOG', 'GLD']
    start_date = '2010-01-01'
    end_date = '2010-01-31'
    dates = pd.date_range(start_date, end_date) # creates a panada series object with those dates
    df = get_data(symbols, dates)
    df.plot()
    plt.show()

