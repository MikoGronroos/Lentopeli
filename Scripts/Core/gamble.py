import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette
import os


games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def gamble():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You have {db.GetPlayerMoney(account.name)} coins")
        amountToGamble = int(input("How much would you like to gamble? "))
        db.UpdateMoney(account.name, -amountToGamble)
        selectedGame = 'blackjack'
        game = games[selectedGame]
        moneyWon = game(amountToGamble)

        db.UpdateMoney(account.name, moneyWon)
        
        selection = int(input("1 to gamble and 2 to exit"))
        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
        if selection == 2:
            return
