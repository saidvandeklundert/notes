from enum import Enum, IntEnum

from pydantic import BaseModel, ValidationError


class Model(str, Enum):
    x = "x"
    y = "y"
    z = "z"


class TireWidth(IntEnum):
    thin = 225
    normal = 245
    wide = 265


class Car(BaseModel):
    model: Model = Model.y
    tire_width: TireWidth = TireWidth.normal


print(Car())
"""
>>> model=<Model.y: 'y'> tire_width=<TireWidth.normal: 245>
"""
print(Car(model="x", tire_width=245))
"""
>>> model=<Model.x: 'x'> tire_width=<TireWidth.normal: 245>
"""
try:
    Car(model="a")
except ValidationError as e:
    print(e)
    """
    1 validation error for Car
    model
        value is not a valid enumeration member; 
        permitted: 'x', 'y', 'z' (type=type_error.enum; enum_values=[<Model.x: 'x'>, <Model.y: 'y'>, <Model.z: 'z'>])
    """
