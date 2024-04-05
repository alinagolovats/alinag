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

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

rounds = int(input("Сколько раундов вы хотите сыграть? "))

user_wins = 0
computer_wins = 0

for round_num in range(1, rounds + 1):
    print(f"\nРаунд {round_num}.")

    user_choice = input("Выберите камень (к), ножницы (н) или бумагу (б): ")
    while user_choice not in ['к', 'н', 'б']:
        print("Неверный ввод. Попробуйте снова.")
        user_choice = input("Выберите камень (к), ножницы (н) или бумагу (б): ")

    computer_choice = random.choice(['к', 'н', 'б'])

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'к' and computer_choice == 'н') or \
         (user_choice == 'н' and computer_choice == 'б') or \
         (user_choice == 'б' and computer_choice == 'к'):
        print("Вы победили!")
        user_wins += 1
    else:
        print("Вы проиграли.")
        computer_wins += 1
print(f"Игра завершена. Выигрышей игрока: {user_wins}, выигрышей компьютера: {computer_wins}.")
