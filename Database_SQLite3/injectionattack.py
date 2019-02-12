"""
To avoid Sql Injection Attack, never use parameters that have come from
a user's input or external code in our statement's str.
SANITIZING - make (something) more palatable by removing elements that are likely to be unacceptable or controversial.
"""

import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = 'update@update.mail'
phone = '1234'  # integers can actually be specified as strings, SQL will detect both cases

# not sanitized
# update_sql = "UPDATE contacts SET email = {} WHERE contacts.phone = {}".format(new_email, phone)

# sanitized, using ? as a PLACEHOLDER
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"

cursor = db.cursor()
# cursor can manipulate data, 1 statement at the time
cursor.execute(update_sql, (new_email, phone))  # using PARAMETER SUBSTITUTION for the placeholder (sanitized method)

sql_injection_attack = "UPDATE contacts SET name = 'HACKER';DROP TABLE contacts"  # statements separated by ;
# cursor.executescript(sqlInjectionAttack)  # this functions can execute MORE than 1 statement at the time

print('{} row/s updated'.format(cursor.rowcount))  # rowcount returns the # of rows that have been modified by cursor

cursor.connection.commit()  # is the equivalent to db.commit, but it gives more readability
# is we used the cursor to manipulate the data, the the commit must come from cursor also
print('Are connections the same: {}'.format(cursor.connection == db))
cursor.close()

# a shortcut to using cursor
for row in db.execute("SELECT * FROM sqlite_master"):  # sqlite_master gives info about the master table
    print(row)  # use the name of the table for the sqlInjectionAttack

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
