import datetime

import pytz


class Account:
    """ Simple account class with balance. """

    # @item are called DECORATORS
    @staticmethod  # <- this and removing the self parameter, we turn the method to a STATIC METHOD
    # static methods don't have access to the attributes of an instance of a class nor to the attributes of the class
    def _current_time():  # starting with _ means that the method is non public (by convention)
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print('Account created for ' + self.name)
        self.show_balance()  # will call function when initialise

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()  # to show balance every time we call the method
            self.transaction_list.append((Account._current_time(), amount))
            # we could also use self._current_time(), but that will cause that python first search in the
            # instance's method, and then in the class namespace (so it will take longer)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print('Must be greater than zero and less than {}'.format(self.balance))
        self.show_balance()

    def show_balance(self):
        print('Balance is {}'.format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on UTC {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    edu = Account('Edu', 0)
    edu.show_balance()
    edu.deposit(1000)
    # edu.show_balance()
    edu.withdraw(5000)
    # edu.show_balance()
    edu.withdraw(500)
    edu.show_transactions()

    oscar = Account('Oscar', 800)
    oscar.show_transactions()
