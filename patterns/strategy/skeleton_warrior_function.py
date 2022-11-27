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
from typing import Callable
from dataclasses import dataclass


@dataclass
class Skeleton:
    name: str
    attack_strategy: AttackStrategy

    def attack(self):
        self.attack_strategy(self)


AttackStrategy = Callable[[Skeleton], None]


def charge(skeleton: Skeleton) -> None:
    print(f"{skeleton.name} charges directly at you.")


def charge_zigzag(skeleton: Skeleton) -> None:
    print(f"{skeleton.name} charges at you in a zig zag pattern.")


def circle(skeleton: Skeleton) -> None:
    print(
        f"{skeleton.name} circles around you, attemping",
        "to stab you in the back.",
    )


def main():
    urd = Skeleton(name="Urd", attack_strategy=charge)
    mard = Skeleton(name="Mard", attack_strategy=charge_zigzag)
    saag = Skeleton(name="Saag", attack_strategy=circle)
    skeletons = [urd, mard, saag]
    for skeleton in skeletons:
        skeleton.attack()


if __name__ == "__main__":
    main()
