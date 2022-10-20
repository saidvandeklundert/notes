from pydantic import BaseModel
from pydantic import ValidationError

"""
Python enforces type hints at run-time.

This offers greater precision. 


If the code ran, you know it ran with all the fields and types being correct.

Even with data coming from other sources (JSON files, API calls, etc.)

For certain corner cases, you can turn to: https://pydantic-docs.helpmanual.io/usage/types/#strict-types
"""


class Human(BaseModel):
    name: str
    age: int


# When we try using an incorrect type, we will get an error:
try:
    henk = Human(name="henk", age=[False])
except ValidationError as e:
    print(
        "Because we speficied the age to be of type int, \
we get the following error"
    )
    print(e.json())

"""
Because we speficied the age to be of type int, we get the following error
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
# Setting non-existing field:
anne = Human(name="anne", age=36)
try:
    anne.yolo = False
except ValueError as er:
    print(
        "The 'yolo' field does not exist \
and setting it give the following error:"
    )
    print(er)

"""
The 'yolo' field does not exist and setting it give the following error:
"Human" object has no field "yolo"
"""

# It is Python, so there are still some unexpected things.
#
# Things can be co-erced into the expected field type:
"""
>>> jan = Human(name="jan", age=6)
>>> marie = Human(name="marie", age="3")  # coerced into integer
>>> print(type(marie.age))
<class 'int'>
"""
#
# Booleans are actually just 0 and 1:
"""
>>> henk = Human(name="henk", age=False) 
>>> 
"""

# solve some corner cases with https://pydantic-docs.helpmanual.io/usage/types/#strict-types
from pydantic import StrictInt


class HumanStrict(BaseModel):
    name: str
    age: StrictInt


henk_strict = HumanStrict(name="henk", age=False)
"""
>>> pydantic.error_wrappers.ValidationError: 1 validation error for HumanStrict
age
  value is not a valid integer (type=type_error.integer)
"""
