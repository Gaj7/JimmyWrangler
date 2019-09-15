import numpy as np
import pandas as pd

df = pd.read_csv("../data/cryptocurrencypricehistory/bitcoin_cash_price.csv")
df['Date']  = pd.to_datetime(df['Date'])
df.plot(x='Date')

df2 = pd.read_csv("../data/crypto-markets.csv")
df2 = df2[df2['symbol']=="BTC"]
df2 = df2.loc[:, ['date', 'open', 'high', 'low', 'close']]
df2['date']  = pd.to_datetime(df2['date'])

df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
df2.columns =  ['Date', 'Open', 'High', 'Low', 'Close']
df3 = pd.concat([df, df2])
