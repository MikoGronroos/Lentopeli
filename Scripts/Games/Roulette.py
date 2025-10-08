import random

def roulette(moneyToGamble):

    print("Welcome to Roulette! Choose a number between 1-12.")
    print("If you bet on an even number, you will win even if the winning number is another even number")
    print("What are you betting on?")

    odd = [1, 3, 5, 7, 9, 11]
    even = [2, 4, 6, 8, 10, 12]

    while True:
        result = random.randint(1, 12)
        print(result)
        answer = int(input("What are you betting on? (1-12): "))

        if answer == result:
            print("You guessed the number correctly!")
            moneyWon = moneyToGamble * 4
        else:
            if answer in odd and result in odd:
                print("You guessed odd correctly!")
                moneyWon = moneyToGamble + moneyToGamble // 3
            elif answer in even and result in even:
                print("You guessed even correctly!")
                moneyWon = moneyToGamble + moneyToGamble // 3
            else:
                print("Hävisit betin")

        jatkaa = input("Haluatko jatkaa? (y/n) ")

        if jatkaa == "n":
            break
    return moneyWon
