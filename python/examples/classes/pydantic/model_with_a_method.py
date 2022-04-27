from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int

    def greet(self):
        print(f"Hi, I am {self.name}")


jan = Human(name="jan", age=6)
jan.greet()
