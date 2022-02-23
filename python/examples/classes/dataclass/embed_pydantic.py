from pydantic import BaseModel
from typing import List, Union


class Child_1(BaseModel):
    a: int


class Child_2(BaseModel):
    b: str


class Child_3(BaseModel):
    c: List[int]


class Parent(BaseModel):
    name: str
    embedded: Union[Child_1, Child_2, Child_3]


instance_1 = Parent(**{"name": "Dave", "embedded": {"a": 1}})
instance_2 = Parent(**{"name": "Dave", "embedded": {"b": "STRING"}})
instance_3 = Parent(**{"name": "Dave", "embedded": {"c": [1, 2, 3]}})
print(instance_1.json())
print(type(instance_1.embedded))
print(instance_2.json())
print(type(instance_2.embedded))
print(instance_3.json())
print(type(instance_3.embedded))
