from pydantic import BaseModel
from pydantic import ValidationError

"""
Models have configuration options.

https://pydantic-docs.helpmanual.io/usage/model_config/

There are many, many configuration options here:
- run validation when fields are changed
- check max string length
- allow, ignore or forbid extra fields during initialization
- make the type immutable
- use the ENUM values by default

Exploring the 'validate_assignment' configuration option here.
"""

# Normally we can re-assign fields:
class Human(BaseModel):
    name: str
    age: int


"""
>>> marie = Human(name="marie", age=3)
>>> print(marie.json())
{"name": "marie", "age": 3}
>>> marie.age = []
>>> marie.json()
'{"name": "marie", "age": []}'
>>>
"""
# The 'age' field is not type-checked when value is re-assigned!!


# Let's change the config:


class HumanNG(BaseModel):
    name: str
    age: int

    class Config:
        validate_assignment = True


jan = HumanNG(name="jan", age=6)
# Everything is still normal here:
"""
>>> print(jan.json())
{"name": "jan", "age": 6}
"""
try:
    jan.age = []
    print(jan.json())
except ValidationError as e:
    print(e.json())

"""
>>> try:
...     jan.age = []
...     print(jan.json())
... except ValidationError as e:
...     print(e.json())
... 
[
  {
    "loc": [
      "age"
    ],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
"""
# Due to config option 'validate_assignment', pydantic will
# validate the type for attributes when they
# are re-assigned as well!!
