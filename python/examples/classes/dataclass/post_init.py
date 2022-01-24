from dataclasses import dataclass


@dataclass
class Human:
    name: str

    def __post_init__(self):
        print("running the __post_init__")
        self.name = self.name.upper()


marie = Human(name="marie")
print(marie.name)
