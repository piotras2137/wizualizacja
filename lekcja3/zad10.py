def lista(** rzeczy):
    ilosc=0
    for cos in rzeczy:
        print(cos," x ",rzeczy[cos])
        ilosc+=int(rzeczy[cos])
    return ilosc
a=lista(kebab=5,napoj=2)
print(a)