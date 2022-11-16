"""
Ensure that high-level modules do not depend on low level modules, but instead depend on abstractions.
"""
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

"""
No dependancy inversion.
"""


@dataclass
class Laser:
    damage: int

    def shoot(self):
        print(f"laser causes {self.damage} damage")


@dataclass
class Robot:
    serial: str
    weapon: Laser


r2d2 = Robot(serial="r2d2", weapon=Laser(damage=21))

r2d2.weapon.shoot()


"""
Better because:
- we pass in a fully initialized object
- the higher level class (Robot) does not depend on a lower level class (Laser).
  We changed it so that it can wield any type of weapon

Weapon is now an interface, which is an abstraction.

This will allow us to equip the robot with any type of Weapon we can come up with.
"""


class Weapon(ABC):
    @abstractmethod
    def shoot(self):
        pass


@dataclass
class Laser(Weapon):
    damage: int

    def shoot(self):
        print(f"Laser causing {self.damage} damage")


@dataclass
class BFG(Weapon):
    damage: int

    def shoot(self):
        print(f"BFG causing {self.damage} damage")


laser = Laser(damage=20)
r2d2 = Robot(serial="r2d2", weapon=laser)
r2d2.weapon.shoot()

bfg = BFG(damage=20000)
r2d2 = Robot(serial="r2d2", weapon=bfg)
r2d2.weapon.shoot()

"""
The Robot no longer depends on a lower level module (Laser), but instead, it depends on
an abstraction (Weapon).

We can pass the robot any type of weapon we like as long as it satisfies the interface.
"""
