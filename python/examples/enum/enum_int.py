from enum import Enum, IntEnum


class Size(int, Enum):
    S = 1
    M = 2
    L = 3
    XL = 4


class AltSize(IntEnum):
    S = 1
    M = 2
    L = 3
    XL = 4


Size.S > Size.M
# False
Size.S < Size.M
# True
Size.L >= Size.M
# True
Size.L <= Size.M
# False
