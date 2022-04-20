"""
The before Bird class is changed into a 'Bird' and a 'FlyingBird'.

This let's us creates subclasses fir all birds without violating
 the Listkov substitution principle.
"""
from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def lay_an_egg(self):
        pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Duck(FlyingBird):
    def lay_an_egg(self):
        print("Duck laying an egg")

    def fly(self):
        print("Flying duck")


class Ostrich(Bird):
    def lay_an_egg(self):
        print("Ostrich laying an egg")
