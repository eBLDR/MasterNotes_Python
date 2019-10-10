"""
For docstring convention see PEP 257
"""


class TRex:
    """ Class docstring.
    Represents a T-Rex dinosaur.
    """

    diet = 'carnivore'

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        self.alive = True

    def has_died(self):
        """ Method docstring.
        Dinosaur has passed away.
        """
        self.alive = False

    # If no docstring is written, comment above method definition will be taken
    def no_doc(self):
        pass

    # def __doc__(self):
    # Will override the docstring specified on the class, if desired.


# Displaying docstrings
help(TRex)

# to print only the docstring of the class
print(TRex.__doc__)

# to print only the docstring of a method of the class
print(TRex.has_died.__doc__)
