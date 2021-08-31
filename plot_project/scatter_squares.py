import matplotlib.pyplot as plt

x_values = range(100)
y_values = [x**3 for x in x_values]


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# zdefiniujemy tytuły wykresu i etykiet osi
ax.set_title("Sześciany liczb", fontsize = 24)
ax.set_xlabel("Watość", fontsize = 14)
ax.set_ylabel("Sześciany wartośći", fontsize = 14)

#zdefiniowanie zakresu dla każdej osi
ax.axis([0, 200, 0, 1000000])

# zdefiniujemy wielkość etykiet
ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()

# automatyczne zapisywanie wykresu do pliku
'''plt.savefig('squares_plot.png', bbox_inches='tight')'''