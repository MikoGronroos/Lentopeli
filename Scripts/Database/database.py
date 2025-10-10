import mysql.connector
import random

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

kursori = yhteys.cursor()

def DoesPlayerExist(name):
    sql = f'select * from game where screen_name = \'{name}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def AddNewPlayer(name, password):
    sql = f"INSERT INTO game (id, location, password, screen_name, money, newPlayer) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (random.randint(0,100000000), None, password, name, 100, True)
    kursori.execute(sql, val)

def CheckPassword(name, password):
    sql = f'select * from game where screen_name = \'{name}\' and password = \'{password}\''
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def UpdateMoney(name, money):
    sql = f"UPDATE game set money = (money + {money}) where screen_name = \'{name}\'"
    kursori.execute(sql)

def CheckMoney(name):
    sql = f"SELECT * FROM game where screen_name = \'{name}\' and money > 0"
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def ResetPlayer(name):
    sql = f"UPDATE game set money = 100 where screen_name = \'{name}\'"   
    kursori.execute(sql)

def getPlayerContinent(name):
    sql = f'select airport.continent from airport, game where game.screen_name = \'{name}\' and airport.ident = game.location' 
    kursori.execute(sql)
    return kursori.fetchall()[0][0]
    

def listMaker(continent):
    continentList = ["EU", "AS", "NA", "SA", "AF", "OC"]
    for a in range(6):
        if continentList[a] == continent:
            continentList.remove(continent)
    return continentList

def getRandomAirportCode(continent):
    sql = f"SELECT ident FROM airport where continent = '{continent}' and type = 'large_airport'" 
    kursori.execute(sql)
    newList = kursori.fetchall()
    return newList[random.randint(0, len(newList))][0]

def isNewPlayer(name):
    sql = f'select * from game where screen_name = \'{name}\' and newPlayer = true'
    kursori.execute(sql)
    return len(kursori.fetchall()) > 0

def newPlayerCreated(location, name):
    sql = f"UPDATE game set location = \'{location}\', newPlayer = 0 where screen_name = \'{name}'"
    kursori.execute(sql)

def airportTaker(continent):
    countryList = []
    sql = f"SELECT name, latitude_deg, longitude_deg, continent FROM airport where continent = '{continent}' and type = 'large_airport'" 
    kursori.execute(sql)
    result = kursori.fetchall()
    randomInt = random.randint(1, kursori.rowcount)
    countryList.append(result)
    return result[randomInt]

def takeAllAirports(continent):
    continentList = listMaker(continent)
    airportList = []
    for i in range(5):
        airportList.append(airportTaker(continentList[i]))
    return airportList

def getGameId(name):
    kursori.execute(f"select id from game where screen_name = \'{name}'")
    return kursori.fetchall()[0][0]

def getPostcardId(continent):
    kursori.execute(f"SELECT id FROM postcards WHERE continent =  \'{continent}'")
    postcard = kursori.fetchone()
    if not postcard:
        return
    postcard_id = postcard[0]
    return postcard_id


def collect_postcard(player_id, postcard_id):
    print(f"{player_id},{postcard_id}")
    val = (player_id, postcard_id)
    sql = "INSERT IGNORE INTO player_postcards (player_id, postcard_id) VALUES (%s, %s)"

    kursori.execute(sql, val)

def show_collected_postcards(player_id):
    kursori.execute(f"select postcards.name, postcards.continent from player_postcards, postcards where player_id =  \'{player_id}' and postcards.id = player_postcards.postcard_id")
    return kursori.fetchall()
