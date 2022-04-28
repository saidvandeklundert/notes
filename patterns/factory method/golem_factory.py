"""
Factory Method Design Pattern

Intent: Provides an interface for creating objects in a superclass, but allows
subclasses to alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod


class Golem(ABC):
    """The base class for a Golem"""

    @abstractmethod
    def greet(self) -> str:
        """give greeting"""
        pass


class FireGolem(Golem):
    def greet(self) -> str:
        return """FireGolem ready"""


class ClayGolem(Golem):
    def greet(self) -> str:
        return """ClayGolem ready"""


class GolemFactory(ABC):
    """Factory that churns out Golems without
    taking ownership over the instances."""

    @abstractmethod
    def get_golem(self) -> Golem:
        """Returns a Golem."""


class FireGolemFactory(GolemFactory):
    """Factory for FireGolems"""

    def get_golem(self) -> Golem:
        return FireGolem()


class ClayGolemFactory(GolemFactory):
    """Factory for FireGolems"""

    def get_golem(self) -> Golem:
        return ClayGolem()


def read_factory(golem_type: str) -> GolemFactory:
    golems = {
        "clay": ClayGolemFactory(),
        "fire": FireGolemFactory(),
    }
    return golems[golem_type]


def main(factory: GolemFactory):
    """A main function using dependancy inversion,
    by depending on an abstract class that is a factory
    that returns a conrete class."""
    golem = factory.get_golem()
    print(golem.greet())


if __name__ == "__main__":
    clay = ClayGolem()
    print(clay.greet())
    fire = FireGolem()
    print(fire.greet())

    # now using the read_factory
    clay_factory = read_factory("clay")
    clay_1 = clay_factory.get_golem()
    print(clay_1.greet())
    fire_factory = read_factory("fire")
    fire_1 = fire_factory.get_golem()
    print(fire_1.greet())

    # now passing a factory into main:
    fac_result = read_factory("fire")
    main(factory=fac_result)
