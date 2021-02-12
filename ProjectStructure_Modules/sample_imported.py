"""
Module docstring - cool.
"""
# Sometimes is useful to add version of module
__version__ = '0.1'

# __name__ changes depending on the way the file is run, either the file is
# imported (file name) or run directly (__main__)
print(__name__)  # is type <str>
print('Why\'r u importin\' me?')


def hi():
    print('I\'m a function inside ' + __name__)
    print('Version', __version__)


key = bin(24)
super_key = hex(100)

if __name__ == '__main__':
    print('You\'ll only see me when I\'m not being imported')
