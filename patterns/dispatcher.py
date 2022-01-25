# example 1:


def dispatch(a: object):
    if isinstance(a, str):
        return "we run the string procedure"
    elif isinstance(a, (int | float)):
        return "we run the numbers procedure"
    elif isinstance(a, (dict | list)):
        return "we do something else"
    return NotImplemented


print(dispatch(1))
print(dispatch("1"))
print(dispatch((1, 2)))
