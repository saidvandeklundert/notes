from pydantic import BaseModel, Field
import yaml

"""
Other APIs might give you wierd field names or CamelCaseNames.

Or even worse, field names that conflict with Python, like 'id'.

"""


class Item(BaseModel):
    item_id: str = Field(alias="id")
    is_available: bool = Field(alias="isAvailable")  # 1


yaml_string = """
---
id: "peanut"
isAvailable: True 
"""
item = Item(**yaml.safe_load(yaml_string))
"""
>>> item
Item(item_id='peanut', is_available=True)
"""
