"""
Getters & setters for private data attributes.

Encapsulation techniques - underscore naming usage:

' _item ' Object names (variables, attributes, methods...) starting with a single underscore, are supposed to be
NON-PUBLIC, although nothing stops us to access it. NON-PUBLIC means that the object should not be used outside
of the class where it's declared. And are not imported when importing a module.

' __item ' Object names starting with 2 underscores (and NOT finishing with 2 underscores) (Aka dunderscore or dunder)
results in name mangling; are supposed to be private. They can only be called from inside the class itself.
Mangling is a Python technique that renames the original item if we try to edit it, and creates a new one using the
original name with the new value. Are imported.
Example: __mangled is declared inside __init__, we try to edit it instance.__mangled = 1, Python will automatically
rename __mangled to _className.__mangled, and its value will remain unchanged. Will also create a new variable called
__mangled, and its value will be the new one.

' __item__ '  is a convention to minimize conflicts in case one wishes to use a similar name for another function,
have no effect.
"""


class Player:

    def __init__(self, name):
        self.name = name
        self._lives = 3  # _attribute to show that it should be private
        self._level = 1
        self._score = 0
        self.__mangle = None  # just for the example of name mangling

    # Getter, a method that returns the value of an attribute
    def _get_lives(self):  # _ to show that it's private and these methods should'nt be used
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
    @property           # Decorator, this creates the property and access the getter method
    def score(self):    # It's at the same time the name of the property and the getter method
        return self._score

    @score.setter       # This decorator assigns the setter method to the specified property
    def score(self, score):
        self._score = score

    # __str__ method is called when using print(object)
    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, ' \
               'Score: {0.score}'.format(self)

    # Private method - can only be called from inside the class
    def __private(self):
        pass


bldr = Player('BLDR')

print(bldr)         # calling the __str__ method

print(bldr.name)    # printing specific data attribute
print(bldr.lives)   # since 'lives' is a property of the object, trying to call the attribute like this
                    # causes the getter method to be called

bldr.lives = 5      # and this, calls the setter method
print(bldr)

bldr.level += 3
print(bldr)

bldr.level -= 1
print(bldr)

bldr.score = 500    # setter method, property created using decorators
print(bldr)

# mangling
bldr.__mangle = 30    # trying to edit a mangled attribute
print(bldr.__mangle)
print(bldr.__dict__)   # here we can see mangling working, _Player_mangle attribute has been created

# trying to call a private method from outside will raise an error
# bldr.__private()
