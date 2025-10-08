import random
def Game(moneyToGamble):
    print("Welcome to the Russian Roulette!")
    bullet = random.randint(1, 6)
    player = 1
    moneyWon = 0
    while True:
        decision = input("Do you want to shoot yourself? (yes/no): ")
        if decision == "yes":
            if bullet == player:
                print("You got shot.")
                break
            else:
                print("Safe.")
                player += 1
                moneyWon = moneyWon + moneyToGamble // 3
                print(f"Your winnings thus far: {moneyWon}")
        elif decision == "no":
            print("You decided to stop.")
            break
        else:
            print("Invalid input.")

    print("The game is over.")
    return moneyWon
