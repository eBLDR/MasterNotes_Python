# Multiple inheritance is also possible, a sub class inheriting from many super classes
import datetime


class A:
    def __init__(self):
        self.attr = 'From A'


class B:
    def func(self):
        print('From B')


class C(A, B):
    """Multiple inheritance, will inherit attributes and methods from all its
    base classes."""


c = C()
print(c.attr)
c.func()

print('=' * 20)


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


class Clock(Time, Date):
    def __init__(self, year, month, day, hour, minute, second):
        # super() will call refer to the first base class declared
        print('super().__init__ is: ', super().__init__)

        # __init__ calls have to be called manually for each, with self specified
        Time.__init__(self, hour, minute, second)
        Date.__init__(self, year, month, day)

    def display(self):
        print(f'{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}')


now = datetime.datetime.utcnow()
clock = Clock(
    year=now.year, month=now.month, day=now.day,
    hour=now.hour, minute=now.minute, second=now.second,
)

clock.display()
