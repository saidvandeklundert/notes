from abc import ABC, abstractmethod
from dataclasses import dataclass


class Walker(ABC):
    """
    Bad interface that is too big.

    In this case, the movements interface does too many things.
    Not all animals can swim, walk and fly.
    """

    @abstractmethod
    def walk(self):
        pass


class WalkAndSwim(Walker):
    @abstractmethod
    def swim(self):
        pass


class WalkAndFlyAndSwim(Walker):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass


@dataclass
class Duck(WalkAndFlyAndSwim):
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
class Elephant(WalkAndSwim):
    """
    Elephants cannot fly!
    """

    name: str

    def swim(self):
        print(f"Elephant {self.name} taking a swim.")

    def walk(self):
        print(f"Elephant {self.name} taking a walk.")


if __name__ == "__main__":
    """
    NOTE:

    Cleaner because we do not have to implement unused methods on elephans.

    """
    donald = Duck(name="Donald")
    donald.fly()
    donald.walk()
    donald.swim()
    elephant = Elephant(name="Dumbo")
    elephant.swim()
    elephant.walk()
