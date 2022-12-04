from pydantic import BaseModel
from enum import Enum


class PROPERTY(Enum):
    nozem = "nozem"
    gabber = "gabber"
    skater = "skater"


class Human(BaseModel):
    """BGP peering model to define a single BGP session."""

    name: str
    property: PROPERTY

    class Config:
        allow_mutation = False
        use_enum_values = True


if __name__ == "__main__":
    x = Human(**{"name": "jan", "property": "nozem"})
    x = Human(**{"name": "jan", "property": "bag"})
