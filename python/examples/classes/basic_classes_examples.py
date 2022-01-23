"""
Is it a thing? Then you can make that thing into a class. 
Otherwise, you can also consider a module with many functions.
--
If you are writing a lot of classes with 1 or 2 mtehods, consider using functions.

They are simpler and easier to test. Premature abstraction is often not a good thing.

Class method:
- use-case is for it to server as an alternate constructor
- A common naming convention for such methods is to include the word from_

Class attribute use-case:
- configuring the behavior of a class
- storing data that should be shared among all instances of a class


Basic strategies to consider (according to dabeaz): 
- writing classes with useful __repr__() methods
- preferring composition over inheritance
- allowing dependency injection

If you wish to have an even more private attribute, prefix the name with two leading underscores ( __ ).
All names such as __name are automatically renamed into a new name of the form _Classname__name.


Summary from dabeas
In the big picture, it's useful to step back and consider a few generally desirable code qualities.

First and foremost, readability counts for a lot—and it often suffers if you pile on too many layers of abstraction. 

Second, you should try to make code that is easy to observe and debug, and don't forget about using the REPL.

Finally, making code testable is often a good driver for good design. 
If your code can't be tested or testing is too awkward, there may be a better way to organize your solution.
"""
from typing import List


class Human:
    def __init__(self, friends):
        self.friends = friends

    def __iter__(self):
        return iter(self.friends)

    def __getitem__(self, index):
        return self.friends[index]

    def __len__(self):
        return len(self.friends)

    def __repr__(self):
        return f"{type(self).__name__}"


a = Human(["Joe", "Jill", "Jane"])

for friend in a:
    print(friend)

print(a[1])
print(len(a))
print(a)

# Creating a stack that INHERITS everything from list:
class Stack(list):
    def push(self, item):
        self.append(item)


my_stack = Stack([0, 1, 2, 3])
print(my_stack)
my_stack.push(4)
print(my_stack)

# Creating a stack USING a list. Instead of inheritence, composition is used:
class BetterStack:
    def __init__(self, a_list: List[int]):
        self.stack = a_list

    def push(self, item: int):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)


my_better_stack = BetterStack([0, 1, 2, 3])
print(my_better_stack)
my_better_stack.push(4)
print(my_better_stack)

# using property and setter:
class Troll:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value


daar = Troll("Daar")
try:
    two = Troll(2)
except TypeError as error:
    print(error)

try:
    daar.name = 2
except TypeError as error:
    print(error)

daar.name = "Raad"

# Super
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, I'm {self.name}")

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


class Developer(Person):
    def __init__(self, name, age, languages):
        super().__init__(name, age)
        self.languages = languages

    def __repr__(self) -> str:
        return f"Developer({self.name}, {self.age}, {self.languages})"

    def speak(self):
        self.talk()
        print(f"I am a developer and I know {self.languages}")


python_dev = Developer("James", 23, ["python"])
c_dev = Developer("Joe", 50, "C")