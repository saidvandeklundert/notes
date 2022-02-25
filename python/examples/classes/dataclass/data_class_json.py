"""
@dataclass_json decorator must be stacked above the @dataclass decorator


We get:
- from_json()
- to_json()
- from_dict()
- to_dict()


https://github.com/lidatong/dataclasses-json
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Human:
    name: str
    age: int


if __name__ == "__main__":
    jan = Human(name="Jan", age=6)
    print(jan)
    print(jan.to_json())
