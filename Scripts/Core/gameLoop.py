#import Scripts.Database.Database as db
import Scripts.Games.blackJack as blackjack
import Scripts.Games.russianRoulette as russianroulette

games = {'blackjack': blackjack.Game,
         'russianroulette': russianroulette.Game}

def GameLoop():
    game = games["blackjack"]
    game()
    return
