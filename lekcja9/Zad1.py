import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)

grupa = dane.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot()
plt.show()