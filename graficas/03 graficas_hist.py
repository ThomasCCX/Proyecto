import matplotlib.pyplot as plt

datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30]
rango = [0,10,20,30,40]

plt.hist(datos, rango, histtype='bar', rwidth=0.8, color='lightgreen')

plt.title('Histograma')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.show()