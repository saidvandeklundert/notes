"""
You can turn percentages around

8% of 25 is the same as 25% of 8

Every piece of data in a program is an object.

Every object has:
- an identity (location in memory)
- a type ( aka class, for instance <class 'str'>)
- a value ( for isntance "string")

An object that has been created is called an instance.

If the instance can be changed, it is called a mutable object.

If the instance contains references to other objects, it is said to be a container.


Special or magic methods are associated with different categories of
 core interpretor features. These categories are sometimes called 'protocols'.

Objects may define a combintations of these features 
 to make an object behave in a certain way.

Some method:
__new__ : static method to create a new class
__init__: to initialize a new instance after it has been created
__del__: called when an instance is being destroyed
__repr__: create a string representation of an instance.
  The convention is for repr to return a string that is valid Python code that can be fed to eval()
"""

# id() will get you the object's identity:
x = 10000
print(id(x))

# type() will return the object's type:
print(type(x))

# the type of an object itself is also an object, known as class:
print(type(int))
print(id(int))

# python manages objects through automatic garbage collection
# all objects are reference-counted
# when the reference count of an object reaches zero, the object is deleted
import sys

print(sys.getrefcount(x))
l = [x]
print(sys.getrefcount(x))
l2 = [x]
print(id(l2[0]))
print(sys.getrefcount(x))

# objects can be deleted using the del statement:
del x
print(l2)
print(id(l2[0]))


from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int


jan = Human("Jan", 6)
print(type(jan))
print(repr(jan))
print(f"{jan}")
print(f"{jan!r}")

# None is implemented as a singletone in Python:
a = None
b = None
print(id(a), id(b), a is b)
