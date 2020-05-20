import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)

top = dane['Rok'].max()
grupa3 = dane[dane['Rok'] > top-5].groupby(['Plec']).agg({'Liczba':['sum']})
grupa3.plot.pie(subplots = True,autopct='%.2f %%')
plt.show()