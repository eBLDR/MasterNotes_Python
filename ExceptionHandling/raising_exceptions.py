"""
Scripts finished with an exception being raised (either at will or by accident)
will exit with code 1 - instead of the usual 0.
"""


class Fin:
    @staticmethod
    def swim():
        print('Powerful fin!')


class Shark:

    def __init__(self):
        self._fin = Fin()

    def swim(self):
        self._fin.swim()
        print('I\'m gonna eat you')


class Intruder:
    # pass

    # Comment out the following method to test the custom exception
    @staticmethod
    def swim():
        print('Shhh...! I\'m using a DPV!')


class School:

    def __init__(self):
        self.school = []

    # function annotation: type Shark expected - to display the warning
    def add_shark(self, shark: Shark) -> None:

        # Verifying that all object have the "swim" method
        swim_method = getattr(shark, 'swim', None)

        if callable(swim_method):
            self.school.append(shark)
        else:
            # Custom exceptions, personalized error message
            raise TypeError('Cannot add shark, are you sure it\'s not a '
                            + str(type(shark).__name__) + ' ?')

    def migrate(self):
        problem = None
        for shark in self.school:
            try:
                shark.swim()

                # We can force to raise the exception to test our exception
                # handling
                # raise AttributeError('Testing exception handler!')

            # Storing the exception in a variable that we can use
            except AttributeError as e:  # e is type object exception
                print('!!! Someone cannot swim !!!')
                problem = e

                # raise  # calling raise here will re-raise the same exception
                # that we've just caught

        if problem:
            # Raising the problem here allows the migrate function to finish
            # instead of stopping half way
            print('\nI am raising the problem now, once everyone has swum.')

            # To raise an exception, must be Exception type (or subclass)
            raise problem


nemo = Shark()
nemo.swim()

print('=' * 30)

school = School()

for i in range(3):
    if i == 1:
        school.add_shark(Intruder())

    school.add_shark(Shark())

school.migrate()
