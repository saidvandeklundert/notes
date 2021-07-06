from ctypes import *
from ctypes import cdll
import time


go_lib = cdll.LoadLibrary("./main.so")
free = go_lib.free


def goprint(s: str):
    go_lib.goPrint.restype = c_char_p
    a = go_lib.goPrint(s.encode("utf-8"))
    print(a)
    return a


start = time.time()
for x in range(100):
    goprint(str(x))

end = time.time()
print(end - start)
