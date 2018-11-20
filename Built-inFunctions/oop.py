class Mock:
    def __init__(self):
        self.mock_attr = 1


class Mack(Mock):
    pass


mock = Mock()

# isinstance(obj, class) - returns True if obj is type class
print('isinstance(mock, Mock):', isinstance(mock, Mock))
# Can take a tuple of classes
print('isinstance(1, (list, int)):', isinstance(1, (list, int)))

print('=' * 20)

attr_name = 'mock_attr'

# hasattr(obj, attr_name) - returns True if obj has attr
print('hasattr(mock, attr_name):', hasattr(mock, attr_name))

# getattr(obj, attr_name) - returns obj.attr_name
print('getattr(mock, attr_name):', getattr(mock, attr_name))

# setattr(obj, attr_name, new_value) - updates the value of obj.attr_name, it can set new attributes
print('setattr(mock, attr_name, 0)')
setattr(mock, attr_name, 0)
print('mock.mock_attr: ', mock.mock_attr)

# delattr(obj, attr_name) - deletes obj.attr_name
print('delattr(mock, attr_name)')
delattr(mock, attr_name)

print('=' * 20)

# issubclass(class, parent_class) - returns True if obj is type class
print('issubclass(Mack, Mock):', issubclass(Mack, Mock))
# Can take a tuple of classes
print('issubclass(Mack, (dict, Mock)):', issubclass(Mack, (dict, Mock)))

