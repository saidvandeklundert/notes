from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int


@dataclass
class HumanWithPersonality(Human):
    personality: str


if __name__ == "__main__":
    jan = Human(name="Jan", age=6)
    print(vars(jan))
    marie = HumanWithPersonality(name="Marie", age=4, personality="sweet")
    print(vars(marie))
