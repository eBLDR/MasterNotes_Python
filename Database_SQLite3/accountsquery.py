import sqlite3
import pytz

# connect#1
# db = sqlite3.connect('accounts.sqlite')

# connect#2
db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute('SELECT * FROM history'):
    utc_time, name, amount = row
    # changing to local time
    local_time = pytz.utc.localize(utc_time).astimezone()
    print('UTC: {}\t Local: {}\nType: {}'.format(
        utc_time, local_time, type(local_time))
    )
    # the column TIMESTAMP is str using connect#1
    # the column TIMESTAMP is original datetime using connect#2

db.close()
