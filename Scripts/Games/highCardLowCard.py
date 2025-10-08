from Scripts.Games import cardDeck as deck

def Game(moneyToGamble):
    moneyWon = 0
    cards = deck.getCards()
    cards = deck.Shuffle(cards)
    playerCard = cards.pop(0)
    dealerCard = cards.pop(0)
    print("Welcome to High card, Low card!")
    print("""
              _____
             |A .  | _____
             | /.\ ||A ^  | _____
             |(_._)|| / \ ||A _  | _____
             |  |  || \ / || ( ) ||A_ _ |
             |____V||  .  ||(_'_)||( v )|
                    |____V||  |  || \ / |
                           |____V||  .  |
                                  |____V|
    """)
    print("RULES: Guess whether your card is higher, lower, or the same as the dealer’s card.")
    print (f"Your card:{playerCard}")
    playerGuessedCorrectly = False
    answer = input("Higher, Lower or Same?: ")
    if answer == "Higher" and playerCard > dealerCard:
        playerGuessedCorrectly = True
    elif answer == "Lower" and playerCard < dealerCard:
        playerGuessedCorrectly = True
    elif answer == "Same" and playerCard == dealerCard:
        playerGuessedCorrectly = True
        moneyWon = moneyToGamble * 2

    if playerGuessedCorrectly:
        print("You guessed correctly.")
    else:
        print("You guessed incorrectly.")
    return moneyWon
Game(1)