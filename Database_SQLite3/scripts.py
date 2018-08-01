import sqlite3

db = sqlite3.connect(':memory:')  # Using a db in ram
c = db.cursor()

# Writting the script
script = '''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT);
            CREATE TABLE accounts(id INTEGER PRIMARY KEY, description TEXT);
            
            INSERT INTO users(name, phone) VALUES ('John', '5557241'), 
            ('Jim', '5547874'), ('Jack', '5484522');'''

# This command will execute the @script passed, the script can have
# multiple statements
c.executescript(script)
 
# Print the results
c.execute('''SELECT * FROM users''')
for row in c:
    print(row)
 
db.close()

# If the script is found on a text file
file = open('myscript.sql', 'r')
script = file.read()
c.executescript(script)
file.close()
