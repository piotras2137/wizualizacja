import numpy as np

a=np.arange(9).reshape(3,3)

b=a.ravel()

for i in b:
    print(i)