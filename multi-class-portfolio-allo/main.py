import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)
pd.set_option('display.max_columns', 50)

df = pd.read_csv('Case3HistoricalPrices.csv', index_col=0)  # set the first col is index
print(df.head())
df.columns

df.columns
df.columns
print(4)


# df.columns[0]
# df['S1'].shift(1)
# df[df.columns[0:2]]
# df[['S1','S2']]
#
# df[df.columns[0]]==df['S1'] #True
# df.columns[0]==df['S1'] #False


# df['shift']=df['S1'].shift(1)

def make_return_series(df):
    df['PctChg'] = (df[df.columns[0]] - df[df.columns[0]].shift(1)) / df[df.columns[0]].shift(1) * 100
    return df


print(3)
df = make_return_series(df)
df[df.columns[0]]
df['S1']
df.plot(figsize=(9, 6))
plt.show()
