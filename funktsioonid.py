#from minuomamoodul import*
#from random import*

#a=randint(-10,10)
#print("Esimene arv=",a)
#b=float(input("Teine arv:"))
#kor=korrutis(a,b,5.5)
#print("Tulemus: ",kor)
#kor=korrutis(b,a,b,10)
#print(f"Tulemus: {b}*{a}*{b}*10=",kor)

#from minuomamoodul import*
#from random import*


##1 arithmetic() funktsiooni kasutamine
#v=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Operatsioon: "))
#print(v)

##2 liigaasta
#vastus=is_year_leap
#int(input("Aasta: "))
#if vastus:
#    print("Liigaasta")
#else:
#    print("Tavaline aasta")


#a=[]
#b=[]


#for i in range(5):
#    a.append(randint(-20,20))
#for i in range(1,4):
#    arv=int(input(f"{i}. arv"))
#    b.append(arv)
#print(a)
#print(b)
#print()
#suurim_element(a,b)

#a=randint(-10,10)
#print("Esimene arv=",a)
#b=float(input("Teine arv:"))
#kor=korrutis(a,b,5.5)
#print("Tulemus: ",kor)
#kor=korrutis(b,a,b,10)
#print(f"Tulemus: {b}*{a}*{b}*10=",kor)

from minuomamoodul import*

salasõnad=loe_failist("Salasõnad.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nimi või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
        def kirjuta_failisse(fail: str, järjend=[]):
            with open(fail, 'w', encoding="utf-8") as f:
                for element in järjend:
                    f.write(element + "\n")
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
    vastus=input("Kas muudame nime või parooli")
    if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
    elif vastus=="parool":
            salasõnad=nimi_või_parooli_muutmine(salasõnad)
    elif vastus=="mõlemad":
        print("Nimi muutmine")
        kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
        print("Parooli muutmine")
        salasõnad=nimi_või_parooli_muutmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")


    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
