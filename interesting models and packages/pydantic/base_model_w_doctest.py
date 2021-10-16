#  python -m doctest -v .\base_model_w_doctest.py
from pydantic import BaseModel
from yaml import safe_load


class Person(BaseModel):
    """Person basemodel
    >>> from yaml_doctest_input import *
    >>> d = safe_load(YAML_EXAMPLE)
    >>> p = Person(**d)
    >>> assert p.name == "Jan"
    """

    name: str
    age: int


if __name__ == "__main__":
    print("MAIN")
    d = safe_load(
        """
---
name: Jan
age: 6    
"""
    )
    p = Person(**d)
    print(p.json(indent=2))
