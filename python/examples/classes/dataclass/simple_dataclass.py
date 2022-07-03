from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int

    def says_hi(self) -> None:
        print(f"Hi, I am {self.name}")


if __name__ == "__main__":
    jan = Human(name="Jan", age=6)
    jan.says_hi()
