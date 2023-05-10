def multiply(x: int, y: int) -> int:
    return x * y


def add(x, y):
    return x + y


GROUP = (multiply, add)

for f in GROUP:
    print(f(2, 10))
