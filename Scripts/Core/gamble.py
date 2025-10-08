import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette


games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def gamble():
    amountToGamble = int(input("How much would you like to gamble? "))
    db.UpdateMoney(account.name, -amountToGamble)
    selectedGame = 'blackjack'
    game = games[selectedGame]
    moneyWon = game(amountToGamble)

    db.UpdateMoney(account.name, moneyWon)

    return
