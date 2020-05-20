import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
c = np.arange(12).reshape(2, 6)

A=a.ravel()
B=b.ravel()
C=c.ravel()

print(A)
print(B)
print(C)