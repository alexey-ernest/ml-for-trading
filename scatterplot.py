import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from utils import get_data, plot_data

def compute_daily_returns(df):
  """Compute and return the daily return values."""
  daily_returns = df.copy()
  daily_returns[1:] = (df[1:]/df[:-1].values) - 1 # to avoid index matching
  daily_returns.ix[0, :] = 0
  return daily_returns

def test_run():
  dates = pd.date_range('2015-11-23', '2016-11-18')
  symbols = ['SPY', 'XOM', 'GLD']
  df = get_data(symbols, dates)

  # Compute daily returns
  daily_returns = compute_daily_returns(df)

  # Scatterplot SPY vs XOM
  daily_returns.plot(kind='scatter', x='SPY', y='XOM')
  beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1) # SPY = beta * XOM + alpha
  print 'beta_XOM=', beta_XOM
  print 'alpha_XOM=', alpha_XOM
  plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='r')

  # Scatterplot SPY vs GLD
  daily_returns.plot(kind='scatter', x='SPY', y='GLD')
  beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1) # SPY = beta * GLD + alpha
  print 'beta_GLD=', beta_GLD
  print 'alpha_GLD=', alpha_GLD
  plt.plot(daily_returns['SPY'], beta_GLD * daily_returns['SPY'] + alpha_GLD, '-', color='r')

  # Calculate correlation coeff
  print daily_returns.corr(method='pearson')

  plt.show()

if __name__ == '__main__':
  test_run()