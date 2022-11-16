from dataclasses import dataclass
from typing import Callable


@dataclass
class Person:
    name: str
    age: int


persons = [
    Person("Jan", 7),
    Person("Marie", 4),
    Person("Said", 38),
    Person("Anne", 38),
]


def interesting_persons(person: Person) -> bool:
    return person.age < 30


def send_email_promotion(
    persons: list[Person], selector: Callable[[Person], bool]
) -> None:
    for person in persons:
        if selector(person):
            print(f"{person.name} is eligable")
        else:
            print(f"{person.name} is NOT eligable")


if __name__ == "__main__":
    send_email_promotion(persons=persons, selector=interesting_persons)
    # same but now with a lambda:
    send_email_promotion(persons=persons, selector=lambda customer: customer.age < 30)
