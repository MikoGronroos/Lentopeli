#Heitetään kolme noppaa. Pelaaja saa tietää yhden heitetyn nopan tuloksen.
#Pelaajalla on kolme arvausta arvata heitettyjen noppien summa. Peli
#kertoo onko arvaus liian korkea/alhainen. Pelaaja maksaa x määrän kolikoita
#pelatakseen ja voittaessa kolikoiden määrä tuplaantuu.

import random

def dicegame():
    dicelist = []
    for i in range(3):
        dice = random.randint(1,6)
        dicelist.append(dice)
    return dicelist

def Game(moneyToGamble):
    moneyWon = 0
    print("Welcome traveler. Ready to play? Guess the sum of the dice correctly and your coins shall be doubled.")
    print(r"""
       _______
      /\ o o o\
     /o \ o o o\_______
    <    >------>   o /|
     \ o/  o   /_____/o|
      \/______/     |oo|
            |   o   |o/
            |_______|/

    """)
    print("RULES: You roll 3 dice. I will tell you the result of one of the dice you rolled. Then, you will guess the total sum of all 3 dice. You have 3 guesses. ")
    dicelist = dicegame()

    print(f"One of the rolled dice was {dicelist[0]} ")

    diceSum = sum(dicelist)

    guessTracker = 0
    while True:
        guess = int(input("Guess the sum of the dice: "))
        if guess == diceSum:
            print("You guessed correctly!")
            moneyWon = moneyToGamble * 2
            break
        elif guessTracker == 2:
            print("You lost!")
            break
        elif guess < diceSum:
            print("Your guess is too low.")
            guessTracker += 1
        elif guess > diceSum:
            print("Your guess is too high.")
            guessTracker += 1

    return moneyWon
