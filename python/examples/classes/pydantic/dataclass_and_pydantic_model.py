from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Human:
    name: str
    age: int


class Humandantic(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    anita = Human(name="Anita", age=[0])
    human_1_1 = Human(name="Jan", age=6)
    human_1_1.age

    human_1_2 = Humandantic(name="Jan", age=6)
    try:
        human_2_1 = Human(name="Jan", age="Six")

        human_2_2 = Humandantic(name="Jan", age="six")
    except Exception as err:
        print(err)
