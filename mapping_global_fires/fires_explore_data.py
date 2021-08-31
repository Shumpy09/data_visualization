import csv

# Analiza struktury danych
filename = 'data/MODIS_C6_1_Global_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''
    for index, column_hader in enumerate(header_row):
        print(index, column_hader)
    '''
    brigs, lons, lats = [], [], []
    for row in reader:
        brig = float(row[2])
        lon = float(row[1])
        lat = float(row[0])
        brigs.append(brig)
        lons.append(lon)
        lats.append(lat)

    print(brigs[:10])
    print(lons[:5])
    print(lats[:5])    