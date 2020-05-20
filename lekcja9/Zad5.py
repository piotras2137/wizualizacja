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

top = dane['Rok'].max()

dane2 = pd.read_csv('iris.data', sep=',', names=['sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class'])
grupa4 = dane2.copy()
grupa4['class'] = grupa4['class'].astype('|S')
grupa4.drop('petal length in cm', axis=1, inplace=True)
grupa4.drop('petal width in cm', axis=1, inplace=True)
lista1 = []
for x in grupa4['class']:
    if x == b'Iris-setosa':
        lista1.append('red')
    elif x == b'Iris-versicolor':
        lista1.append('blue')
    else:
        lista1.append('black')
grupa4['class'] = lista1



plt.show()


dane3 = pd.read_csv('zamowienia.csv', delimiter=';')
grupa5 = dane3.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})

grupa5.plot.bar()
plt.show()

