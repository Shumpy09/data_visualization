import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

# zdefiniujemy tytuły wykresu i etykiet osi
ax.set_title(" liczb", fontsize = 24)
ax.set_xlabel("Watość", fontsize = 14)
ax.set_ylabel("Kwadraty wartośći", fontsize = 14)

# zdefiniujemy wielkość etykiet
ax.tick_params(axis='both', labelsize = 14)


plt.show()