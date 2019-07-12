"""
Module docstring - cool.
"""

# the __name__ changes depending on either the file is imported (file name) or not (__main__)
print(__name__)  # is type <str>
print('Why\'r u importin\' me?')


def hi():
    print('I\'m a function inside ' + __name__)


key = bin(24)
superKey = hex(100)

if __name__ == '__main__':
    print('You\'ll only see me when I\'m not being imported')
