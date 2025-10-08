import random

def roulette(moneyToGamble):

    print("Welcome to Roulette!")
    print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |")
    print("RULES: Choose a number between 1-12.\n"
          "If you bet on an even number, you will win even if the winning number is another even number. \n"
          "Same rule goes for odd numbers.")

    odd = [1, 3, 5, 7, 9, 11]
    even = [2, 4, 6, 8, 10, 12]

    while True:
        result = random.randint(1, 12)
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
                print("You lost the bet. :(")

        jatkaa = input("Do you wish to continue? (yes/no): ")

        if jatkaa == "n":
            break
    return moneyWon
