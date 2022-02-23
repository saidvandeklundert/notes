"""
Multiple constructors can come in handy when you need to create
 instances using different types of arguments / sources of data.


# multiple constructors 1: optional init arguments
# multiple constructors 2: check the input argument type
# multiple constructors 3: using a class method:
# multiple constructors 4:  @singledispatch or @singledispatchmethod:



__init__: class instance initializer

 object.__new__(cls[, ...]): static method, called to create a new instance of class cls.

object.__call__(self[, args...]): turns an instance of the class into a function and let's you
    specify what the function does.
"""

# regular class with 1 init method
from typing import Optional, Union
from dataclasses import dataclass
import yaml


class Human:
    def __init__(self, name, age):
        """Regular instance initializer."""
        self.name = name
        self.age = age


# multiple constructors 1: optional init arguments


class Point:
    def __init__(self, x, y=0):
        self.y = y
        self.x = x

    def __call__(
        self,
    ):
        print(f"running call {self.x} {self.y}")


point_1 = Point(x=1, y=1)
point_2 = Point(1)

# multiple constructors 2: check the input argument type:


@dataclass
class NetworkDeviceBuilder:
    hostname: str
    os: str


class NetworkDevice:
    def __init__(
        self, host: Union[str, NetworkDeviceBuilder], os: Optional[str] = None
    ):
        if isinstance(host, str):
            """Constructor 1"""
            self.hostname = host
            self.os = os
        elif isinstance(host, NetworkDeviceBuilder):
            """Constructor 2"""
            self.hostname = host.hostname
            self.os = host.os
        else:
            raise RuntimeError(f"unsupported format for host: {type(host)}.")

    def __repr__(self):
        return f"{self.hostname} {self.os}"


dev_1 = NetworkDevice("R1", "Junos")
dev_2_arg = NetworkDeviceBuilder(hostname="R2", os="eos")
dev_2 = NetworkDevice(dev_2_arg)
print(dev_1, dev_2)

# multiple constructors 3: using a class method:

yaml_s = """
name: John
age: 30
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_yaml(cls, yaml_s):
        kwarg = yaml.safe_load(yaml_s)
        return Person(**kwarg)

    @classmethod
    def from_excell(cls, excell):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.name} {self.age}"


person_1 = Person(name="Jan", age=6)
person_2 = Person.from_yaml(yaml_s)
print(person_1, person_2)


# multiple constructors 4:  @singledispatch or @singledispatchmethod:
from functools import singledispatchmethod


@dataclass
class HumanBuilder_1:
    name: str
    age: int


@dataclass
class HumanBuilder_2:
    some_name: str
    some_age: int


class HumanBeing:
    @singledispatchmethod
    def __init__(self, human_builder):
        raise ValueError(f"unsupported formats: {human_builder}")

    @__init__.register(HumanBuilder_1)
    def _from_strings(self, human_builder):
        print("running init with HumanBuilder_1")
        self.name = human_builder.name
        self.age = human_builder.age

    @__init__.register(HumanBuilder_2)
    def _from_str_float(self, human_builder):
        print("running init with HumanBuilder_2")
        self.name = human_builder.some_name
        self.age = human_builder.some_age


builder_1 = HumanBuilder_1(name="jan", age=6)
human_being_1 = HumanBeing(builder_1)

builder_2 = HumanBuilder_2(some_name="marie", some_age=4)
human_being_2 = HumanBeing(builder_2)

builder_3 = {"some_name": "marie", "some_age": 4}
human_being_3 = HumanBeing(builder_3)
