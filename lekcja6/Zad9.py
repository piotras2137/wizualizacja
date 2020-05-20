import numpy as np

mat = np.arange(25)
mat[0] = 0
mat[1] = 1
for x in range(2,25):
    mat[x] = mat[x-1]+mat[x-2]

mat = mat.reshape((5,5))
print(mat)