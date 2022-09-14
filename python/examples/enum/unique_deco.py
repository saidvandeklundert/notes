from enum import Enum, auto, unique

# unique is a class decorator for Enum that raises a ValueError if there are any duplicate enumeration values.


@unique
class MgmtPrefix(Enum):
    infra = auto()  # will be assigned value 1
    tor = auto()
    something = 1


"""
Running this results in:
>>> ValueError: duplicate values found in <enum 'MgmtPrefix'>: something -> infra
"""
