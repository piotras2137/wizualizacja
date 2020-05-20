
def monotonicznosc(y="-5x+6"):
    lista=y.split()
    print(lista)
    if(lista[0][0]=="-"):
        print("funkcja jest malejaca")
    else:
        if(int(lista[0][0])>0):
            print("funkcja jest rosnaca")
        if(int(lista[0][0])==0):
            print("funkcja jest stala")
monotonicznosc(y="3x+2")
monotonicznosc()