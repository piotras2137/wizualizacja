import numpy as np
import pandas as pd
import xlrd
import openpyxl



Imiona=pd.ExcelFile('imiona.xlsx')

Data_Frame=pd.read_excel(Imiona, 'Arkusz1')

print(Data_Frame)