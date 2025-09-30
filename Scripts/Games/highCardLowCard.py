from Scripts.Games import cardDeck as deck

def Game():
    cards = deck.getCards()
    cards = deck.Shuffle(cards)
    playerCard = cards.pop(0)
    dealerCard = cards.pop(0)
    moneyGambled = input("Determine how much you want to lose: ")
    print("Welcome to High card, Low card!")
    print (f"Your card:{playerCard}")
    playerGuessedCorrectly = False
    answer = input("Higher, Lower or Same?")
    if answer == "Higher" and playerCard > dealerCard:
        playerGuessedCorrectly = True
    elif answer == "Lower" and playerCard < dealerCard:
        playerGuessedCorrectly = True
    elif answer == "Same" and playerCard == dealerCard:
        playerGuessedCorrectly = True

    if playerGuessedCorrectly:
        print("You guessed correctly.")
    else:
        print("You guessed incorrectly.")
    return
Game()