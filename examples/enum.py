# https://docs.python.org/3/library/enum.html
#
# PEP 435: https://www.python.org/dev/peps/pep-0435/
#
# What is it good for? https://stackoverflow.com/questions/37601644/python-whats-the-enum-type-good-for
"""
ENUM is good for a number of reasons:
- communicate and pass values accross a large code bases in a precise way
- enforce immutability
- ensure naming and arguments to functions are the same everywhere
- as a result, less error checking is required inside functions. You already know that the enum is of a valid value.


Motivation: The properties of an enumeration are useful for defining an immutable, related set
 of constant values that may or may not have a semantic meaning.


"""
from enum import Enum


class Platform(str, Enum):
    IOS = "ios"
    IOSXR = "iosxr"
    NXOS = "nxos"
    EOS = "eos"
    JUNOS = "junos"


if __name__ == "__main__":
    for p in Platform:
        print(p)
        print(p.name)
    print(Platform.EOS.name)
    print(Platform.EOS.value)
    Platform.EOS.value = "new value"
"""
Platform.IOS
IOS
Platform.IOSXR
IOSXR
Platform.NXOS
NXOS
Platform.EOS
EOS
Platform.JUNOS
JUNOS
EOS
eos
Traceback (most recent call last):
  File "\examples\enum.py", line 35, in <module>
    Platform.EOS.value = "new value"
  File "\Python39\lib\types.py", line 182, in __set__
    raise AttributeError("can't set attribute")
AttributeError: can't set attribute
"""
