from pydantic import BaseModel

"""
We can outfit models with methods like any other (data)-class:
"""


class Human(BaseModel):
    name: str
    age: int

    def greet(self):
        print(f"Hi, I am {self.name}")


jan = Human(name="jan", age=6)
jan.greet()
"""
>>> Hi, I am jan
"""
