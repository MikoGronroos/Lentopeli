#import Scripts.Database.Database as db
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette
import os

games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def GameLoop():

    amountToGamble = int(input("How much would you like to gamble? "))

    selectedGame = 'blackjack'
    game = games[selectedGame]
    game(amountToGamble)

    os.system('cls' if os.name == 'nt' else 'clear')
    return
