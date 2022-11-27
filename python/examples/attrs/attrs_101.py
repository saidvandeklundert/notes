"""
https://hynek.me/articles/import-attrs/
"""
from attrs import asdict, define, make_class, Factory


@define
class Human:
    name: str
    age: int


if __name__ == "__main__":
    jan = Human(name="Jan", age=7)
