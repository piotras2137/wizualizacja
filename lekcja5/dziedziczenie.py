class typiarz():
    imie="kek"
    def __init__(self):
        print("stworzono typa")


    def dajdane(self,imie):
        self.imie=imie

class programista(typiarz):
    jezyk="python"
    def __init__(self):
        print("stworzono kodera")
    
piotras=typiarz()
piotras.dajdane("pioter")
mistrz=programista()
print(mistrz.imie)
mistrz.dajdane("adolf")
print(mistrz.imie)
mistrz=piotras
print(mistrz.imie)