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
    Documentation goes here.
    """
    # pass  # a command that does nothing :)

    print('I\'m a useless function')


print(test_function.__name__)  # to print the name of the function, str

# call the function
test_function()
print(test_function())  # to see what's returned

what = print("A")
print(what)  # this will print None, since print() does not return anything

print('=' * 20)


# Function annotations (or type hints), provides info about the type of the parameter expected (are optional)
# it can also be a customized class
def get_char(prompt: str) -> str:  # -> return Type - hint about the type returned
    """
    Ask to the user to input a character/s using specific prompt.
    :param prompt: text to be displayed :type str
    :return: c: character/s that had been input by the used :type str
    """
    while True:
        c = input(prompt)
        return c  # return will send the variable/s specified, it also stops the execution of the function
        # return  # return can also be typed alone, it will break the function and return None

char = get_char('Type something: ')
print(char)

print('=' * 20)


# *args can take any number of arguments, passed to the function in a tuple
# keyword parameters (or named parameters) (i.e.: key_word_par = None)
def centre_text(*texts, sep_char=' ', end_char='\n', file=None):  # named parameters are set to default
    text = ""
    for arg in texts:
        text += str(arg) + sep_char  # list comprehension method is more efficient, but for now we stick to this
    left_margin = (50 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=file)


# saving to a file
with open('centred.txt', mode='w') as centredFile:
    centre_text('Twelve', file=centredFile)
    centre_text('in binary is', file=centredFile)
    centre_text(1100, file=centredFile)
    centre_text('or 0000 1100 in 1 byte', file=centredFile)
    centre_text('or C in hex', file=centredFile)
    centre_text('it can', 'also take', 'several number of', 'arguments', sep_char='-sep-', file=centredFile)


def happy_text(*texts, sep=' :) '):
    text = ''
    for arg in texts:
        text += str(arg) + sep
    return text  # will return whatever type/variable


print(happy_text('I', 'am', 'damn', 'happy', sep=' :( '))  # we can specify the named parameters, if not, they are set
# to default
happy1 = happy_text('Assigning', 'returned', 'values')
print(happy1)
