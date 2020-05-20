plik=open("podzielneprzez4.txt",'w')
for i in range(400):
    s=i*4
    plik.write(str(s))
    plik.write('\n')
plik.close()
