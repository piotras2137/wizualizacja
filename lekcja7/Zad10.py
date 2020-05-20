import numpy as np

a = np.arange(81).reshape(9,9)

print(a)

b=a.ravel()

print(b)

c = a.reshape((3,27))
print(c)

#ilość kolumn razy ilość wierszy musi dać nam wynik 81
