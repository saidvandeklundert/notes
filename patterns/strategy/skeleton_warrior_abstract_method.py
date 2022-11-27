"""
Strategy pattern for skeleton warriors a game.

During the initialization of the skeleton warrior,
 the skeleton is given an attack strategy.

Using:
- abstract method
- protocol
- function
- callable 
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, skeleton: Skeleton) -> None:
        ...


class Charge(AttackStrategy):
    def attack(self, skeleton: Skeleton) -> None:
        print(f"{skeleton.name} charges directly at you.")


class ChargeZigZag(AttackStrategy):
    def attack(self, skeleton: Skeleton) -> None:
        print(f"{skeleton.name} charges at you in a zig zag pattern.")


class Circle(AttackStrategy):
    def attack(self, skeleton: Skeleton) -> None:
        print(
            f"{skeleton.name} circles around you, attemping",
            "to stab you in the back.",
        )


@dataclass
class Skeleton:
    name: str
    flight_method: AttackStrategy

    def attack(self):
        self.flight_method.attack(self)


def main():
    urd = Skeleton(name="Urd", flight_method=Charge())
    mard = Skeleton(name="Mard", flight_method=ChargeZigZag())
    saag = Skeleton(name="Saag", flight_method=Circle())
    skeletons = [urd, mard, saag]
    for skeleton in skeletons:
        skeleton.attack()


if __name__ == "__main__":
    main()
