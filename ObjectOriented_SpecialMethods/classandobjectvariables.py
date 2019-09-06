"""
There are two types of fields, depending on whether the class or the object
owns the variables respectively.

CLASS VARIABLES: are shared , they can be accessed by all instances of that class. There is
only one copy of the class variable and when any one object makes a change to a class
variable, that change will be seen by all the other instances.

OBJECT VARIABLES: are owned by each individual object/instance of the class. In this case,
each object has its own copy of the field i.e. they are not shared and are not related in any
way to the field by the same name in a different instance.
"""


class Robot:
    # Class variable
    population = 0

    def __init__(self, name):
        # Object variable
        self.name = name
        print('Initialising {}.'.format(self.name))

        # Updating class variable
        Robot.population += 1

        # Equivalent to
        # self.__class__.population += 1
        # self.__class__ refers to the object's class

    def die(self):
        print('{} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one. No robots alive...'.format(self.name))

        else:
            print('There are still {} robots working.'.format(Robot.population))

    def say_hi(self):
        print('Greetings, my masters call me {}.'.format(self.name))

    @classmethod
    def how_many(cls):
        print('We have {} robots.'.format(cls.population))

    # The following way is un-pythonic, using the decorator is advised
    # The same logic will work for staticmethod()
    # @classmethod decorator can be replaced by
    def are_there_some(cls):
        if cls.population > 0:
            print('Yes, there are some robots!')

        else:
            print('No robots out there!')

    are_there_some = classmethod(are_there_some)


Robot.are_there_some()
Robot.how_many()

r2_d2 = Robot('R2-D2')
c3po = Robot('C-3PO')

Robot.are_there_some()
Robot.how_many()
# Equivalent to calling the methods through the instance
c3po.how_many()

r2_d2.say_hi()
r2_d2.die()

Robot.how_many()

c3po.die()
