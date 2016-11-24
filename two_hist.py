import pandas as pd
import matplotlib.pyplot as plt

from utils import get_data, plot_data

def compute_daily_returns(df):
  """Compute and return the daily return values."""
  daily_returns = df.copy()
  daily_returns[1:] = (df[1:]/df[:-1].values) - 1 # to avoid index matching
  daily_returns.ix[0, :] = 0
  return daily_returns

def test_run():
  dates = pd.date_range('2015-11-23', '2016-11-18')
  symbols = ['SPY', 'XOM']
  df = get_data(symbols, dates)

  # Compute daily returns
  daily_returns = compute_daily_returns(df)

  # Plot a histogram
  daily_returns['SPY'].hist(bins=20, label='SPY')
  daily_returns['XOM'].hist(bins=20, label='XOM')
  plt.legend(loc='upper right')
  plt.show()

if __name__ == '__main__':
  test_run()