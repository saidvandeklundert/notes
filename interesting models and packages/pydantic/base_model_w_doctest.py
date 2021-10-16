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
    print(
        """ To run the doctests:
python -m doctest -v .\base_model_w_doctest.py
Trying:
    from yaml_doctest_input import *
Expecting nothing
ok
Trying:
    d = safe_load(YAML_EXAMPLE)
Expecting nothing
ok
Trying:
    p = Person(**d)
Expecting nothing
ok
Trying:
    assert p.name == "Jan"
Expecting nothing
ok
2 items had no tests:
    base_model_w_doctest
    base_model_w_doctest.Person.__config__
1 items passed all tests:
   4 tests in base_model_w_doctest.Person
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
"""
    )
