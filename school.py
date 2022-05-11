import sqlite3 as sql
import csv # if we need it

# define the connection and the cursor

connection = sql.connect(test.db) #error because i didnt installed sqlite3

cursor = connection.cursor()

# creating the storing table

dbCreate = "CREATE TABLE IF NOT EXISTS tblname(row1 DECIMAL, row2 DECIMAL, row3 DEXIMAL, row4 Datetime PRIMARY KEY"

cursor.execute(dbCreate)

# Doing the first interaction
AskDate = input("Bitte geben Sie Ihr gewünschtes Datum ein: ")

cursor.execute("SELECT * FROM tblname")

date = "SELECT * FROM tblname WHERE row4 like " + Askdate + '"'

# First Output

print("Sie haben " + date + "ausgesucht")

# second interaction
string = input("Bitte geben sie einen der Werte 'Max', 'Min' oder 'Avg' aus ")

print("Sie haben " + string + " ausgewählt")

# creating the second Output

eval_row1 = "SELECT MAX(row1) as 'Max', MIN(row1) as 'Min', AVG(row1) as 'Avg' WHERE row4 LIKE" + string + '"'


#define the choices
if eval_row1 == "Max":
    result=cursor.fetchone()[0]
    print(result)
elif eval_row1 == "Max":
    result=cursor.fetchone()[1]
    print(result)
elif eval_row1 == "Avg":
    result=cursor.fetchone()[2]
    print(result)
else:
    print("Bitte richtigen Wert eingeben!")

#closing the connection
connection.commit()
connection.close()




