"""
Ensure the square.c is present and you are on a system that can run gcc.

Then compile the C programm:

gcc -shared -o square.so square.c

After having done this, you can execute the square.py script.

https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html#Link-Options
"""

import ctypes

c_lib = ctypes.CDLL("./square.so")

print(c_lib.square(2))

for i in range(10):
    x = c_lib.square(i)
    print(x)