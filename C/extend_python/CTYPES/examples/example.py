from sys import getsizeof
from ctypes import *


class POINT(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


c_point = POINT(10, 20)
point = Point(10, 20)
point_slots = PointSlots(10, 20)

print("c_point: ", getsizeof(c_point))
print("point: ", getsizeof(point), "point vars: ", getsizeof(vars(point)))
print("point_slots: ", getsizeof(point_slots))
