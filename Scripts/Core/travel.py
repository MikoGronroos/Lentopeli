import os

def travel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Select location to travel to!\n1. Bangkok\n2. Berlin")
    selection = int(input("select airport 1-5 or exit 6: "))
    if selection == 6:
        return
    return
