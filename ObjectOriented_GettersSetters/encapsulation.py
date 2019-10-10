# Using encapsulation for mangling and private attributes.
# See encapsulation.txt


class TopSecret:
    def __init__(self, name):
        self.name = name

        # Defining protected attributes, _<attr>
        # To show that it should be private
        self._members = ['Bond', 'Leiter', 'M']

        # Private method - example of name mangling
        self.__secret_code = 7

    # Protected method
    def _protected(self):
        print('I am a protected method from {}, with members: {}'.format(
            self.name, ', '.join(self._members)
        ))

    # Private method - can only be called from inside the class
    def __reveal(self):
        # Private attributes and methods can be accessed from inside the class
        print('Secret code is {}'.format(self.__secret_code))

    def decrypt(self, code):
        if code == self.__secret_code:
            self.__reveal()
        else:
            print('Wrong code! {}'.format(code))


top_secret = TopSecret('MI6')

# Calling protected attributes and methods is permitted
print(top_secret._members)
top_secret._protected()

print('=' * 30)

# Here we can see mangling working, _<class>__<attr> have been created
print(dir(top_secret))

# __dict__ does not show private attributes, but it does show protected ones
print(top_secret.__dict__)

# Calling a private attribute will raise an error
try:
    print(top_secret.__secret_code)
except AttributeError as exc:
    print(exc)

# Calling a private method from outside will raise an error
try:
    top_secret.__reveal()
except AttributeError as exc:
    print(exc)

print('=' * 30)
new_code = 24

print('Updating secret code to {}...'.format(new_code))
top_secret.__secret_code = new_code  # Editing a mangled attribute is possible...
print(top_secret.__secret_code)

# But when dealt from inside a class it still refers to the original value!
top_secret.decrypt(new_code)

top_secret.decrypt(7)
