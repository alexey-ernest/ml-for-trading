import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from utils import get_data, plot_data

def compute_daily_returns(df):
  """Compute and return the daily return values."""
  daily_returns = df.copy()
  daily_returns[1:] = (df[1:]/df[:-1].values) - 1 # to avoid index matching
  return daily_returns

def portfolio_stats(start_val, symbols, allocs, start_date='2015-11-23', end_date='2016-11-18', risk_free=0):
  """Calculates annual sharpe ratio for a portfolio"""
  dates = pd.date_range(start_date, end_date)

  df = get_data(symbols, dates)

  # Normalize prices
  norm_df = df/df.ix[0]

  # Allocations
  alloc_df = norm_df * allocs

  # Position values
  pos_vals_df = alloc_df * start_val

  # Portfolio values over time
  port_vals_df = pos_vals_df.sum(axis=1)

  # Calculate daily returns for the portfolio
  daily_returns = compute_daily_returns(port_vals_df)
  daily_returns = daily_returns[1:] # excluding day 0
  
  # Calculate annual sharpe ratio for daily samples
  sharpe_ratio = (daily_returns.mean() - risk_free) / daily_returns.std() * np.sqrt(252)

  return port_vals_df, daily_returns, (port_vals_df[-1]/start_val - 1), sharpe_ratio


def test_run():
  port_vals, daily_returns, cum_ret, sharpe_ratio = portfolio_stats(1000000, ['SPY', 'XOM', 'GOOG', 'GLD'], [.4, .4, .1, .1])
  print 'Cumulative return:', cum_ret
  print 'Sharpe ratio:', sharpe_ratio
  
  plot_data(port_vals, title='Portfolio value', ylabel='Portfolio value')
  #plot_data(daily_returns, title='Portfolio daily returns', ylabel='Daily returns')

if __name__ == '__main__':
  test_run()