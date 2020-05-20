#klasa słowa
class Slowa:
    slowo1="arka"
    slowo2="gdynia"
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def czypalindrom(self):#czy od przodu i od tyłu są takie same
        isit=True
        for i in range(int(len(self.slowo1)/2)):
            if(self.slowo1[i]!=self.slowo1[len(self.slowo1)-1-i]):
                isit=False
        if isit==False:
            print("nie jest")
        else:
            print("jest")
        #do dokonczenia
    def czymetagramy(self):#czy róznia sie jedna litera
        print("nie")
        #do dokonczenia
    def czyanagramy(self):#czy maja taki sam zestaw liter
        print("nie")
        #do dokonczenia
    def wyswietlwyrazy(self):
        print(self.slowo1)
        print(self.slowo2)
kek=Slowa("poliilap","swinie")
kek.wyswietlwyrazy()
kek.czypalindrom()