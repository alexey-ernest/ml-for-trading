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
  symbols = ['SPY']
  df = get_data(symbols, dates)

  # Compute daily returns
  daily_returns = compute_daily_returns(df)

  # Plot a histogram
  daily_returns.hist(bins=20)
  
  # Get mean and standard diviation
  mean = daily_returns['SPY'].mean()
  std = daily_returns['SPY'].std()

  plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
  plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
  plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

  # Compute kurtosis
  print 'kurtosis\n', daily_returns.kurtosis()

  plt.show()

if __name__ == '__main__':
  test_run()