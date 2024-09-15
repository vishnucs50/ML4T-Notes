import pandas as pd

def get_mean_volume(symbol):

    stock = pd.read_csv(f'../VK-ML4TFa24/data/{symbol}.csv')
    return stock['Volume'].mean()

def test_run():
    stocks = ['AAPL', 'IBM']
    for stock in stocks:
        print(f"Stock: {stock}   Mean:{get_mean_volume(stock)}")



if __name__ == '__main__':
    test_run()

