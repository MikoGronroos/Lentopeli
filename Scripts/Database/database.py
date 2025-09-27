import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

kursori = yhteys.cursor()

def TestiFunktio():
    sql = f'select * from game';
    kursori.execute(sql);
    return kursori.fetchall()
