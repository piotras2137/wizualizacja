#rysowanie tabliczki mnozenia
from sys import *
from string import *
for i in range(1,10,1):
    for j in range(1,10,1):
        s=i*j
        stdout.write("%d"%s)
        if(s<10):#tutaj to jest poto zeby bylo rowniej 
            stdout.write(" ")
        stdout.write(" ")
    stdout.write('\n')