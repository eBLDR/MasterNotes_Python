"""
SUPER CLASS - is the base class
SUB CLASS - inherits from a super class
INHERITANCE - will inherit all the attributes, properties and methods
"""


class Enemy:
    """ Super Class """

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        """ Constructor class with optional parameters """
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print('{0.name} took {1} points damage and have {0.hit_points} left'.format(self, damage))
        else:
            self.lives -= 1
            if self.lives > 0:
                print('{0.name} lost a live'.format(self))
            else:
                print('{0.name} is dead'.format(self))
                self.hit_points = 0
                self.alive = False

    def __str__(self, annex=''):
        return ('Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}' + annex).format(self)


class Troll(Enemy):
    """ Troll is a Sub Class of Enemy, it's inheriting data from Enemy """

    def __init__(self, name, iq=1):
        # using Super class constructor method
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

        # using Super method
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)

        # Equivalent to
        super().__init__(name=name, hit_points=23)  # specify parameters, or not for using default

        print('super().__init__ is: ', super().__init__)

        self.iq = iq  # Create data attributes only for the subclass

    def grunt(self):
        print('Me {0.name}. {0.name} stomp you!'.format(self))

    def __str__(self, annex=None):
        annex = ', Iq: {0.iq}'
        return super().__str__(annex)


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        import random  # just to show that it's possible to import anywhere
        if random.randint(1, 3) == 3:
            print('*** {0.name} dodges ***'.format(self))
            return True
        else:
            return False

    # overriding methods!
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)  # calling the super method


# Multilevel inheritance
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

    while urg_troll.alive:
        urg_troll.take_damage(5)
        print(urg_troll)

    print('\n--- TESTING METHODS IN SUBCLASS ---\n')

    urg_troll.grunt()

    print('\n--- TESTING VAMPIRE SUB CLASS ---\n')

    vlad = Vampire('Vlad')
    print(vlad)
    while vlad.alive:
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
