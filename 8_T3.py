import mysql.connector
from geopy import distance
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='Laggorithm',
         password='CupOfLiberTea',
         autocommit=True)
def CodeToName(Code):
    cursor = connection.cursor()
    result= f"select  latitude_deg, longitude_deg from airport where ident = '{Code}';"
    cursor.execute(result)
    result = cursor.fetchall()
    return result
Code1 = input("Anna ICAO-koodia: ")
pos1 = CodeToName(Code1)
print(pos1)
Code2 = input("Anna ICAO-koodia: ")
pos2 = CodeToName(Code2)
print(pos2)
connection.close()
distance = distance.distance(pos1, pos2).km
print(f"{round(distance, 2)} kilometria")
