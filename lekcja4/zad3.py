from sys import *
with open("kek.txt",'w') as plik:
    plik.write("raz\n")
    plik.write("dwa\n")
    plik.write("trzy\n")
    plik.write("cztery\n")
with open("kek.txt",'r') as plik:
    kek=plik.readline()
    while kek:
        print(kek)
        kek=plik.readline()