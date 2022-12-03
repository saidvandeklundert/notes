# python -m mypy .\00_basic.py
from typing import List, Union

some_items = ["str", False, "another str"]

# the naive approach:


def transform(items):
    transformed_items = []
    for item in items:
        transformed_items.append(item.upper())

    return transformed_items


result = transform(some_items)


# getting help from type hints:

some_items_annotated: List[Union[str, bool]] = ["str", False, "another str"]


def transform_annotated(items: List[str]) -> List[Union[str, bool]]:
    transformed_items = []
    for item in items:
        transformed_items.append(item.upper())

    return transformed_items


result_typed = transform_annotated(some_items_annotated)


# type hints are telling you the argument is not correct.


# a bit better:


def transform_annotated_a_bit_better(
    items: List[Union[str, bool]]
) -> List[Union[str, bool]]:
    transformed_items = []
    for item in items:
        transformed_items.append(item.upper())

    return transformed_items


result_typed = transform_annotated_a_bit_better(some_items_annotated)

# type hints is telling you the function can fail since you are not
#  dealing with the types correctly.

# thank you type hints!:


def transform_correct(items: List[Union[str, bool]]) -> List[Union[str, bool]]:
    transformed_items = []
    for item in items:
        if isinstance(item, str):
            transformed_items.append(item.upper())
        transformed_items.append(item)
    return transformed_items


result_typed = transform_annotated_a_bit_better(some_items_annotated)


# this is a lot more robust and mypy can check it for free during CI.
