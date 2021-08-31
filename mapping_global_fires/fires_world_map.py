import csv

import plotly.graph_objs as PG
from plotly import offline
from datetime import datetime

num_rows = 50000

# Analiza struktury danych
#filename = 'data/MODIS_C6_1_Europe_48h.csv'
filename = 'data/MODIS_C6_1_Global_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, brigs, lons, lats, hover_texts = [], [], [], [], []
    row_num = 0

    for row in reader:
        date = datetime.strptime(row[5], "%Y-%m-%d")
        brig = float(row[2])
        lon = float(row[1])
        lat = float(row[0])
        label = f'{brig}'

        dates.append(date)
        brigs.append(brig)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(label)

        # warunek wstrzymujący wczytywanie kolejnych danych
        row_num += 1
        if row_num == num_rows:
            break

# Mapa pożarów 
#data = [PG.Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker' :{
        #'size': [brig/10 for brig in brigs],
        'color': brigs,
        'colorscale': 'YlOrRd',
        #'reversescale': True,
        'colorbar': {'title': 'Intensywność pożarów'},
    },
}]

my_layout = PG.Layout(title='Pożary na świecie')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')