import Scripts.Database.database as db
import Scripts.Core.account as account
import os

def travel():
    os.system('cls' if os.name == 'nt' else 'clear') 
    airports = db.takeAllAirports(db.getPlayerContinent(account.name))
    print(f"You have {db.GetPlayerMoney(account.name)} coins")
    i = 0
    for value in airports:
        i = i + 1
        print(f"{i}, name: {value[0]} and continent: {value[3]}")
    selection = int(input("select airport 1-5 or exit 6: "))
    if selection < 6 and selection > 0:
        db.fly(airports[selection - 1][4], account.name)
    if selection == 6:
        return
    return
