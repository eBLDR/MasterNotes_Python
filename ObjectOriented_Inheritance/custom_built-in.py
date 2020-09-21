# Inherit from built-in class
class CustomList(list):
    def get_values(self, value):
        """ Filtering objects with a condition. """
        return [
            obj for obj in self if obj == value
        ]


class CustomDict(dict):
    def longest_key(self):
        """
        Finds the longest key in the dictionary.
        :return: <str>
        """
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


stellar = CustomDict()
print(type(stellar))

print(isinstance(stellar, dict))

# It can be treated as a normal dict
stellar['blue'] = 'O'
stellar['white'] = 'A'
stellar['yellow'] = 'G'

# With the new behaviour added
print(stellar.longest_key())

print('=' * 30)

normal_dict = {
    'blue white': 'B',
    'yellow white': 'F',
    'light orange': 'K',
    'orange red': 'M'
}

# Initialization can also be done in this way,
# resorting on the default __init__ method
stellar_2 = CustomDict(normal_dict)
print(type(stellar_2))
print(stellar_2.longest_key())
