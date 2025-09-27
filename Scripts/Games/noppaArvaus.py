#Heitetään kolme noppaa. Pelaaja saa tietää yhden heitetyn nopan tuloksen.
#Pelaajalla on kolme arvausta arvata heitettyjen noppien summa. Peli
#kertoo onko arvaus liian korkea/alhainen. Pelaaja maksaa x määrän kolikoita
#pelatakseen ja voittaessa kolikoiden määrä tuplaantuu.

import random

print("Welcome traveler. Interested in a game of dice? For 1-3 coin, guess the sum of the dice correctly and your coins shall be doubled.")

def dicegame():
    dicelist = []
    for i in range(3):
        dice = random.randint(1,6)
        dicelist.append(dice)
    return dicelist

dicelist = dicegame()

print(f"One of the rolled dice was {dicelist[0]} ")

diceSum = sum(dicelist)


def game():
    guessTracker = 0
    while True:
        guess = int(input("Guess the sum of the dice: "))
        if guess == diceSum:
            print("you guessed correcty")
            break
        elif guessTracker == 2:
            print("you lost LOL")
            break
        elif guess < diceSum:
            print("youre guess is too low")
            guessTracker += 1
        elif guess > diceSum:
            print("youre guess is too high")
            guessTracker += 1



while True:
    game()
    decision = input("Do you wish to continue? yes/no:")
    if decision == "no":
        break



print("The game has ended")
