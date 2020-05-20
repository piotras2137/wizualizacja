def sprawdzenie(y1="2x+b", y2="2x+b"):
    lista1=y1.split()
    lista2=y2.split()
    if lista1[0][0]==lista2[0][0]:
        print("funkcje są równoległe")
    elif int(lista1[0][0])*int(lista2[0][0])==-1:
        print("funkcje są prostopadłe")
    else :
        print('te funkcje nie mają ze sobą nic wspolnego')
sprawdzenie()
