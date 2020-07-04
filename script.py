import pandas as pd

df = pd.read_csv('matriz_OD.csv')
df.fillna(0, inplace=True)

new_indices = {a: b for a, b in list(zip(df.index, df.columns))}
df.rename(index=new_indices, inplace=True)

df += df.T
df /= df.values.sum()

df *= 6300

df = df.applymap(round)

print('-- Daily demand matrix --')
print(df)
print('\n\n')

print('-- Occupation along route --')
passengers = 0
for i, zone in enumerate(df.index):
    print(zone, end=' ')
    if zone == df.index[-1]:
        break
    passengers += df.loc[zone, zone:].values.sum() - df.loc[zone, :zone].values.sum()
    print('---{}--→'.format(passengers), end=' ')
