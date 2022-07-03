from dataclasses import dataclass
from enum import Enum


class Profession(str, Enum):
    TAXIDRIVER = "taxidriver"
    TRUCKDRIVER = "truckdriver"


@dataclass
class Human:
    name: str
    profession: str

    def says_hi(self) -> None:
        print(f"Hi, I am {self.name} and I am a {self.profession}")

    def dictify(self):
        return vars(self)


if __name__ == "__main__":
    jan = Human(name="Jan", profession=Profession.TAXIDRIVER)
    jan.says_hi()
