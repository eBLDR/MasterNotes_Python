# Multiple inheritance is also possible, a sub class inheriting from many super classes
import datetime


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# Multiple inheritance, will inherit attributes and methods from all the base classes
class Clock(Time, Date):
    def __init__(self, year, month, day, hour, minute, second):
        # super() will call to the first base class declared
        print('super().__init__ is: ', super().__init__)

        # __init__ calls have to be called manually for each, with self specified
        Time.__init__(self, hour, minute, second)
        Date.__init__(self, year, month, day)

    def display(self):
        print('{year}-{month}-{day} {hour}:{minute}:{second}'.format(
            year=self.year, month=self.month, day=self.day,
            hour=self.hour, minute=self.minute, second=self.second
        ))


now = datetime.datetime.utcnow()
clock = Clock(year=now.year, month=now.month, day=now.day,
              hour=now.hour, minute=now.minute, second=now.second)

clock.display()
