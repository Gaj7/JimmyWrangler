# See `notebooks/JW.ipynb` for descriptions of the dataframe manipulations
# and plots of the data.

import numpy as np
import pandas as pd

# First dataset
df = pd.read_csv("../data/cryptocurrencypricehistory/bitcoin_cash_price.csv")
df['Date']  = pd.to_datetime(df['Date'])

# Second dataset
df2 = pd.read_csv("../data/crypto-markets.csv")
df2 = df2[df2['symbol']=="BTC"]
df2 = df2.loc[:, ['date', 'open', 'high', 'low', 'close']]
df2['date']  = pd.to_datetime(df2['date'])

# Naive merge
df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
df2.columns =  ['Date', 'Open', 'High', 'Low', 'Close']
df3 = pd.concat([df, df2])

# Scale dataset 2 to 1
df2_overlapping = df2[(df2['Date'] >= df['Date'].min()) & (df2['Date'] <= df['Date'].max())]

def normalize(v):
    min1 = df['Open'].min()
    max1 = df['Open'].max()
    len1 = max1-min1
    min2 = df2_overlapping['Open'].min()
    max2 = df2_overlapping['Open'].max()
    len2 = max2-min2
    return (v - min2)*((len1)/(len2))+min1

df2_scaled = df2.copy()
df2_scaled.loc[:,['Open','High','Low','Close']] = df2_scaled.loc[:,['Open','High','Low','Close']].apply(normalize)
df2_scaled

# Merge scaled datsets
df4 = pd.concat([df, df2_scaled])
