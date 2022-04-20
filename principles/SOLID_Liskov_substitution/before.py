"""
You should be able to replace objects in a program with
 instances of their subtypes without altering the correctness of
 the program.


Subtypes must be substitutable for their base types. To be substitutable,
 the subtype must behave like its supertype.
"""
from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def lay_an_egg(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Duck(Bird):
    def lay_an_egg(self):
        print("Duck laying an egg")

    def fly(self):
        print("Flying duck")


class Ostrich(Bird):
    def lay_an_egg(self):
        print("Ostrich laying an egg")

    def fly(self):
        pass


"""
The Ostrich is a subclass of Bird, but it cannot fly!
"""
