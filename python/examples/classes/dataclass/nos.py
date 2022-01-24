"""
Start by importing it:

from dataclasses import dataclass


There is no __init__, dataclass takes care of that for us.


When using 'field':
    field(default_factory=list) will construct a new list as a default arg

    a default_factory also allows you to use a function that generates the default value for you

    you can pass init=False to restrict users from setting the attribute value


Dataclass decorator options:
 - frozen=True: turn the dataclass into a CONSTANT    
"""
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid

from numpy import vectorize


class Os(Enum):
    JUNOS = auto()
    EOS = auto()


@dataclass
class Interface:
    description: str


@dataclass
class Router:
    hostname: str
    vendor: Os
    interfaces: list[Interface] = field(default_factory=list)

    def __post_init__(self):
        if self.vendor == Os.JUNOS:
            print("We created a Junos router, doing something during construction!")

    @property
    def role(self):
        return self.hostname.split(".")[0]


if __name__ == "__main__":
    print("yolo")
    r1 = Router(hostname="cr.sjc.01", vendor=Os.JUNOS)
    print(r1)
    print("role", r1.role)
