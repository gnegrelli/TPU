import pandas as pd

df = pd.read_csv('matriz_OD.csv')
df.fillna(0, inplace=True)

new_indices = {a: b for a, b in list(zip(df.index, df.columns))}
df.rename(index=new_indices, inplace=True)

df += df.T
df /= df.values.sum()

df *= 6300

df = df.applymap(round)

print(df)

# print(df.loc['1':'2', '3'], df.loc['1':'2', '3'].values.sum())
# print(df.loc['4':'5', '3'], df.loc['4':'5', '3'].values.sum())
# print(df.loc['1':'2', '4':'5'], df.loc['1':'2', '4':'5'].values.sum())

for i, zone in enumerate(df.index[:-1]):
    print(df.iloc[i, i+1:])
    print(df.loc[zone, zone:].values.sum() - df.loc[zone, zone])
    print(50*'-')
