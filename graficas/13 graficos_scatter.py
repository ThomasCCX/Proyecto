import pandas as pd
import matplotlib.pyplot as plt

liquido_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

liquido_column_headers = [
    'Alcohol','Acido Malico','Cenizas','Alcalinidad de las cenizas',
    'Magnesio','Fenoles totales','Flavonooides',
    'Fenoles no flavonoides', 'Proantocianinas','Intensidad de color',
    'Matiz','OD280/OD315 de sustancia diluida','Prolina'
]
tabla_liquido = pd.read_csv(liquido_url, names=liquido_column_headers)

#Figure
fig, ax1 = plt.subplots()
fig.set_size_inches(13,10)

#Label
ax1.set_xlabel('Alcohol')
ax1.set_ylabel('Intensidad de color')
ax1.set_title('Relación entre la intensidad de color y la cantidad de alcohol en el liquido')

# C Sequence
c = tabla_liquido['Intensidad de color']

# Plot
plt.scatter(
    tabla_liquido['Alcohol'], tabla_liquido['Intensidad de color'], 
    c = c, cmap = 'RdPu', s = tabla_liquido['Prolina']*0.5, alpha=0.5
)
cbar = plt.colorbar()
cbar.set_label('Intensidad de color')
plt.show()
