from Scripts.Games import cardDeck as deck

print("Welcome to Poker!")

def poker():
    cards = deck.getCards()
    cards = deck.Shuffle(cards)

    playerCards = []
    dealerCards = []

    while True:
        for i in range(5):
            playerCard = cards.pop(0)
            playerCards.append(playerCard)
            dealerCard = cards.pop(0)
            dealerCards.append(dealerCard)
        print(playerCards)
        print(dealerCards)

        while True:
            z = int(input("Which card would you like to switch? (select one per question, 6 when you're done.) "))
            z = z-1
            if z == 5:
                break
            playerCards.remove(z)





poker()