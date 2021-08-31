import plotly.graph_objs as G
from plotly import offline

from die import Die


# Utworzenie kości typu D8
die_1 = Die()
die_2 = Die()

# Wykonianie pewnej liczby rzutów i umieszczenie wyników na liście
'''results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
'''
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analiza wyników
'''frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
'''
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Wizualizacja wyników
x_values = list(range(2, max_result+1))
data = [G.Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = G.Layout(title='Wynik rzucania dwiema koścmi D8 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')