from typing import Tuple


def parse(d: dict, l: list) -> Tuple[bool, str]:
    l.append(d)
    x = False
    y = "string"
    return x, y


class Person:
    def __init__(
        self,
        attribute_1,
        attribute_2,
    ):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2

    def multiples(self):
        return self.attribute_1 * self.attribute_2


dave = Person("Dave", 16)


def printPerson(p: Person):
    print(p.multiples())


printPerson("dave")
printPerson(dave)
parse("s", 1092)
a, b = parse(
    {
        "a": 1,
    },
    [0, 1, 2],
)
y = "a" + a

"""



def add(i: int) -> int:
    x = 2 + i
    return x


add(3)
add("2")

"""