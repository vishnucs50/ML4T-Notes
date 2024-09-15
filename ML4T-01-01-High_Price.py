import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv('../VK-ML4TFa24/data/IBM.csv')
    print(df.columns)
    df['High'].plot()
    plt.show()

if __name__ == '__main__':
    test_run()