"""
To avoid Sql Injection Attack, never use parameters that have come from
a user's input or external code in our statement's str.
SANITIZING - make (something) more palatable by removing elements that are
likely to be unacceptable or controversial.
"""
import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = 'update@update.mail'
# Integers can actually be specified as strings, SQL will detect both cases
phone = '1234'

# Not sanitized
# update_sql = 'UPDATE contacts SET email = {} WHERE ' \
#              'contacts.phone = {}'.format(new_email, phone)

# Sanitized, using ? as a PLACEHOLDER
update_sql = 'UPDATE contacts SET email = ? WHERE contacts.phone = ?'

cursor = db.cursor()
# cursor can manipulate data, 1 statement at the time
# Using PARAMETER SUBSTITUTION for the placeholder (sanitized method)
cursor.execute(update_sql, (new_email, phone))

# statements separated by ";"
sql_injection_attack = "UPDATE contacts SET name = 'HACKER';DROP TABLE contacts"

# This method can execute MORE than 1 statement at the time
# cursor.executescript(sqlInjectionAttack)

# rowcount returns the # of rows that have been modified by cursor
print('{} row/s updated'.format(cursor.rowcount))

# Equivalent to db.commit, but it gives more readability
cursor.connection.commit()
# It is we used the cursor to manipulate the data, the the commit must come
# from cursor also
print('Are connections the same: {}'.format(cursor.connection == db))
cursor.close()

# A shortcut to using cursor
# sqlite_master gives info about the master table
for row in db.execute('SELECT * FROM sqlite_master'):
    print(row)  # use the name of the table for the sqlInjectionAttack

for row in db.execute('SELECT * FROM contacts'):
    print(row)

db.close()
