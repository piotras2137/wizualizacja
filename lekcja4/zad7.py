#klasa robaczek 
class Robaczek:
    x=0
    y=0 
    krok=2
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ilosckrokow):
        self.y+=(ilosckrokow*self.krok)
    def idz_w_dol(self,ilosckrokow):
        self.y-=(ilosckrokow*self.krok)
    def idz_w_lewo(self,ilosckrokow):
        self.x-=(ilosckrokow*self.krok)
    def idz_w_prawo(self,ilosckrokow):
        self.x+=(ilosckrokow*self.krok)
    def pokaz_gdzie_jestes(self):
        print(self.x," ",self.y)
robak=Robaczek(1,0,2)
robak.pokaz_gdzie_jestes()