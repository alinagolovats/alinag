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

print("Добро пожаловать в игру Камень, Ножницы, Бумага!")
while True:
    try:
        num_rounds = int(input("Сколько раундов вы хотите сыграть? "))
        break
    except ValueError:
        print("Неверный ввод. Введите целое число.")
rounds_played = 0
user_wins = 0
computer_wins = 0
while rounds_played < num_rounds:
    user_choice = input("Выберите камень, ножницы или бумагу (для выхода введите 'выход'): ").lower()
    if user_choice == "выход":
        break
    if user_choice not in ["камень", "ножницы", "бумага"]:
        print("Неверный ввод. Попробуйте еще раз.")
        continue
    computer_choice = random.choice(["камень", "ножницы", "бумага"])
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
        user_wins += 1
    else:
        print("Компьютер выиграл!")
        computer_wins += 1
    rounds_played += 1
print(f"Игра завершена. Выигрышей игрока: {user_wins}, выигрышей компьютера: {computer_wins}.")