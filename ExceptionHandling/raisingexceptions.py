class Fin(object):

    def swim(self):
        print('I\' gonna eat you')


class Shark(object):

    def __init__(self):
        self._fin = Fin()  # Composition

    def swim(self):
        self._fin.swim()


class Intruder(object):
    """ Replace all the following methods for pass to test the custom exception """

    # pass

    def __init__(self):
        self.dpv = self.swim

    def swim(self):
        print('Shhh...! I\'m using a DPV!')


class School(object):

    def __init__(self):
        self.school = []

    # function annotation: type Shark expected
    def add_shark(self, shark: Shark) -> None:

        swim_method = getattr(shark, 'swim', None)

        if callable(swim_method):
            self.school.append(shark)
        else:
            # custom exceptions, personalized error message
            raise TypeError('Cannot add shark, are you sure it\'s not a ' + str(type(shark).__name__) + ' ?')

    def migrate(self):
        problem = None
        for shark in self.school:
            try:
                shark.swim()
                # we can force to raise the exception to test our exception handling
                raise AttributeError('Testing exception handler!')

            # storing the exception in a variable that we can use
            except AttributeError as e:  # e is type object exception
                print('!!! Someone cannot swim !!!')
                problem = e  # saving the exception

                # raise  # calling raise here will re-raise the same exception that we've just caught

        if problem:
            # raising the problem here allows the migrate function to finish instead of stopping half way
            print('\nI am raising the problem now, once everyone has swum.')
            print(problem.args)  # Attribute containing the message (tuple)
            raise problem


if __name__ == '__main__':
    nemo = Shark()
    nemo.swim()
