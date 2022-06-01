from pydantic import BaseModel, ValidationError, validator

"""
Python has the concept of validators.

The 'regular' Pydantic checks the 'mechanical' value.

The validators allow you to put in semantic checks.

To use the validator:
- annotate a method with the validator decorator
- reference the field value you want to decorate
- put in place the logic and checks
- can use simple assertions or implement whatever python you can think of
"""


class InputValues(BaseModel):

    vlan: int

    @validator("vlan")
    def vlan_validator(cls, v):
        assert v >= 1, "invalid vlan number, number too low"
        assert v <= 4094, "invalid vlan number, number too high"
        return v


"""
>>> _2000 = InputValues(vlan=2000)
>>> 
>>> try:
...     _6000 = InputValues(vlan=6000)
... except ValidationError as e:
...     print(e)
... 
1 validation error for InputValues
vlan
  invalid vlan number, number too high (type=assertion_error)
>>>
"""


# For simple things, there are also some config options:
class SomeModel(BaseModel):
    v: str

    class Config:
        max_anystr_length = 5


one = SomeModel(v="one")
thirtyfive = SomeModel(v="thirtyfive")
"""
>>> one = SomeModel(v="one")
>>> thirtyfive = SomeModel(v="thirtyfive")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pydantic\main.py", line 331, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for SomeModel
v
  ensure this value has at most 5 characters (type=value_error.any_str.max_length; limit_value=5)
"""


# We can also validate fields based on the values assigned to other fields.
#
from pydantic import BaseModel, ValidationError, validator


class Person(BaseModel):
    name: str
    age: int
    drivers_licens: bool

    @validator("drivers_licens")
    def drivers_license_age(cls, v, values):
        if "drivers_licens" and values["age"] < 18:
            raise ValueError("Drivers license before the age of 18")
        return v


try:
    Person(
        name="Jan",
        age=6,
        drivers_licens=True,
    )
except ValidationError as e:
    print(e)
"""
>>> try:
...     Person(
...         name="Jan",
...         age=6,
...         drivers_licens=True,
...     )
... except ValidationError as e:
...     print(e)
... 
1 validation error for Person
drivers_licens
  Drivers license before the age of 18 (type=value_error)
"""
