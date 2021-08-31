import json

import plotly.graph_objs as Pg
from plotly import offline
import requests


# Analiza struktury danych
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

response_all_eq_dict = r.json()
all_eq_dicts = response_all_eq_dict['features']
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

dynamic_title = response_all_eq_dict['metadata']['title']

my_layout = Pg.Layout(title=dynamic_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake_test.html')