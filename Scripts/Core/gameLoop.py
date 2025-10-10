import Scripts.Database.database as db
import Scripts.Core.account as account
import Scripts.Core.gamble as gamble
import Scripts.Core.travel as travel
import os
import sys

def GameLoop():

    os.system('cls' if os.name == 'nt' else 'clear')
    if NoMoreMoney(account.name) == False:
        print ("You lost, game over.")
        sys.exit(0)
    selection = int(input("1 to gamble, 2 to travel, 3 to inventory, 4 to shop and 5 to exit"))
    if selection == 1:
        gamble.gamble()
    if selection == 2:
        travel.travel()
    if selection == 3:
        sys.exit(0)
    return

def NoMoreMoney(name):
    return db.CheckMoney(name)
