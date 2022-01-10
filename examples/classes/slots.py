"""

The use of __slots__ can offer 2 improvements:
- faster attribute access
- less memory usage

https://stackoverflow.com/questions/472000/usage-of-slots


https://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html
"""
from sys import getsizeof
import timeit


class Human:
    def __init__(self, name, age, job, email):
        self.name = name
        self.age = age
        self.job = job
        self.email = email


class HumanSlots:
    __slots__ = ("name", "age", "job", "email")

    def __init__(self, name, age, job, email):
        self.name = name
        self.age = age
        self.job = job
        self.email = email


instance_of_jan = {"name": "jan", "age": "6", "job": "student", "email": "jan@jan"}
jan = Human(**instance_of_jan)
jan_slots = HumanSlots(**instance_of_jan)
print(getsizeof(jan.__dict__))
print(getsizeof(jan_slots))

total = [Human(**instance_of_jan) for x in range(1000)]
total_slots = [HumanSlots(**instance_of_jan) for x in range(1000)]

print(getsizeof(total))
print(getsizeof(total_slots))
test_code_1 = """
class Human:

    def __init__(self, name, age, job, email):
        self.name = name
        self.age = age
        self.job = job
        self.email = email
instance_of_jan = {"name": "jan", "age": "6", "job": "student", "email": "jan@jan"}
jan = Human(**instance_of_jan)
"""
print(timeit.timeit(test_code_1, number=100000))
test_code_2 = """
class Human:
    __slots__ = ("name", "age", "job", "email")

    def __init__(self, name, age, job, email):
        self.name = name
        self.age = age
        self.job = job
        self.email = email
instance_of_jan = {"name": "jan", "age": "6", "job": "student", "email": "jan@jan"}
jan = Human(**instance_of_jan)
"""
print(timeit.timeit(test_code_2, number=100000))


##


##