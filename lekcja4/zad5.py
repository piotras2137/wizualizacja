#klasa do ciągów arytmetycznych
class Ciag:
    a=1
    r=5
    n=3
    def __init__(self,a=1,r=5,n=3):
        self.a=a
        self.r=r
        self.n=n
    def pobierzelementy(self):
        print("nie ma")
        #tutaj jakies wygibasy beda

    def pobierzparametry(self,a,r):
        self.a=a
        self.r=r
    def policzsume(self):
        suma=0
        element=self.a
        for i in range(self.n):
            suma+=element
            element+=self.r
        print(suma)
    def policzelementy(self):
        element=self.a
        for i in range(self.n):
            print(i," ", element)
            element+=self.r

kek=Ciag(0,2,9)
kek.policzsume()
kek.policzelementy()
