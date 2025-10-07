#import Scripts.Database.Database as db
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette
import os

games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def GameLoop():
    print("You are here!")
    os.system('cls' if os.name == 'nt' else 'clear')
    return
