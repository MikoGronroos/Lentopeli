#import Scripts.Database.Database as db
import Scripts.Games.blackJack as blackjack

games = {"blackjack": blackjack.Game,}

def GameLoop():
    games["blackjack"]()
    return
