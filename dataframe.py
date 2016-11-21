import pandas as pd

def test_run():
  # define date range
  start_date = '2016-09-01'
  end_date = '2016-09-08'
  dates = pd.date_range(start_date, end_date)

  # create an empty data frame
  df1 = pd.DataFrame(index=dates)

  # read SPY into temporary dataframe
  dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", 
                      parse_dates=True, usecols=['Date', 'Adj Close'],
                      na_values=['nan'])
  dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

  # join two data frames
  df1 = df1.join(dfSPY, how='inner')

  # read in more stocks
  symbols = ['GOOG', 'IBM', 'GLD']
  for symbol in symbols:
    df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", 
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])
    df_temp = df_temp.rename(columns={'Adj Close': symbol})
    df1 = df1.join(df_temp) # use default how='left'
  
  print df1

if __name__ == "__main__":
  test_run()
  