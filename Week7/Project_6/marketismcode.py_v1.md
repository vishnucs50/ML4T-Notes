```py
def compute_portvals(trades, start_val=100000, commission=0.00, impact=0.00):
    # Get unique symbols and date range from the trades DataFrame
    symbols = trades["Symbol"].unique()
    dates = pd.to_datetime(trades["Date"].unique())  # Ensure dates are in datetime format
    start_date = dates.min()
    end_date = dates.max()

    # Create prices DataFrame for symbols
    prices_df = get_data(symbols, pd.date_range(start_date, end_date))
    prices_df["Cash"] = 1.0  # To track cash

    # Create trades DataFrame based on positions and shares
    trade_df = pd.DataFrame(0.0, index=prices_df.index, columns=prices_df.columns)
    for index, row in trades.iterrows():
        date = row["Date"]
        symbol = row["Symbol"]
        order = row["Order"]
        shares = row["Shares"]

        if order == 'BUY':
            trade_df.loc[date, symbol] += shares
            final_price = prices_df.loc[date, symbol]
            cash_spent = (final_price * shares) + commission
            trade_df.loc[date, "Cash"] -= cash_spent
        elif order == 'SELL':
            trade_df.loc[date, symbol] -= shares
            final_price = prices_df.loc[date, symbol]
            cash_gained = (final_price * shares) - commission
            trade_df.loc[date, "Cash"] += cash_gained

    # Compute holdings and cash
    holdings_df = trade_df.cumsum()
    holdings_df["Cash"] += start_val

    # Compute portfolio values
    values_df = prices_df * holdings_df
    portvals = values_df.sum(axis=1)

    return portvals
```