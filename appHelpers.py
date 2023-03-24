import mysql.connector

def create_db_if_not_exists():

    database = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",  
    )

    cursor = database.cursor(buffered=True)
    query = ("CREATE DATABASE IF NOT EXISTS db")

    cursor.execute(query)

    database.commit()
    cursor.close()
    database.close()

def create_table_if_not_exists():

    database = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",  
        database="db"
    )

    cursor = database.cursor(buffered=True)
    query = ("CREATE TABLE IF NOT EXISTS counter (number int)")

    cursor.execute(query)

    database.commit()
    cursor.close()
    database.close()

def create_data_if_not_exists():

    database = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",  
        database="db"
    )

    cursor = database.cursor(buffered=True)
    query = ("SELECT COUNT(*) FROM counter")
    cursor.execute(query)

    number = cursor.fetchone()[0]

    test = False

    if(number == 0):
        test = True
        create_query = ("INSERT INTO counter VALUES (0)")
        cursor.execute(create_query)
        database.commit()

    cursor.close()
    database.close()

    return number, test
