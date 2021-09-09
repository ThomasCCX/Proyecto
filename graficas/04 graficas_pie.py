import matplotlib.pyplot as plt

valores = [20,40,60,80]

plt.pie(valores, 
    labels=['Prekinder', 'Kinder', 'Primaria', 'Secundaria'], 
    colors=['red','purple','blue','orange'],
    startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

plt.title('Gráfico de torta')

plt.show()