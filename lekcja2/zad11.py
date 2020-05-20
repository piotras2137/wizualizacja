#rysowanie diamentów z literek
from sys import *
wielkosc=int(input("podaj wielkosc diamenta"))
  #
 ###
#####
 ###
for i in range(1,wielkosc+1,1):
    for j in range(int((wielkosc-1)/2)):
        stdout.write(" ")
    for j in range(i):
        stdout.write("#")
    for j in range(int((wielkosc-1)/2)):
        stdout.write(" ")
    stdout.write('\n')    