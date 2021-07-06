from ctypes import *
from ctypes import cdll
import time


class go_string(Structure):
    _fields_ = [("p", c_char_p), ("n", c_int)]


lib = cdll.LoadLibrary("./main.so")


def bar(str):
    b = go_string(c_char_p(str), len(str))
    lib.bar.restype = c_char_p
    a = lib.bar(b, c_char_p(str))
    print(a)


bar("haha")
bar("hoho")
time.sleep(100)