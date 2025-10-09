import random

def Game(moneyToGamble):
    print("Welcome to the Russian Roulette!")
    print(r"""
      (                                 _
       )                               /=>
      (  +____________________/\/\___ / /|
       .''._____________'._____      / /|/\
      : () :              :\ ----\|    \ )
       '..'______________.'0|----|      \
                        0_0/____/        \
                            |----    /----\
                           || -\\ --|      \
                           ||   || ||\      \
                            \\____// '|      \
                                    .'/       |
                                   .:/        |
                                   :/_________|


    """)
    print("RULES:Keep pulling the trigger until you either get shot or decide to stop. \n"
          "Each successful trigger pull without getting shot earns you money. \n"
          "The longer you play, the higher the reward, but the risk increases with each shot. ")
    bullet = random.randint(1, 6)
    player = 1
    moneyWon = 0
    while True:
        decision = input("Do you wish to shoot yourself? (yes/no): ")
        if decision == "yes":
            if bullet == player:
                print("You got shot. Game over.")
                break
            else:
                print("Safe.")
                player += 1
                moneyWon = moneyWon + moneyToGamble // 3
                print(f"Your winnings thus far: {moneyWon}")
        elif decision == "no":
            print("You decided to stop. Game over.")
            break
        else:
            print("Invalid input.")
    return moneyWon