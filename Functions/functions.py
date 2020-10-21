"""
Functions are blocks of code that can be reusable. In a process that is called "procedural decomposition".
All functions RETURN something, if not specified, default = None
PARAMETER refers to the variables defined in the function (may have 0).
ARGUMENT refers to the actual objects used when the function is called.
LOCAL VARIABLES can be created inside the function, and are deleted when the function is finished.
Ensure to provide documentation.
Care of the type of the variable.
"""


def test_function():
    """
    Documentation string goes here - also called 'function signature' or
    'docstring'.
    pep257 talk about the style of docstrings.
    """
    # pass  # A command that does nothing

    print('I\'m a useless function')


# To print the name of the function, str
print(test_function.__name__)

# To print the docstring of the function, str
print(test_function.__doc__)

# Call the function
test_function()

# To see the returned value
print(test_function())

what = print('A')
# This will print None, since print() does not return anything
print(what)

print('=' * 20)


def get_char(prompt):
    """
    Ask to the user to input a character/s using specific prompt.
    :param prompt: text to be displayed :type str
    :return: c: character/s that had been input by the used :type str
    """
    while True:
        c = input(prompt)

        # Return will send the variable/s specified out of the function,
        # it also stops the execution of the function
        return c

        # Return can also be typed alone, it will break the function and return None
        # return


char = get_char('Type something: ')
print(char)

print('=' * 20)


# Keyword parameters (or named parameters) (i.e.: key_word_par = None)
# Must be specified after normal parameters and must have a default value
def say(message, times=1):
    print(message * times)


# We can specify the named parameters, if not, they are set by default
say('Hello')
say('World', times=5)

print('=' * 20)

# Keyword parameters can be specified referring an existing variable
default = 'whats\'up'


def speak(text=default):
    print(text)


speak()

print('=' * 20)

# callable(@arg) - True if an object is a function/method
print(f'callable(speak): {callable(speak())}')
