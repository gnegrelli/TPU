import numpy as np
import pandas as pd

from igraph import *

df = pd.read_csv('OD.csv')
df.fillna(0, inplace=True)

new_indices = {a: b for a, b in list(zip(df.index, df.columns))}
df.rename(index=new_indices, inplace=True)

df += df.T
df /= df.values.sum()

df *= 6300

df = df.applymap(round)

print('-- Daily demand matrix --')
print(df)
print('\n')

print('-- Occupation along route --')
passengers = 0
for i, zone in enumerate(df.index):
    print(zone, end=' ')
    if zone == df.index[-1]:
        break
    passengers += df.loc[zone, zone:].values.sum() - df.loc[zone, :zone].values.sum()
    print('---{}--→'.format(passengers), end=' ')
print('\n\n')

# Create graph and add its vertices and edges
g = Graph()
g.add_vertices(len(df))
g.add_edges([(i, j) for i in range(len(df)) for j in range(i+1, len(df))])

# Get demand on edges and normalize it
edge_weights = np.array([df.iloc[e.tuple[0], e.tuple[1]] for e in g.es])
edge_weights = 20*edge_weights/np.max(edge_weights)


g.vs['name'] = df.index
g.vs['label'] = g.vs['name']
g.vs['color'] = 'green'

layout = [(1, 1), (2, 1), (1.5, 2), (3, 1.5), (2.5, 0), (.5, 0), (0, 1.5), (3, 2.5)]

g.es['width'] = edge_weights

plot(g, layout=layout)
