import json

import plotly.graph_objs as Pg
from plotly import offline


# Analiza struktury danych
#url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

filename = 'data/eq_data_actual_m1.json'
with open(filename, encoding="utf-8")  as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:   
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Mapa trzęsień ziemi
# data = [Pg.Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Siła'},
    },
}]

dynamic_title = all_eq_data['metadata']['title']

my_layout = Pg.Layout(title=dynamic_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake.html')