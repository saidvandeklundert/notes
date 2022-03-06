from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int

if __name__ == "__main__":
    jan = Human(name="Jan", age=6)
    marie = Human(name=3, age="Marie")
    print(jan)
    print(marie)