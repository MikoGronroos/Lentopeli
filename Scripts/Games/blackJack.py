from Scripts.Games import cardDeck as deck

def stand(dealerCards, playerCards, cards):
    state = 0;
    while True:
        dealerSum = calculateValue(dealerCards)
        print(f"Dealer's cards: {dealerCards}")
        if dealerSum <= 16:
            dealerCards.append(cards.pop(0))
        elif dealerSum >= 17 and dealerSum <= 21:
            if calculateValue(dealerCards) > calculateValue(playerCards):
                state = -1
            elif calculateValue(dealerCards) == calculateValue(playerCards):
                state = 2
            elif calculateValue(dealerCards) < calculateValue(playerCards):
                state = 1
            break
        elif dealerSum > 21:
            state = 1
            break
    return state

def hit(playerCards, cards):
    state = 0;
    playerCards.append(cards.pop(0))
    print(f"Your cards: {playerCards}")
    if calculateValue(playerCards) > 21:
        state = -1
    return state

def setupCards(playerCards, cards):
    playerCards.append(cards.pop(0))
    playerCards.append(cards.pop(0))



def Game():
    print("Howdy. Down for a round of blackjack?")
    print("Dealer must stand at 17, ace can be either 11 or 1.")

    cards = deck.getBlackjackCards()
    cards = deck.Shuffle(cards)

    playerCards = []
    setupCards(playerCards, cards)

    dealerCards = []
    setupCards(dealerCards, cards)

    playerState = 0

    print(f"Your cards: {playerCards}, dealer's cards: {dealerCards[0]}")
    while True:
        if playerState != 0:
            break
        decision = input("Do you wish to hit or stand? hit/stand:")
        if decision == "hit":
            playerState = hit(playerCards, cards)
        elif decision == "stand":
            playerState = stand(dealerCards, playerCards, cards)

    if playerState == -1:
        print("You lost, I honestly expected better")
    elif playerState == 1:
        print("You won")
    elif playerState == 2:
        print("Tie")
    return

def calculateValue(cards):
    newSum = sum(i for i, j in cards)
    if newSum > 21:
        newSum = 0
        for i, j in cards:
            if i == 11:
                newSum += 1
            else:
                newSum += i
    return newSum
