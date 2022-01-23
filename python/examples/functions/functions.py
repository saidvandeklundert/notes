"""
A closure is a function along with an environment containing
 all of the variables needed to execute the functions body.


Functions have attributes. 
 In https://docs.python.org/3/reference/datamodel.html look for 'User-defined functions'
"""


def basic(a):
    """Print the value of a."""
    print(a)


# force users to supply keyword arguments
def two_args(arg1, arg2):
    print(f"arg1 {arg1} arg2 {arg2}")


def force_keyword_arg_invocation(*, arg1, arg2):
    print(f"arg1 {arg1} arg2 {arg2}")


def deny_keyword_arg_invocation(arg1, arg2, /):
    print(f"arg1 {arg1} arg2 {arg2}")


two_args(1, 2)
force_keyword_arg_invocation(arg1=1, arg2=2)
try:
    force_keyword_arg_invocation(1, 2)  # type: ignore
except TypeError as error:
    print(error)

try:
    deny_keyword_arg_invocation(arg1=1, arg2=2)
except TypeError as error:
    print(error)

# retrieving the function name:
print(f"{basic.__name__} is the name of this function")
print(
    f"- {basic.__doc__} - is the docstring associated with the function named {basic.__name__}"
)

# lambda args : expression
a = lambda x, y: x * y
print(a(2, 3))

# Partial
from functools import partial, wraps


def multiply(x, y):
    return x * y


# use the following to re-use the multiply function to create
#  a function that always multiplies a value by 2
doubling = partial(multiply, 2)
print(doubling(4))

from functools import wraps

# wraps will maintain the wrapped functions docstring and name
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        return f(*args, **kwargs)

    return wrapper


@my_decorator
def wrapped():
    """Wrapped doctstring"""
    print("wrapped")


wrapped()

# you can use map to apply a function to all elements of a sequence


def square(x):
    return x * x


print(list(map(square, [1, 2, 3, 4])))

# but you might as well use listcomps or genexps:
lc = [x * x for x in [1, 2, 3, 4]]
gc = (x * x for x in [1, 2, 3, 4])
print(lc)
for i in gc:
    print(i)

#
import inspect


def some_func(a: str) -> str:
    """
    This is a docstring
    """
    import sys

    b = a + "b"
    print(inspect.currentframe())
    f_locals: dict = inspect.currentframe().f_locals  # type: ignore
    print(f"function locals {f_locals}")
    print(f"syg.getframe: {sys._getframe()}")
    return b


sig = inspect.signature(some_func)
print(sig)
some_func("a")

# interesting debug method:
import inspect
from collections import ChainMap


def debug_inside_function(*varnames):
    print("debug_inside_function")
    f = inspect.currentframe().f_back
    vars = ChainMap(f.f_locals, f.f_globals)
    print(f"{f.f_code.co_filename}:{f.f_lineno}")
    for name in varnames:
        print(f"    {name} = {vars[name]!r}")


def demonstration_func(a, b, c):
    debug_inside_function(
        a,
        b,
        c,
    )

    print("fin")


demonstration_func("a", "b", "c")
