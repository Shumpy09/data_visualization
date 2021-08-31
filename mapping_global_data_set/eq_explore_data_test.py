import json
import requests

# Analiza struktury danych
filename = 'data/eq_test.json'
#url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
#r = requests.get(url)
#print(f"Kod stanu: {r.status_code}")
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_test.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


# Analiza danych



'''
filename = 'data/eq_data_actual_m1.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_actual_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
'''
'''
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
'''