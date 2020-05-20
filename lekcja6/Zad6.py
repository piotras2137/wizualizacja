import numpy as np

haslo1='Damian'
haslo2= np.array(list('Damian'))

pusta=np.ones((5,5))
poziomo=np.array([haslo2, pusta])
skos=np.diag([x for x in haslo1])

print(poziomo)
print(skos)