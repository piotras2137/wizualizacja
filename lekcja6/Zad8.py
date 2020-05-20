import numpy as np



def cut(a, direction):
    if(a.shape[0]%2 != 0):
        return "a.shape[0]%2 != 0"
    else:
        if(direction==1):
            return a[:int(a.shape[0]/2)]
        else:
            return np.hsplit(a, 2)[0]

a=np.arange(25)
a=a.reshape((5,5))

print(cut(a, 5))