from dataclasses import dataclass, field
from typing import List
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))


# make it immutable and kw arg only and using slots
@dataclass(frozen=False, kw_only=True, slots=True)
class Human:
    name: str
    email: str
    children: List[str]
    needy: bool = False
    # The following ensures that every instance has it's own list
    rucksack: List[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    # here we set init to False, meaning no one can override it at init:
    auto_id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)  # no init and no __repr__

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.email}"  # runs after the initializer

    def __iter__(self):
        return iter(self.children)


if __name__ == "__main__":
    dude = Human(
        name="Joe",
        email="joe@joe.com",
        children=["Marie", "Shasha", "Gosh"],
        id="po",
    )
    print(dude)
    for kid in dude:
        print(kid)
