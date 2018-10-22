"""
MySQL works on a server, it doesn't create a .db file on the working directory like SQLite3 does.

Before running the python script, MySQL server must be running.
"""

import mysql.connector

DB_NAME = 'UsersDb'

TABLES = {}

# DDL to create table
TABLES['users'] = (
    "CREATE TABLE `UsersDb`.`tblUser` ("
    " `UserId` INT NOT NULL AUTO_INCREMENT,"
    " `UserName` VARCHAR(45) NULL,"
    " `Password` VARCHAR(45) NULL,"
    " PRIMARY KEY (`UserId`));"
)


def create_db(cursor):
    # Creating database
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))


# Establishing connection

cnx = mysql.connector.connect(user='bldr', password='free',
                              host='127.0.0.1')
                              # if db is known and existing
                              # database='{}'.format(DB_NAME))

# Creating a cursor
cursor = cnx.cursor()

# Connecting to DB if already exists or creating if not
try:
    cnx.database = DB_NAME
except Exception as err:
    create_db(cursor)
    cnx.database = DB_NAME

# Creating tables - ddl for Data Definition Language
for name, ddl in TABLES.items():
    try:
        print("Creating table {}".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        print("Already exists.")
        print(err)


# Closing connections
cursor.close()
cnx.close()
