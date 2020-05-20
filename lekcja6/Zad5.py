import numpy as np



def wektor(n):
    wektor=np.diag([n for n in range(n, 0, -1)])
    return wektor

print(wektor(5))