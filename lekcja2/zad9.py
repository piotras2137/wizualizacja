liczba=int(input("podaj wielocyfrowa liczbe"))
duza=1
while duza<liczba:
    duza*=10
suma=0
while duza>1:
    suma+=liczba/duza
    liczba%=duza
    duza/=10
print(suma)