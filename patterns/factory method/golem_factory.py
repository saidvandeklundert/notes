from abc import ABC, abstractmethod


class Golem(ABC):
    """The base class for a Golem"""

    @abstractmethod
    def great(self) -> str:
        """give greeting"""
        pass


class FireGolem(Golem):
    def great(self) -> str:
        return """FireGolem ready"""


class ClayGolem(Golem):
    def great(self) -> str:
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
    print(golem.great())


if __name__ == "__main__":
    clay = ClayGolem()
    print(clay.great())
    fire = FireGolem()
    print(fire.great())

    # now using the read_factory
    clay_factory = read_factory("clay")
    clay_1 = clay_factory.get_golem()
    print(clay_1.great())
    fire_factory = read_factory("fire")
    fire_1 = fire_factory.get_golem()
    print(fire_1.great())

    # now passing a factory into main:
    fac_result = read_factory("fire")
    main(factory=fac_result)