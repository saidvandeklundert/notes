
Python type checkers:
- mypy:

- pytype:
Google's pytype also infers by analyzing untyped code flows.

- Pyright / Pylance:

Microsoft's Pyright can infer and check typed code. Is part of the pylance extension for Vscode. 

- pyre

Facebook's pyre is a type checker (Pyre) and a static code analysis tool (Pysa).

## Example type checker:

https://github.com/google/pytype

```
! install pytype:
pip install pytype
! generate example config:
pytype --generate-config pytype.cfg

! alter it in the way you like


```


## Basic example:

```python
def add(i: int) -> int:
    x = 2 + i
    return x


add(3)
add("2")
```

Mypy result:
```
scratchpad.py:7: error: Argument 1 to "add" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## Multiple arguments and multiple returns

```python
from typing import Tuple


def parse(d: dict, l: list) -> Tuple[bool, str]:
    l.append(d)
    x = False
    y = "string"
    return x, y
```

Mypy result:
```
Success: no issues found in 1 source file
```


Let's add some errors to the previous:
```python
parse("s", 1092)
a, b = parse(
    {
        "a": 1,
    },
    [0, 1, 2],
)
y = "a" + a
```

Now mypy returns the following:
```
scratchpad.py:11: error: Argument 1 to "parse" has incompatible type "str"; expected "Dict[Any, Any]"
scratchpad.py:11: error: Argument 2 to "parse" has incompatible type "int"; expected "List[Any]"
scratchpad.py:18: error: Unsupported operand types for + ("str" and "bool")
Found 3 errors in 1 file (checked 1 source file)
```

From pycon:
[Talk: Dustin Ingram - Static Typing in Python](https://www.youtube.com/watch?v=ST33zDM9vOE)
[TALK / Maggie Moss / Gradual Typing in Practice](https://youtu.be/Lj_9TyT3V98)
