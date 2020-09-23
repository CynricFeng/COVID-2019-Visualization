import pandas as pd

df = pd.read_csv('./data/covid19_confirmed.csv')
df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)

df2.to_csv('./data/covid19_confirmed_line.csv')