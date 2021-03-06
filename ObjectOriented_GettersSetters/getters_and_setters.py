class Player:
    def __init__(self, name):
        self.name = name

        # Private data attributes
        self._lives = 3
        self._level = 1
        self._score = 0

    # Getter, a method that returns the value of an attribute
    def _get_lives(self):  # _ to show that it's private and these methods shouldn't be used
        print('I\'m a Getter for _lives')
        return self._lives

    # Setter, a method that reassigns the value of an attribute
    def _set_lives(self, lives):
        print('I\'m a Setter for _lives')
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives cannot be negative')
            self._lives = 0

    # Property class constructor, property can't have the same name as data attribute
    # property(@get method, @set method, @del method, @doc method)
    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level

    level = property(_get_level, _set_level)

    # Another syntax for properties, using decorators; it has the same use and result
    @property  # Decorator, this creates the property and access the getter method
    def score(self):  # It's at the same time the name of the property and the getter method
        return self._score

    @score.setter  # This decorator assigns the setter method to the specified property
    def score(self, score):
        self._score = score

    # __str__ method is called when using print(object)
    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, ' \
               'Score: {0.score}'.format(self)


bldr = Player('BLDR')

print(bldr)  # Calling the __str__ method

print(bldr.name)  # Printing specific data attribute
# Since 'lives' is a property of the object, trying to call the attribute like this
# causes the getter method to be called
print(bldr.lives)

# And this, calls the setter method
bldr.lives = 5
print(bldr)

# Augmented assignment also works for setters
bldr.level += 3
print(bldr)

bldr.level -= 1
print(bldr)

# Setter method, property created using decorators
bldr.score = 500
print(bldr)
