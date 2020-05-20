from itertools import *
kek=combinations(range(1,10),3)
for i in kek:
    print(i)

def generowanie(zbior,ilosc):
    wynik=combinations(zbior,ilosc)
    return wynik

kek=generowanie("wykop.pl",5)
for i in kek:
    print(i)