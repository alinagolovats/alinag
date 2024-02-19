#from string import*
#from random import*
#while True:
#    sym=input("Mis sümbol kasutame?")
#    if sym in punctuation: 
#        break
#    else:
#        print("Saab kasutada ainult:!#$%&'()*+,-./:;<=>?@[\]^_`{|}~.")
#while True:
#    try:
#        n=int(input("Ridade arv: "))
#        break
#    except TypeError:
#        print("Ainult täisarvanud")
#for i in range(n):
#    print(randint(1,50)*sym)



Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

while True:
    indeks=input("Indeks: ")
    if len(indeks)==5 and indeks.isdigit():
        break
    else:
        print("Ainult viienumbriline arv saab kontrollida")
print(indeks,"kasutatakse",Indeksid[int(indeks[0])-1],"piirkonnas")
if int(indeks[0]) in [1,2,3]:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")
