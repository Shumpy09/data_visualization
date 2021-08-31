from random import Random
import matplotlib.pyplot as plt
from numpy import intp

from random_walk import RandomWalk


# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny
while True:

    # Przygotowanie danych błądzenia loswego i wyświetlenia punktów
    rw = RandomWalk(5000)
    rw.fill_walk()

    # wyświetlenie punktów błądzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth = 2) #c=point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=1)

    # Podkreślenie pierwszego i ostatniego punkty błądzenia losowego
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Utworzyć kolejne błądzeni losowe (t/n): ")
    if keep_running == 'n':
        break