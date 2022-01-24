A protocol is like a Rust trait or Go interface.

Before 3.8, you could do something similar with ABCs. However, in that case, you had to inherit the abstract base class.

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

    def say_hi(
        self,
    ) -> str:
        return "Hi, how are you?"

def greet(person: Speaker):
    greeting = person.say_hi()
    print(greeting)

```