#from operator import truediv
#from pickle import TRUE


#def korrutis(arv1:float,arv2:float,arv3:float,arv4=1.0)->float:
#    """Funktsioon tagastab 4 arvude korrutis, arvud sisestab kasutaja. Vaikimisi arv4=1.0. Tulemus tagastatakse float formaadis

#    :param float arv1: sisestatakse nagu parameeter
#    :param float arv2: sisestatakse nagu parameeter
#    :param float arv3: sisestatakse nagu parameeter
#    :param float arv4: sisestatakse nagu parameeter, vaikimisi võrdub ühega
#    :rtype: float
#    """
#    k=arv1*arv2*arv3*arv4
#    return k
#def suurim_element(arvud1:list,arvud2:list):
#    """Funktsioon kuvab ekraanile suurim arv listidest.

#    :param list arvud1: Arvude loetelu
#    :param list arvud2: Arvude loetelu
   
#    """
#    suurim1=max(arvud1)
#    suurim2=max(arvud2)
#    suurim=max(suurim1,suurim2)
#    print(suurim)


#def arithmetic(arv1:float,arv2:float,sümbol:str)->any:
#    """Funktsioon tagastab aritmeetiliste tehtede tulemused
#    + - liitumine
#    - - lahutamine
#    * - korrutamine
#    / - jagamine
#    : param float arv1: ujukomaarv mis sisestab kasutaja
#    : param float arv2: ujukomaarv mis sisestab kasutaja
#    : param str sümbol: sõne/tehe mis sisestab kasutaja
#    """
#    if sümbol=="+":
#        vastus=arv1+arv2
#    elif sümbol=="-":
#        vastus=arv1-arv2
#    elif sümbol=="*":
#        vastus=arv1*arv2
#    elif sümbol=="/":
#        if arv2==0:
#            vastus=="DIV0"
#        else:
#            vastus=arv1/arv2
#    else:
#        vastus="Tundmatu operatsioon"
#    return vastus



#def is_year_leap(aasta:int)->bool:
#    """Funktsioon tagastab True, kui aasta on liigaasta või False kui aasta on tavaline.
#    :param int aasta: Kasutaja sisestab aasta number
#    :rtype:bool
#    """
#    if aasta%4==0:
#        vastus=True 
#    else:
#        vastus=False 
#    return vastus



from string import*
from time import sleep
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioonid tagastab täidetud kasutaja list ja parool list:
    :param list kasutajad:kasutajate list
    :param list paroolid:paroolide list
    :rtype: list,list
    """
    while True:
        nimi=input("Sisesta kasutajanimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Sisesta salasõna? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna")
            break
        else:
            print("Selline kasutaja on juba olemas")
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas

    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast!{nimi}")
                        break
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")
        
def nimi_või_parooli_muutmine(list_:list):
    """

    """
    muutuja=input("Sisesta vana andmeid: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Sisesta uut andmet: ")
        list_[indeks]=muutuja
    return list_


def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist

    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse

    """
    n=int(input("Mitu: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'a',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()

def ümber_kirjuta_fail(fail:str):
    f=open(fail,'w')
    text=input("Sisesta teksti: ")
    f.write(text+"\n")
    f.close()

def failide_kustutamine()
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
