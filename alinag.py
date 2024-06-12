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



#Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

#while True:
#    indeks=input("Indeks: ")
#    if len(indeks)==5 and indeks.isdigit():
#        break
#    else:
#        print("Ainult viienumbriline arv saab kontrollida")
#print(indeks,"kasutatakse",Indeksid[int(indeks[0])-1],"piirkonnas")
#if int(indeks[0]) in [1,2,3]:
#    print("Оставайтесь дома!")
#else:
#    print("Носите маски!")



import random

print("Tere tulemast mängu 'Kivi, paber, käärid'!")

rounds = int(input("Mitu vooru sa tahad mängida?"))

user_wins = 0
computer_wins = 0

for round_num in range(1, rounds + 1):
    print(f"\nÜmmargune {round_num}.")

    user_choice = input("Valige kivi, käärid või paber: ")
    while user_choice not in ['kivi', 'käärid', 'paber']:
        print("Vigane sisestus. Proovi uuesti.")
        user_choice = input("Valige kivi, käärid või paber: ")

    computer_choice = random.choice(['kivi', 'käärid', 'paber'])

    print(f"Te valite: {user_choice}")
    print(f"Arvuti valis: {computer_choice}")

    if user_choice == computer_choice:
        print("Loosimine!")
    elif (user_choice == 'kivi' and computer_choice == 'käärid') or \
         (user_choice == 'käärid' and computer_choice == 'paber') or \
         (user_choice == 'paber' and computer_choice == 'kivi'):
        print("Sina võitsid!")
        user_wins += 1
    else:
        print("Sa kaotasid.")
        computer_wins += 1
print(f"Mäng läbi. Mängija võidab: {user_wins}, võidab arvuti: {computer_wins}.")
