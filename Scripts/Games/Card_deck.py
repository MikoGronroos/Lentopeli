import random

def getCards():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def Shuffle(deck):
    random.shuffle(deck)
    return deck

