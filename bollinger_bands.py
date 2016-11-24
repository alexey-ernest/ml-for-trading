
import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df

def test_run():

    # Define a date range
    dates = pd.date_range('2015-11-23', '2016-11-18')

    # Choose stock symbols to read
    symbols = ['SPY']
    
    # Get stock data
    df = get_data(symbols, dates)
    
    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title='SPY Bollinger Bands', label='SPY')

    # Compute rolling mean using a 20-day window
    rm_SPY = df['SPY'].rolling(window=20).mean()

    # Compute rolling std
    rstd_SPY = df['SPY'].rolling(window=20).std()

    # Compute bollinger upper and lower bands
    uband = rm_SPY + 2 * rstd_SPY
    lband = rm_SPY - 2 * rstd_SPY

    # Add rolling mean and bollinger bans to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)
    uband.plot(label='Upper band', ax=ax)
    lband.plot(label='Lower band', ax=ax)

    # Add exis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()
