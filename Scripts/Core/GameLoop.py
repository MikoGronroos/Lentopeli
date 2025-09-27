#import Scripts.Database.Database as db
import Scripts.Games.BlackJack as blackjack

games = {"blackjack": blackjack.Game,}

def GameLoop():
    games["blackjack"]()
    return
