import Scripts.Database.database as db
import Scripts.Core.account as account
import os

def showInventory():
    os.system('cls' if os.name == 'nt' else 'clear')
    values = db.show_collected_postcards(account.getGameId())
    for value in values:
        print(f"{value}")
    selection = int(input("1 to exit: "))
    if selection == 1:
        return
