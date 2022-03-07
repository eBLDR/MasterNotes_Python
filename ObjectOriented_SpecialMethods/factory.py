"""
Factory methods are frequently used to build an instance from
dictionary-like data.
"""
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.populated = False

    # Using a class method as a factory
    @classmethod
    def from_birth_year(cls, name, birth_year):
        # cls() can create instances of the class
        # Must take the same arguments as __init__ method
        age = date.today().year - birth_year

        new_instance = cls(name, age)
        print(type(new_instance))

        new_instance.populate()

        return new_instance

    def display(self):
        print(f"{self.name}'s age is: {self.age}. Populated: {self.populated}")

    def populate(self):
        self.populated = True


person = Person('Tom', 36)
person.display()

# Creating an object using class method factory
person1 = Person.from_birth_year('Sherlock', 1854)
person1.display()
