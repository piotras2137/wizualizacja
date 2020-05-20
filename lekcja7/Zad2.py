import numpy as np

macierz1=np.arange(9).reshape(3, 3)
macierz2=np.arange(16).reshape(4, 4)

print(macierz1)
print(macierz2)

print("\n")

print(macierz1.min(axis=1))
print("\n")
print(macierz2.min(axis=1))
print("\n")
print(macierz1.min(axis=0))
print("\n")
print(macierz2.min(axis=0))