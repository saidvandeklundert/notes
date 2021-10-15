def add(a: int, b: int):
    return a + b


# simple listcomp:
x = [x for x in range(1, 101)]

# calling a function in the listcomp:
x = [add(x, 10) for x in range(1, 101)]

# if statements in the listcomp:
x = [add(x, 10) for x in range(1, 101) \
    if x > 10 and x < 15]
