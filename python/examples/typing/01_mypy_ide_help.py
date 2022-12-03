# python -m mypy .\01_mypy_ide_help.py
from typing import List, Union

string: str = "string value"
integer: int = 1


list_of_stuff: List[Union[str, bool]] = [False, True, "string"]

# Pylance/ IDE language assistence:

# types are checked and calls to non-existent methods are flagged:
string.upper()
integer.upper()

# also works on 'complicated' things like Unions. Here,
# the IDE can force you to put a proper place in check:
for item in list_of_stuff:
    item.upper()

for item in list_of_stuff:
    if isinstance(item, str):
        item.upper()
