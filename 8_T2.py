import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='Laggorithm',
         password='CupOfLiberTea',
         autocommit=True)
def CodeToName(Code):
    HeliRowCount = 0
    AirportRowCount = 0
    cursor = connection.cursor()
    sql = f"select * from airport where iso_country = '{Code}' and type = 'heliport';"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        HeliRowCount += 1
        for row in result:
            AirportRowCount += 1
    sql2 = f"select * from airport where iso_country = '{Code}' and type = 'small_airport';"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for row in result2:
        AirportRowCount += 1
    cursor.close()
    connection.close()
    print(f"helicopters: {HeliRowCount}, airports: {AirportRowCount}")
    return
Code = input("Anna country-koodia (FI tai jotain muuta): ")
CodeToName(Code)