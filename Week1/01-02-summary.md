1. Specify a date range using pandas date_range method
    - it takes 2 arguments ***start_date*** ***end_date***
```python
import pandas as pd

start_date = 2010-01-01
end_date = 2010-01-26

dates = pd.date_range(start-date, end_date)
df = pd.DataFrame(index = dates)
```
2. Above creates an empty dataframe with the date ranges as index.
3. Read other csv files as data frames:
```py
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col = 'Date', usecols= ['Date', 'Adj Close'], parse_dates=True, na_values = ['nan'])
```
4. Every df will have the same column "Adj Close"
5. When we attempt to join df_temp with df, it will throw an error becuase:
    - Pandas need every column to be unique
6. Therefore, rename the "Adj Close" with the symbol name
```python
df_temp = df_temp.rename(columns = {'Adj Close': symbol})
```
7. Now join & drop na
```python
df = df.join(df_temp)
df = df.dropna(how='any')
```
```py
>>> np.max(mean_winnings + std_winnings)
32126.14
>>>np.min(mean_winnings - std_winnings)
-34158.99
```
```py
>>>earnings.mean(axis=1).mean()
>>>-40.34263636363636
 ```

 ```py
    >>>print(f'\nMean earnings per spin: {mean_earnings}')
    >>>Mean earnings per spin: [ 0.0000e+00 -3.4000e-02 -7.9000e-02 ... -4.5703e+01 -4.5703e+01 -4.5705e+01]
    >>>print(f'\nStd earnings per spin{std_earnings}')
    >>>Std earnings per spin[  0.           0.99942183   1.85654491 ... 162.35297592 162.35370889 162.35603461]
    >>>print(f'\n{mean_earnings.mean()}')
    >>>-40.34263636363637
    >>>print(f'\n{std_earnings.mean()}')
    >>>150.46635675514457
```