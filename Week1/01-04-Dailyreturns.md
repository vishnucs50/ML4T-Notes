1. Daily returns is a very important statistics used in financial analysis.
2. Its how much the stock went up or down on a given day
3. Calculation:
```
daily_return = (todays_price / previous_day_price) - 1
```
4. Code:
```py
def daily_returns(dataframe):
    daily_returns = dataframe.copy()
    daily_returns[1:] = (dataframe[1:]/dataframe[:-1].values) - 1
    # print(daily_returns)
    return daily_returns
```
5. Easier to do with pandas:
```py
def daily_returns(dataframe):
    daily_retuns = (dataframe/dataframe.shift(1)) - 1
    # pandas tend to create 1st row with full of nan values after above code. Therefore do below
    daily_returns[0,:] = 0
    return daily_returns

```