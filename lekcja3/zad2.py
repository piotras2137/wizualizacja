from math import *
from random import randint,seed
seed(1) 
macierz=list()
for i in range(4):
    linia=list()
    for j in range(4):
        linia.append(randint(1,10))
    macierz.append(linia)

print(macierz)
print(macierz[0][0])
print(macierz[1][1])
print(macierz[2][2])
print(macierz[3][3])
przekatna={macierz[i][i] for i in range(4)}