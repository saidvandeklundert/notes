from ctypes import *
from ctypes import cdll
import time


lib = cdll.LoadLibrary("./main.so")


def bar(s: str):
    lib.bar.restype = c_char_p
    a = lib.bar(s)
    print(a)
    return a


start = time.time()
for x in range(100):
    bar(str(x))
end = time.time()
print(end - start)
