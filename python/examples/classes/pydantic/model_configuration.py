"""
Also interesting:

https://pydantic-docs.helpmanual.io/usage/types/#strict-types
"""

from pydantic import BaseModel
from pydantic import ValidationError

# we can re-assign fields:
class Human(BaseModel):
    name: str
    age: int


marie = Human(name="marie", age=3)
print(marie.json())
marie.age = []
print("\n\nField is not type-checked when value is re-assigned!!\n\n", marie.json())


class HumanNG(BaseModel):
    name: str
    age: int

    class Config:
        validate_assignment = True


jan = HumanNG(name="jan", age=6)
print(jan.json())
try:
    jan.age = []
    print(jan.json())
except ValidationError as e:

    """
    Due to config option 'validate_assignment',
    pydantic will validate the type for attributes when
    they are re-assigned as well!!
    """

    print(e.json())
