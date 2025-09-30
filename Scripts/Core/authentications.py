from ipaddress import summarize_address_range

import mysql.connector
import Scripts.Database.database as db

def Login():
    while True:
        characterName = input("Enter character name: ")
        password = input("Enter password:")
        if db.CheckPassword(characterName, password) == True:
            print("Congratulations! You have successfully logged in! :)")
            return True
        else:
            print("password or username incorrect :(")


def Signup():
    characterName = input("Enter character name: ")
    while db.DoesPlayerExist(characterName) == True:
        characterName = input("Character name already used. Pick a new name: ")
    password = input("Enter password: ")
    db.AddNewPlayer(characterName, password)
    return True


def Authenticate():
    question = input("Log in or register a new character (login/register): ")
    if question == "login":
        return Login()
    elif question == "register":
        return Signup()