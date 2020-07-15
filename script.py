import numpy as np
import pandas as pd

from pathlib import Path

from igraph import *


def daily_demand(path, peak='morning', passengers=None, verbose=False):
    assert Path(path).exists(), 'Invalid path: {}'.format(path)
    assert path.endswith('.csv'), 'Only .csv files are supported'

    assert peak in ['morning', 'daily'], 'Valid values for argumetn \'peak\' are \'morning\' and \'daily\'. {} is ' \
                                         'not valid'.format(peak)

    if passengers is not None:
        assert isinstance(passengers, int) and passengers > 0, 'Number of daily passengers must be a positive integer'

    # Read Origin-Destiny matrix from file and treat missing data
    df = pd.read_csv(path)
    df.fillna(0, inplace=True)
    df = df.astype(int)

    # Rename indices to match column names
    new_indices = {a: b for a, b in list(zip(df.index, df.columns))}
    df.rename(index=new_indices, inplace=True)

    # Add transponse of OD matrix to obtain number of passengers during daily peak (morning and afternoon)
    if peak == 'morning':
        df += df.T

    if passengers is not None:
        # Obtain percentage of passengers in routes during day
        df /= df.values.sum()

        # Obtain daily number of passenger for each route
        df *= passengers
        df = df.applymap(round)

    if verbose:
        print('-- Daily demand matrix --')
        print(df)
        print('\n')

    return df


def occupation(dem, route=None):
    assert isinstance(dem, pd.DataFrame), 'Daily demand must be provided in a pandas DataFrame'

    if route is not None:
        assert isinstance(route, list), 'Route must be given in a list format'
        assert set(route).issubset(set(dem.index)), 'Route must contain only stops listed in demand matrix'
    else:
        route = list(dem.index)

    print('-- Occupation along route --')
    passengers = 0
    for zone in route:
        print(zone, end=' ')
        if zone == route[-1]:
            break
        zone_id = route.index(zone)
        passengers += dem.loc[zone, route[zone_id:]].values.sum() - dem.loc[zone, route[:zone_id + 1]].values.sum()
        print('---{}--→'.format(passengers), end=' ')
    print('\n\n')

# # Create graph and add its vertices and edges
# g = Graph()
# g.add_vertices(len(df))
# g.add_edges([(i, j) for i in range(len(df)) for j in range(i+1, len(df))])
#
# # Get demand on edges and normalize it
# edge_weights = np.array([df.iloc[e.tuple[0], e.tuple[1]] for e in g.es])
# edge_weights = 10*edge_weights/np.max(edge_weights)
#
#
# g.vs['name'] = df.index
# g.vs['label'] = g.vs['name']
# g.vs['color'] = 'green'
#
# layout = [(1.25, 2.25), (2.25, 2.25), (1.75, 1), (3, 2), (2.5, 4), (1, 4), (0.5, 2), (3.25, 0)]
#
# g.es['width'] = edge_weights
#
# plot(g, layout=layout)


if __name__ == '__main__':
    dem = daily_demand('matriz_OD.csv', passengers=6300, verbose=True)
    occupation(dem, route=['1', '3', '5'])
