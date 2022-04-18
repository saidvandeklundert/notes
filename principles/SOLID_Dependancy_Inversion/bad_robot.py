"""
Ensure that high-level modules do not depend on low level modules, but instead depend on abstractions.
"""
from dataclasses import dataclass


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
