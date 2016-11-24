
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

def plot_data(df, title='Stock Prices'):
    ax = df.plot(title=title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()

def test_run():
    # Define a date range
    dates = pd.date_range('2015-11-23', '2016-11-18')

    # Choose stock symbols to read
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    

    # compute global statistics for each stock
    print '\nMean:\n', df.mean()
    print '\nMedian:\n', df.median()
    print '\nStd:\n', df.std()

    plot_data(df)


if __name__ == "__main__":
    test_run()
