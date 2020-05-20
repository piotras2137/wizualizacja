class NaZakupy:
    nazwa_produktu="mleko"
    ilosc=1
    jed_miary="litr"
    cena=2.30
    def __init__(self,nazwa_produktu,ilosc , jed_miary ,cena):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jed_miary=jed_miary
        self.cena=cena
    def wyswietl_produkt(self):
        print('nazwa ',self.nazwa_produktu)
        print("ilosc ",self.ilosc)
        print("jednostka ",self.jed_miary)
        print("cena za jednostke ",self.cena)
    def ile_produktu(self):
        print(nazwa," ",self.ilosc)
    def ile_kosztuje(self):
        print(self.cena*self.ilosc)
kebab=NaZakupy("kebab",1,"litr",10)
print(kebab)
kebab.wyswietl_produkt()