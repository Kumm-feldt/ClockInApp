import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="antonio00"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE master_admin")

# Commit the changes
mydb.commit()

# Close the connection
mydb.close()
