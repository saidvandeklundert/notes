"""
Ensure the add.c is present and you are on a system that can run gcc.

Then compile the C programm:

gcc -c -fpic add.c
gcc -shared -o libadd1.so add.o

After having done this, you can execute the py_add.py script.

https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html#Link-Options
"""

import ctypes

add_lib = ctypes.CDLL("./libadd1.so")

"""
>>> type(add_lib)
<class 'ctypes.CDLL'>
"""
# To make add_one in Python (sort of) into the add_one C function:
add_one = add_lib.add_one

add_one.argtypes = [ctypes.POINTER(ctypes.c_int)]

# create C-style integer
x = ctypes.c_int()

add_one(ctypes.byref(x))
print(x)


c_lib = ctypes.CDLL("./libadd1.so")
x = c_lib.square(2)
print(x)