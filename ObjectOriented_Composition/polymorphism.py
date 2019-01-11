"""
The word POLYMORPHISM means that objects in Python can behave as multiple types. That is because they inherit their
attributes from the base class object(), and Python is a dynamically typed language.
For example, a type int can behave as a str when it's printed, because
it has inherit the __str__ method from the super class object().
"""


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Weee, thi is fun')
        elif self.ratio == 1:
            print('This is hard work, but I\'m flying')
        else:
            print('I think I\'ll just walk')


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)  # this is composition

    @staticmethod
    def quack():
        print('Quack quack')

    def fly(self):
        self._wing.fly()


class BlackDuck(Duck):

    def __init__(self):
        super().__init__()
        self._wing = Wing(0.7)

    def fly(self):
        print('Don\'t u see my black wings?')
        super().fly()


if __name__ == '__main__':
    donald = Duck()
    # we can call donald.fly() (Duck Object), which actually calls Wing.fly() (Wing Object)
    # they are both of different types, but both understand the method fly(), therefore it works
    dlanod = BlackDuck()
    donald.fly()
    dlanod.fly()
