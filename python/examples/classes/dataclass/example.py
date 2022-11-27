from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    occupation: str
    married: str


def get_person() -> Person:
    return Person(
        **{
            "name": "Ibrahim",
            "age": 29,
            "occupation": "network automation engineer",
            "married": "nope",
        }
    )
