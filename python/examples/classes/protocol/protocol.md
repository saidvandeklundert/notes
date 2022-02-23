A protocol is like a Rust trait or Go interface.

Before 3.8, you could do something similar with ABCs. However, in that case, you had to inherit the abstract base class.

ABC: for nominal typing. If you want a typing relation to be there, you write it down explicitly using inheritence.

Protocols is used for structural typing: instead of stating it explicitly, Python examines the structure of the objects. If they have the same methods/properties, then it is assumed that the types match. There is no inheritence with protocols. Rather, an interface is specified.


With a protocol, you can just specify an interface that something should adhere to and then, in other functions and methods, declare that the argument to that function/method should implement that protocol.


```python
from typing import Protocol
from dataclasses import dataclass


class Speaker(Protocol):
    def say_hi(self) -> str:
        ...


@dataclass
class Human:
    name: str
    age: int

    def say_hi(self) -> str:
        return "Hi, how are you?"
        

def greet(person: Speaker):
    greeting = person.say_hi()
    print(greeting)

```

Protocols PEP: https://www.python.org/dev/peps/pep-0544

From the mypy docs:
```
Structural subtyping can also be useful. Class D is a structural subtype of class C if the former has all attributes and methods of the latter, and with compatible types.

Structural subtyping can be seen as a static equivalent of duck typing, which is well known to Python programmers. Mypy provides support for structural subtyping via protocol classes described below. See PEP 544 for the detailed specification of protocols and structural subtyping in Python.
```

