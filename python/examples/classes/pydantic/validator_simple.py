from pydantic import BaseModel, ValidationError, validator


class InputValues(BaseModel):
    """
    To use the validator:
    - annotate a method with the validator decorator
    - reference the field value you want to decorate
    - put in place the logic and checks
    - can use simple assertions or implement whatever
     python you can think of
    """

    vlan: int

    @validator("vlan")
    def vlan_validator(cls, v):
        assert v >= 1, "invalid vlan number, number too low"
        assert v <= 4094, "invalid vlan number, number too high"
        return v


_2000 = InputValues(vlan=2000)

try:
    _6000 = InputValues(vlan=6000)
except ValidationError as e:
    print(e)
    """
    1 validation error for InputValues
    vlan
    invalid vlan number, number too high (type=assertion_error)
    """
