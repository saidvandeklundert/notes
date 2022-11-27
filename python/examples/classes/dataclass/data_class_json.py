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
    jan
    jan.to_json()
    jan.to_dict()
    # Can also construct from dict, excess fields are ignored:
    marie = Human.from_dict({"name": "marie", "age": 4, "child": True})
