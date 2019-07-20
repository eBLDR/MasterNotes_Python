import sqlite3
import pytz
import datetime

db = sqlite3.connect('accounts.sqlite')
db.execute('DROP TABLE IF EXISTS accounts')
db.execute('DROP TABLE IF EXISTS history')
# db.execute('DELETE FROM accounts')  # to clear the table
db.execute(
    'CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, '
    'balance REAL NOT NULL)'
)
db.execute(
    'CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,'
    'account TEXT NOT NULL, amount REAL NOT NULL, PRIMARY KEY (time, account))'
)


class Account:

    @staticmethod
    def _current_time():
        """ Notice that is UTC time, no timezone included """
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute(
            'SELECT name, balance FROM accounts WHERE (name = ?)', (name,)
        )
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print(row)
            print('Retrieved record for {}.'.format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute(
                'INSERT INTO accounts VALUES(?, ?)', (name, opening_balance)
            )
            cursor.connection.commit()
            print('Account created for {}.'.format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self._save_update(amount)
            print('{:.2f} deposited'.format(amount))
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print('{:.2f} withdrawn.'.format(amount))
            return amount
        else:
            print('The amount must be greater than zero and no more '
                  'than {:.2f}.'.format(self._balance))
            return 0.0

    def show_balance(self):
        print('Balance on account {} is {:.2f}'.format(
            self.name, self._balance)
        )

    def _save_update(self, amount):
        new_balance = self._balance + amount
        withdrawal_time = Account._current_time()
        print(Account._current_time())  # testing
        try:
            db.execute(
                'UPDATE accounts SET balance = ? WHERE name = ?',
                (new_balance, self.name)
            )
            db.execute(
                'INSERT INTO history VALUES(?, ?, ?)',
                (withdrawal_time, self.name, amount)
            )

        except sqlite3.Error:
            db.rollback()  # to delete the last update before it's committed

        else:
            db.commit()
            self._balance = new_balance


# remember the rounding problem when working with floats!
# (see binaryroundproblem.py)
if __name__ == '__main__':
    bldr = Account('BLDR')
    bldr.deposit(110)
    bldr.deposit(10)
    bldr.deposit(10)
    bldr.withdraw(30)
    bldr.show_balance()

    ojka = Account('Ojka')
    coka = Account('Coka', 500)
    eloi = Account('Eloi', 25)

    db.close()
