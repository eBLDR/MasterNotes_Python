"""
Stored procedures are programs that can accept
parameters, it does not return a value like a function.
"""
import mysql.connector

DB_NAME = 'UsersDb'

# Using database created at creatingdb.py
cnx = mysql.connector.connect(user='bldr', password='free', host='127.0.0.1', database='{}'.format(DB_NAME))

# Creating a cursor
cursor = cnx.cursor()

# Creating procedure - spCreateUser as example
dll = (
    """
    USE `{0}`;
    DROP procedure IF EXISTS `spCreateUser`;
    DELIMITER $$
    USE `{0}`$$
    CREATE PROCEDURE `spCreateUser` (
    IN p_UserName varchar(50),
    IN p_Password varchar(50)
    )
    BEGIN
    if ( select exists (select 1 from tblUser where UserName = p_UserName) ) THEN select 'Username Exists !!';
    ELSE
    insert into tblUser (
    UserName,
    Password
    )
    values (
    p_UserName,
    p_Password
    );
    END IF;
    END$$
    DELIMITER ;
    """.format(DB_NAME)
)

cursor.execute(dll)

# Closing connections
cursor.close()
cnx.close()
