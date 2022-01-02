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
    force_keyword_arg_invocation(1, 2)
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
from functools import partial


def multiply(x, y):
    return x * y


# use the following to re-use the multiply function to create
#  a function that always multiplies a value by 2
doubling = partial(multiply, 2)
print(doubling(4))