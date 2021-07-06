from ctypes import *
from ctypes import cdll
import time


lib = cdll.LoadLibrary("./main.so")


def bar(s: str):
    lib.bar.restype = c_char_p
    a = lib.bar(s)
    print(a)


bar("haha")
bar("hoho")
time.sleep(100)