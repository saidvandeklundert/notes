from typing import Optional
from pydantic import BaseModel


class Suitcase(BaseModel):
    items: list


class Human(BaseModel):
    name: str
    age: int
    suitcase: Optional[Suitcase]


jan = Human(name="jan", age=6, suitcase=Suitcase(items=["comb", "toothbrush"]))
print(jan.json())

# construct model WITHOUT validating data:
input_d = {"name": "marie", "age": 2, "suitcase": {"items": ["comb", "toothbrush"]}}
marie = Human.construct(**input_d)
print(marie.json())

# construct model WITHOUT validating data can also go wrong:
input_d = {
    "name": ["marie", "oops"],
    "age": 2,
    "suitcase": {"items": ["comb", "toothbrush"]},
}
marie_err = Human.construct(**input_d)
print(marie_err.json())
