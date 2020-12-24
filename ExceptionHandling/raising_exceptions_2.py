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

    def add_shark(self, shark: Shark) -> None:
        # Verifying that object has the "swim" method
        swim_method = getattr(shark, 'swim', None)

        if not callable(swim_method):
            raise TypeError(
                f'Cannot add shark, are you sure it\'s not a {type(shark).__name__} ?'
            )

        self.school.append(shark)

    def migrate(self):
        problem = None
        for shark in self.school:
            try:
                shark.swim()
            except AttributeError as e:
                print('!!! Someone cannot swim !!!')
                problem = e

        if problem:
            # Raising the problem here allows the migrate function to finish
            # instead of stopping half way
            print('\nI am raising the problem now, once everyone has swum.')

            raise problem


nemo = Shark()
nemo.swim()

print('=' * 30)

school = School()

for i in range(3):
    school.add_shark(Shark())

# Adding corrupted object to array
school.add_shark(Intruder())

school.migrate()
