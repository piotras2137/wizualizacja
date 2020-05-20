import numpy as np



def generuj(n):
    tablica=np.diag([2 for a in range(n)])
    for i in range(1, n):
        a=np.diag([2*(i+1) for a in range(n-i)],+i)
        b=np.diag([2*(i+1) for a in range(n-i)],-i)
        tablica=tablica+a+b
    return tablica

print(generuj(10))
