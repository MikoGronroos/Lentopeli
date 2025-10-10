import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Core.gamble as gamble
import Scripts.Core.travel as travel
import Scripts.Core.inventory as inventory
import Scripts.Core.shop as shop
import os
import sys

def GameLoop():

    os.system('cls' if os.name == 'nt' else 'clear')
    if NoMoreMoney(account.name) == False:
        print ("You lost, game over.")
        sys.exit(0)
    print(f"You have {db.GetPlayerMoney(account.name)} coins")
    print("Collect 6 postcards from different continents to win")
    selection = int(input("1 to gamble, 2 to travel, 3 to inventory, 4 to shop and 5 to exit"))
    if selection == 1:
        gamble.gamble()
    if selection == 2:
        travel.travel()
    if selection == 3:
        inventory.showInventory()
    if selection == 4:
        shop.shop()
    if selection == 5:
        sys.exit(0)
    return

def NoMoreMoney(name):
    return db.CheckMoney(name, 0)
