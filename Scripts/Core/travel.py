import Scripts.Database.database as db
import os

def travel():
    os.system('cls' if os.name == 'nt' else 'clear')
    #print("Select location to travel to!\n1. Bangkok\n2. Berlin")
    db.takeAllAirports()
    selection = int(input("select airport 1-5 or exit 6: "))
    if selection == 6:
        return
    return
