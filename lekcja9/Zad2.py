import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)

lista = []
for x in dane['Imie']:
    if x[-1] == 'A':
        lista.append('kobieta')
    else:
        lista.append('mężczyzna')
dane['Plec'] = lista

grupa2 = dane.groupby(['Plec']).agg({'Liczba':['sum']})
grupa2.plot.bar()
plt.show()
