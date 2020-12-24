import inheritance as enemies


class Gang:
    """ Creating a gang of enemies """

    def __init__(self):
        self.gang = []

    def add_enemy(self, enemy: enemies.Enemy) -> None:

        # Checking the type is a BAD option to filter parameters
        # if type(enemy) is Enemy:  # Bad because will not catch instances

        # Better is to use
        # if isinstance(enemy, Enemy):  # instance, super class

        # In Python, if something can 'behave like an enemy then it's an enemy', so the best is to use:
        take_damage_method = getattr(enemy, 'take_damage', None)
        # getattr (get attribute) searches in the class dictionary for the specified name
        # attribute, returns None in case the attribute doesn't exists

        print(take_damage_method)

        # callable checks if the attribute is a method (so it's callable) rather than data
        if callable(take_damage_method):
            self.gang.append(enemy)
        else:
            raise TypeError('Cannot add enemy, looks like it\'s a ' + str(type(enemy).__name__))

    def suffering(self, dmg):
        for enemy in self.gang:
            enemy.take_damage(dmg)


e1 = enemies.Troll('BigTroll')
e2 = enemies.Vampire('ColdVamp')

gang = Gang()

gang.add_enemy(e1)
gang.add_enemy(e2)

gang.suffering(5)
