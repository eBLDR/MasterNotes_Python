import sqlite3

# Handling exceptions
# Try/catch method
try:
    db = sqlite3.connect('contacts.sqlite')
    cursor = db.cursor()

    # Do some statement
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
                      name TEXT, phone TEXT, email TEXT unique, password TEXT)''')

    # Commit the changes if no errors raised
    db.commit()
    print('Successful - COMMIT')

except Exception as e:
    # Roll back transaction if any error occurred
    db.rollback()
    print('Unsuccessful - ROLLBACK')
    raise e

finally:
    # Always close the session
    cursor.close()
    db.close()
    print('Session finished - CLOSE')

print('=' * 30)

# Context manager method
name, phone, email = 'ABC', '3366858', 'user@example.com'

try:
    with sqlite3.connect('contacts.sqlite') as db:
        # Opening this way will commit if no errors were raised and will roll
        # back automatically if any error occurred
        db.execute('''INSERT INTO users(name, phone, email)
                  VALUES(?,?,?)''', (name, phone, email))
except sqlite3.IntegrityError:
    print('Record already exists')
finally:
    db.close()
    print('Closed')
