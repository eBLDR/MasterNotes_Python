"""
SUPER CLASS - is the base class
SUB CLASS - inherits from a super class
INHERITANCE - will inherit all the attributes, properties and methods
MULTIPLE INHERITANCE - is also possible, a sub class inheriting from many super classes
"""


class Enemy(object):
    """ Super Class """

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        """ Constructor class with optional parameters """
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points > 0:
            self._hit_points = remaining_points
            print('{0._name} took {1} points damage and have {0._hit_points} left'.format(self, damage))
        else:
            self._lives -= 1
            if self._lives > 0:
                print('{0._name} lost a live'.format(self))
            else:
                print('{0._name} is dead'.format(self))
                self._hit_points = 0
                self._alive = False

    def __str__(self, annex=''):
        return ('Name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}' + annex).format(self)


class Troll(Enemy):
    """ Troll is a Sub Class of Enemy, it's inheriting data from Enemy """

    def __init__(self, name, iq=1):
        # using Super class constructor method
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

        # using Super method
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)

        # equivalent to
        super().__init__(name=name, hit_points=23)  # specify parameters, or not for using default

        self._iq = iq  # we can create data attributes only for the subclass

    def grunt(self):
        print('Me {0._name}. {0._name} stomp you'.format(self))

    def __str__(self):
        annex = ', Iq: {0._iq}'
        return super().__str__(annex)


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        import random  # just to show that it's possible to import anywhere
        if random.randint(1, 3) == 3:
            print('*** {0._name} dodges ***'.format(self))
            return True
        else:
            return False

    # overriding methods!
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)  # calling the super method


# sub class of Vampire (aka extension of the class Vampire)
class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)


if __name__ == '__main__':
    random_monster = Enemy('Basic Enemy', 12, 1)

    print('\n--- TESTING ENEMY SUPER CLASS ---\n')

    print(random_monster)

    random_monster.take_damage(4)
    print(random_monster)

    print('\n--- TESTING TROLL SUB CLASS ---\n')

    ugly_troll = Troll('Ugly')
    print('Ugly Troll - {}'.format(ugly_troll))

    ug_troll = Troll('Ug', 8)
    print('Ug Troll - {}'.format(ug_troll))
    ug_troll.take_damage(17)
    print('Ug Troll - {}'.format(ug_troll))

    urg_troll = Troll('Urg', iq=5)
    print(urg_troll)

    print('\n--- TESTING ALIVE IN TROLL SUB CLASS ---\n')

    while urg_troll._alive:
        urg_troll.take_damage(5)
        print(urg_troll)

    """
    Overloading methods are used in other languages (such as Java or C++) to use different versions
    of the method depending on the number and type of arguments that are passed to it.
    Python doesn't have such a thing, the arguments are assigned by order, by named parameters,
    or set to default if not specified. (See functions.)
    """

    print('\n--- TESTING METHODS IN SUBCLASS ---\n')

    urg_troll.grunt()

    print('\n--- TESTING VAMPIRE SUB CLASS ---\n')

    vlad = Vampire('Vlad')
    print(vlad)
    while vlad._alive:
        vlad.take_damage(5)
    print(vlad)

    print('\n--- TESTING VAMPIRE KING SUB CLASS ---\n')

    king = VampireKing('King')
    print(king)

    for i in range(4):
        king.take_damage(50)
    print(king)

    print('\nisinstance() function\n')
    # isinstance(@object, @class or @type or (@class_1, @class_2))
    # Returns a boolean if @object is instance of @class
    print('isinstance(king, VampireKing):', isinstance(king, VampireKing))
    print('isinstance(king, Vampire):', isinstance(king, Vampire))
