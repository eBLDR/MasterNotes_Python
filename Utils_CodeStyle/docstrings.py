"""
For docstring convention styles see PEP 257.
Docstring style for official python documentation is reStructured Text.

Documentation string, also called 'function signature' or 'docstring',
is placed immediately following the class or (class) method indented by
one level. By doing so, the string literal will be set to __doc__.

All docstrings should have the same max character length as comments
(72 characters).

Three major categories:
    - Class Docstrings: Class and class methods
    - Package and Module Docstrings: Package, modules, and functions
    - Script Docstrings: Script and functions
"""


def one_line_docstring():
    """A simple function that does nothing."""


help(one_line_docstring)

# To print the docstring of the function, str
print(one_line_docstring.__doc__)

print('#' * 30)

"""
Multi-lined docstrings are used to further elaborate on the object
beyond the summary. All multi-lined docstrings have the following parts:
    - A one-line summary line
    - A blank line proceeding the summary
    - Any further elaboration for the docstring
    - Another blank line
"""


def multi_line_docstring():
    """Summary line.

    Further elaboration section.
    """

    # Notice the blank line above, code continues here.


help(multi_line_docstring)
print(multi_line_docstring.__doc__)

print('#' * 30)


def args_and_return__docstring(arg_1, arg_2, kwarg_1=False):
    """Summary line.

    :param arg_1: explanation of arg_1
    :type arg_1: str
    :param arg_2: explanation of arg_2
    :type arg_2: int
    :param kwarg_1: explanation of kwarg_1
        (default is False)
    :type kwarg_1: bool
    :return: explanation of what is returned
    :rtype: list
    """


help(args_and_return__docstring)
print(args_and_return__docstring.__doc__)

print('#' * 30)


class TRex:
    """Class docstring.

    Represents a T-Rex dinosaur.
    """

    diet = 'carnivore'

    def __init__(self, color, weight):
        """

        :param color: skin color
        :type color: str
        :param weight: mass in kg
        :type weight: float
        """
        self.color = color
        self.weight = weight
        self.alive = True

    def has_died(self):
        """Method docstring.

        Dinosaur has passed away.
        """
        self.alive = False

    # If no docstring is written, comment above method definition will
    # be taken.
    def no_doc(self):
        pass

    # def __doc__(self):
    # Will override the docstring specified on the class, if desired.


# Displaying docstrings
help(TRex)

print('#' * 30)

# Displays docstring of the class
print(TRex.__doc__)

print('#' * 30)

# Displays only the docstring of a method of the class
print(TRex.has_died.__doc__)
