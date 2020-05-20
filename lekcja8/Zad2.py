import numpy as np
import pandas as pd
import xlrd
import openpyxl


Imiona=pd.ExcelFile('imiona.xlsx')
a=pd.read_excel(Imiona, 'Arkusz1')


print(a[a['Liczba']>1000])

print(a[a['Imie']=='DAMIAN'])

print(a['Liczba'].sum())

print(a.loc[((a.Rok > 1999) & (a.Rok < 2006)), ['Liczba']].sum())

print(a.groupby(a['Plec']).agg({'Liczba':['sum']}))

print(a.sort_values(by='Liczba').groupby(['Rok','Plec']).nth(-1))

print(a.sort_values(by='Liczba').groupby(['Plec']).nth(-1))
