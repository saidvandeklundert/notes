from pydantic import BaseModel
from pydantic import ValidationError


class Human(BaseModel):
    name: str
    age: int


jan = Human(name="jan", age=6)
marie = Human(name="marie", age="3")  # coerced into integer
print(type(marie.age))

# using incorrect type:
try:
    henk = Human(name="henk", age=[False])
except ValidationError as e:
    print(
        "Because we speficied the age to be of type int, \
         we get the following error"
    )
    print(e.json())

# setting non-existing field:
try:
    marie.yolo = False
except ValueError as er:
    print(
        "The 'yolo' field does not exist \
        and setting it give the following error:"
    )
    print(er)
