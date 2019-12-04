"""
Abstract Base Classes (ABC).
An abstract class does not allow to instantiate objects from it, only
another subclass can be derived from it.
"""
import abc


class MyABC(metaclass=abc.ABCMETA):

    def __init__(self):
        pass

    @abc.abstractmethod
    def my_abstract_method(self):
        """ Using this decorator requires that the class’s metaclass is ABCMeta
        or is derived from it. A class that has a metaclass derived from
        ABCMeta cannot be instantiated unless all of its abstract methods and
        properties are overridden. """

        raise NotImplementedError('Subclass must override this method.')
