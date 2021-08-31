import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    '''
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    '''

    # Pobranie ilosci opadów z pliku
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rain = float(row[3])
        dates.append(current_date)
        rains.append(rain)

# Wygenerowanie wykresu dla opadów
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue', alpha=0.5)

# Formatowanie wykresu
ax.set_title("Opady dzienne 2018\nDolina Śmierci", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Ilość opadów', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()