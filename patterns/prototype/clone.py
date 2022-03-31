from __future__ import annotations
from dataclasses import dataclass
import copy


@dataclass
class Human:
    name: str
    age: int

    def clone(self) -> Human:
        return Human(**vars(self))

    def clone_alt(self) -> Human:
        return copy.copy(self)


if __name__ == "__main__":
    john = Human(name="John", age=20)
    john_clone = john.clone()
    print(id(john), id(john_clone))
