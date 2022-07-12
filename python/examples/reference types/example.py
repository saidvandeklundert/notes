# list
x = [1, 2, 3]
y = x
id(x)
# 140150413486976
id(y)
# 140150413486976
id(x[0])
# 140150440708000
id(y[0])
x is y
another_list = ["a", "b", {"a": "a", "b": "b"}]
x.append(another_list)
y
# [1, 2323, 3, ['a', 'b', {'a': 'a', 'b': 'b'}]]
import copy

shallow_copy = copy.copy(y)  # or shallow_copy = list(y)
shallow_copy is x
# False
shallow_copy[0] = 10_000
shallow_copy
# [10000, 2323, 3, ['a', 'b', {'a': 'a', 'b': 'b'}]]
x
# [1, 2323, 3, ['a', 'b', {'a': 'a', 'b': 'b'}]]
shallow_copy[3][0] = "AAAAAAA"

shallow_copy
# [10000, 2323, 3, ['AAAAAAA', 'b', {'a': 'a', 'b': 'b'}]]
x
# [1, 2323, 3, ['AAAAAAA', 'b', {'a': 'a', 'b': 'b'}]]

deep_copy = copy.deepcopy(shallow_copy)
deep_copy[3][0] = "BBBBBBBBBBBBBBB"
deep_copy
# [10000, 2323, 3, ['BBBBBBBBBBBBBBB', 'b', {'a': 'a', 'b': 'b'}]]
shallow_copy
# [10000, 2323, 3, ['AAAAAAA', 'b', {'a': 'a', 'b': 'b'}]]


# dict

dict_a = {"a": 1, "b": 2}
dict_b = dict_a


# tuple
tuple_a = (1, 2, 3)
tuple_b = tuple_a

# data class
from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int


jan = Human(name="Jan", age=6)
another_jan = copy.copy(jan)
id(jan)
id(another_jan)
