import random
def Game():
    print("Welcome to the Russian Roulette!")
    bullet = random.randint(1, 6)
    player = 1
    while True:
        decision = input("Do you want to shoot yourself? (yes/no): ")
        if decision == "yes":
            if bullet == player:
                print("You got shot.")
                break
            else:
                print("Safe.")
                player += 1
        elif decision == "no":
            print("You decited to stop.")
            break
        else:
            print("Invalid input.")

    print("The game is over.")
    return
