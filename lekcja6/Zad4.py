import numpy as np

def funkcja(podstawapotegowania,n):
    return np.logspace(1.0, n, num=n, base = podstawapotegowania, dtype=int)

print(funkcja(2,4))