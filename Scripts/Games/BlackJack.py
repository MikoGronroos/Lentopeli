from Scripts.Games import Card_deck as deck

def Game():
    print("Howdy. Down for a round of blackjack?")
    print("Dealer must stand at 17, ace can be either 11 or 1.")

    cards = deck.getBlackjackCards()
    cards = deck.Shuffle(cards)

    playerCards = []
    playerCards.append(cards.pop(0))
    playerCards.append(cards.pop(0))

    dealerCards = []
    dealerCards.append(cards.pop(0))
    dealerCards.append(cards.pop(0))

    playerState = 0
    gameOver = False

    print(f"Your cards: {playerCards}, dealer's cards: {dealerCards[0]}")
    while True:
        if gameOver:
            break
        decision = input("Do you wish to hit or stand? hit/stand:")
        if decision == "hit":
            playerCards.append(cards.pop(0))
            print(f"Your cards: {playerCards}")
            if calculateValue(playerCards) > 21:
                playerState = -1
                break
        elif decision == "stand":
            while True:
                dealerSum = calculateValue(dealerCards)
                print(f"Dealer's cards: {dealerCards}")
                if dealerSum <= 16:
                    dealerCards.append(cards.pop(0))
                elif dealerSum >= 17 and dealerSum <= 21:
                    gameOver = True
                    if calculateValue(dealerCards) > calculateValue(playerCards):
                        playerState = -1
                    elif calculateValue(dealerCards) == calculateValue(playerCards):
                        playerState = 2
                    elif calculateValue(dealerCards) < calculateValue(playerCards):
                        playerState = 1
                    break
                elif dealerSum > 21:
                    playerState = 1
                    gameOver = True
                    break

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
Game()
