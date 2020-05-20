import numpy as np
import pandas as pd
import xlrd
import openpyxl


a = pd.read_csv('zamowienia.csv', sep=';')

print(a['Sprzedawca'].unique())

print(a.groupby(a['Sprzedawca']).agg({'idZamowienia':['count']}))

print(a.groupby(a['Kraj']).agg({'idZamowienia':['count']}))
