from math import *
def iloczynciagu(a1=1,r=2,ile=3):
    suma=a1
    a=a1
    for i in range(ile):
        a+=r
        suma*=a
    print(suma)
iloczynciagu()