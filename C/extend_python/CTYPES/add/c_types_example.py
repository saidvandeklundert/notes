"""
Ensure the add.c is present and you are on a system that can run gcc.

Then compile the C programm:

gcc -c -fpic square.c
gcc -shared -o clib.so square.c

After having done this, you can execute the py_add.py script.

https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html#Link-Options
"""

import ctypes

c_lib = ctypes.CDLL("./clib.so")
x = c_lib.square(40)
print(x)