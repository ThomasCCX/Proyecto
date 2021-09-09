import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'name':['Jhon','Lisa','Peter','Carl','Linda','Betty'],
    'date_of_birth':['01/21/1988','03/10/1977','07/25/1999','01/22/1977','09/30/1968','09/15/1970'],
}

tabla = pd.DataFrame(datos)
tabla['date_of_birth'] = pd.to_datetime(tabla['date_of_birth'], infer_datetime_format=True)

plt.clf()
tabla['date_of_birth'].map(lambda d: d.month).plot(kind='hist')

plt.show()