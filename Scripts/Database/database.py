import mysql.connector
import random

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='TiVi03DB',
        autocommit=True
        )

kursori = yhteys.cursor()

def TestiFunktio():
    sql = f'select * from game'
    kursori.execute(sql)
    return kursori.fetchall()

def DoesPlayerExist(name):
    sql = f'select * from game where screen_name = \'{name}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def AddNewPlayer(name, password):
    sql = f"INSERT INTO game (id, location, password, screen_name) VALUES (%s, %s, %s, %s)"
    val = (random.randint(0,100000000), "00FA", password, name)
    kursori.execute(sql, val)

def CheckPassword(name, password):
    sql = f'select * from game where screen_name = \'{name}\' and password = \'{password}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def UpdateMoney(name, money):
    sql = f"UPDATE game set money = (money + {money}) where screen_name = \'{name}\'"
    kursori.execute(sql)
    sql2 = f"SELECT * FROM game where screen_name = \'{name}\' and money > 0"
    kursori.execute(sql2)
    return len(kursori.fetchall()) > 0