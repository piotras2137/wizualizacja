from sys import *
wielkosc=int(input("podaj wielkosc wiezy"))
for i in range(wielkosc):
    for j in range(i+1):
        stdout.write("H")
    stdout.write('\n')