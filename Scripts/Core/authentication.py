import Scripts.Database.database as db
import Scripts.Core.account as account

def Login():
    while True:
        account.name = input("Enter character name: ")
        password = input("Enter password:")
        if db.CheckPassword(account.name, password) == True:
            print("Congratulations! You have successfully logged in! :)")
            return True
        else:
            print("password or username incorrect :(")


def Signup():
    account.name = input("Enter character name: ")
    while db.DoesPlayerExist(account.name) == True:
        account.name = input("Character name already used. Pick a new name: ")
    password = input("Enter password: ")
    db.AddNewPlayer(account.name, password)
    return True


def Authenticate():
    question = input("Log in or register a new character (login/register): ")
    if question == "login":
        return Login()
    elif question == "register":
        return Signup()
