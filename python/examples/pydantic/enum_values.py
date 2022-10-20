from pydantic import BaseModel
from enum import Enum


class AttributeType(Enum):
    S = "S"  # string
    N = "N"  # number
    B = "B"  # binary


class AttributeBase(BaseModel):
    attribute_name: str
    attribute_type: AttributeType


"""
To ensure dict representation of class
 will show the enum value instead of the enum:
"""


class Attribute(BaseModel):
    attribute_name: str
    attribute_type: AttributeType

    class Config:
        use_enum_values = True


attr_base = AttributeBase(attribute_name="some_name", attribute_type=AttributeType.B)
attr = Attribute(attribute_name="some_name", attribute_type=AttributeType.B)

print(attr_base.dict())
print(attr.dict())
