import Scripts.Database.database as db
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette
import Scripts.Core.account as account
import os
import sys

games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def GameLoop():
    amountToGamble = int(input("How much would you like to gamble? "))
    db.UpdateMoney(account.name, -amountToGamble)
    selectedGame = 'blackjack'
    game = games[selectedGame]
    moneyWon = game(amountToGamble)

    db.UpdateMoney(account.name, moneyWon)
    
    NoMoreMoney(account.name)

    #os.system('cls' if os.name == 'nt' else 'clear')
    return

def NoMoreMoney(name):
    if db.CheckMoney(name) == False:
        print ("You lost, game over.")
        sys.exit(0)

