class Material:
    rodzaj="filc"
    dlugosc=2.5
    szerokosc=3.5
    def __init__(self):
        print("stworzono material")
    def wyswietlnazwe(self):
        print(self.rodzaj)


class Ubranie(Material):
    kolor="zolty"
    rozmiar="xxl"
    dla_kogo="dla mnie"
    def __init__(self):
        print("stworzono ubranie")
    def wyswietldane(self):
        print(self.kolor," ",self.rozmiar, " ",self.dla_kogo)


class Sweter(Ubranie):
    rodzaj_swetra="golf"
    def __init__(self):
        print("stworzono swetr")
    def wyswietinfo(self):
        print(self.rodzaj_swetra)

filc=Material()
ubranko=Ubranie()
swetr=Sweter()