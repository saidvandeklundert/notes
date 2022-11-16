from abc import ABC, abstractmethod
from dataclasses import dataclass


class Movements(ABC):
    """
    Bad interface that is too big.

    In this case, the movements interface does too many things.
    Not all animals can swim, walk and fly.
    """

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass


@dataclass
class Duck(Movements):
    """
    Ducks can do a lot.
    """

    name: str

    def swim(self):
        print(f"Duck {self.name} taking a swim.")

    def walk(self):
        print(f"Duck {self.name} taking a walk.")

    def fly(self):
        print(f"Duck {self.name} taking a fly.")


@dataclass
class Elephant(Movements):
    """
    Elephants cannot fly!
    """

    name: str

    def swim(self):
        print(f"Elephant {self.name} taking a swim.")

    def walk(self):
        print(f"Elephant {self.name} taking a walk.")

    def fly(self):
        pass


if __name__ == "__main__":
    """
    NOTE:

    Not so clean because we 'pass' methods that we do not implement on the Elephant.

    """
    donald = Duck(name="Donald")
    donald.fly()
    donald.walk()
    donald.swim()
    elephant = Elephant(name="Dumbo")
    elephant.swim()
    elephant.walk()
