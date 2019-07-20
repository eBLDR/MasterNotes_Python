"""
SQLite3 is a database engine. It is self-contained, serverless,
zero-configuration and transactional. It is very fast and lightweight,
and the entire database is stored in a single disk file.

CRUD - Create, Read, Update, Delete operations
"""
import sqlite3

# in Python, there is no need to add ; at the end of the SQL statements

# Create a database in RAM
# db = sqlite3.connect(':memory:')

# Opening a database, creating it if not existing
db = sqlite3.connect('contacts.sqlite')

# A cursor enables manipulation of sets (it behaves as a generator in Python),
# it's preferable to be used instead of db.***, being a generator means that
# the data can only be retrieved once.
cursor = db.cursor()

# cursor.execute('raw SQLite3 statement') to perform actions
# CREATE table
cursor.execute('DROP TABLE contacts')
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL, phone INTEGER, email TEXT)""")
# FOREIGN KEY(column_name_in_new_table) REFERENCES table(column_name)
# IF NOT EXISTS will create the table only if it doesn't exists
# PRIMARY KEY provides and autoincrementing integer number, it's unique
# NOT NULL will not accept null values in that column
# FOREIGN KEY / REFERENCES will link the new column in the new table to the
# values on another table's column

# cursor.execute("DELETE FROM contacts")  # to clear the table every time,
# otherwise the INSERT will duplicate on each run

# CREATE - insert records
cursor.execute("INSERT INTO contacts (name, phone, email) VALUES "
               "('BLDR', 666666666, 'ed@bldr.cat')")

cursor.execute("INSERT INTO contacts (name, phone, email) VALUES "
               "('OJKA', 888883459, 'ojka@bldr.cat')")

# Record with null fields
cursor.execute("INSERT INTO contacts (name) VALUES ('Not me')")

# Using ? placeholder to insert, pass parameters in a tuple
name, num, email = 'Python', '010101', '01@01.com'
cursor.execute(
    'INSERT INTO contacts (name, phone, email) VALUES (?,?,?)',
    (name, num, email)
)

# A dictionary can also be used
cursor.execute(
    "INSERT INTO contacts (name, phone, email) VALUES (:name, :phone, :email)",
    {'name': 'Anaconda', 'phone': '111111111', 'email': 'ana@con.da'}
)

# If we need to insert many records at once, use
users = [('name1', 'phone1', 'email1'),
         ('name2', 'phone2', 'email2'),
         ('name3', 'phone3', 'email3')]
cursor.executemany(
    'INSERT INTO contacts (name, phone, email) VALUES(?,?,?)',
    users
)

# READ - query records
cursor.execute('SELECT name, phone, email FROM contacts')

for row in cursor:  # cursor is iterable
    print(row)

print(type(row))  # tuple
print('{} fields/columns found'.format(len(row)))

# cursor is now fully retrieved, so
for row in cursor:
    print(row)  # won't do anything

print('=' * 30)

cursor.execute('SELECT * FROM contacts')  # querying again, * = all
# fetchall function returns a list with all the info in cursor
data_list = cursor.fetchall()
print(data_list)  # A list

cursor.execute('SELECT * FROM contacts')
record = cursor.fetchone()  # returns ONLY the next item in cursor
print(record)  # A tuple

print('=' * 30)

field = input('Enter a field where to search:\nname / phone / email\n').lower()
name = input('Please enter a {} to search for: '.format(field))

# Using WHERE conditions
record = cursor.execute("SELECT * FROM contacts WHERE {} LIKE ?".format(
    field), (name,)
)

# using LIKE to be non-case sensitive
print(record.fetchone())

print('=' * 30)

# UPDATE
new_phone = '3113093164'
user_id = 1
cursor.execute(
    'UPDATE contacts SET phone = ? WHERE id = ?',
    (new_phone, user_id)
)

cursor.execute('SELECT * FROM contacts WHERE id = ?', (user_id,))
print(cursor.fetchall())

# DELETE
delete_userid = 2
cursor.execute('DELETE FROM contacts WHERE id = ?', (delete_userid,))
print('Contact with id = {} deleted!'.format(delete_userid))

# CLosing cursor connection
cursor.close()

# TRANSACTIONS
# If we don't commit, everything is ROLLED BACK, this means that
# none of the changes are saved
db.commit()  # Commit all the changes

# db.rollback()  # Undo all the changes

db.close()  # closing the table
