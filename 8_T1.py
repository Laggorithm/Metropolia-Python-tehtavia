import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='Laggorithm',
         password='CupOfLiberTea',
         autocommit=True)
def CodeToName(Code):
    cursor = connection.cursor()
    sql = f"select name from airport where ident = '{Code}';"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(sql)
    for row in result:
        print(row[0])
        cursor.close()
        connection.close()
    return
#00CA
Code = input("Anna ICAO-koodia: ")
CodeToName(Code)