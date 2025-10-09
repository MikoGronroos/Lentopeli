import Scripts.Database.database as db
import Scripts.Core.account as account
import random

def startNewGame():
    continentList = ["EU", "AS", "NA", "SA", "AF", "OC"]
    startingContinent = continentList[random.randint(0, len(continentList) - 1)]
    print(startingContinent)

