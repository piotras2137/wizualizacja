import matplotlib.pyplot as plt
import numpy as np
import math 
import pandas as pd
import random


lista1 = [1/x for x in range(1,21)]
lista2 = [x for x in range(1,21)]
plt.plot(lista2, lista1, label='x^-1')

plt.axis([1, 20, 0, 1])

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()

plt.show()
