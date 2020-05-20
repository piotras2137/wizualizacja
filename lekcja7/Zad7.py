import numpy as np


sin=np.array([5, 4, 1, 2, 7, 3]).reshape(2, 3)

a=np.sin(sin)

cos=np.array([1, 3, 5, 7, 10, 12]).reshape(2, 3)

b=np.cos(cos)

print(a)
print("\n")
print(b)
print("\n")
print(a+b)