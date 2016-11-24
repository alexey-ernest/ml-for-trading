"""
Optimizes portfolio allocations according to Sharpe ratio
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

from utils import get_data, plot_data

def error(allocs, df, risk_free):
  """Calculats error as -(sharpe ratio) to minimize"""

  # Normalize prices
  norm_df = df/df.ix[0]

  # Allocations
  alloc_df = norm_df * allocs

  # Portfolio values over time
  port_allocs_df = alloc_df.sum(axis=1)

  # Compute daily returns of the portfolio
  daily_returns = port_allocs_df/port_allocs_df.shift(1) - 1
  daily_returns = daily_returns[1:]

  # Calculate annual sharpe ratio for daily samples
  sharpe_ratio = (daily_returns.mean() - risk_free) / daily_returns.std() * np.sqrt(252)

  return -sharpe_ratio

def optimize(df, allocations=None, risk_free=0):
  if allocations == None:
    allocations = [1.0/df.shape[0]] * df.shape[0]

  cons = ({'type': 'ineq', 'fun': lambda x: x},
          {'type': 'eq', 'fun': lambda x: sum(x) - 1})
  result = spo.minimize(error, allocations, args=(df,risk_free), constraints=cons, method='SLSQP', options={'disp': True})
  return result.x

def test_run():
  dates = pd.date_range('2015-11-23', '2016-11-18')
  symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
  df = get_data(symbols, dates)
  allocations = [.25] * len(symbols)

  optimized_allocs = optimize(df, allocations)
  print 'Optimized portfolio:'
  print zip(symbols, optimized_allocs)

if __name__ == '__main__':
  test_run()