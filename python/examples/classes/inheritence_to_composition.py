"""

Example from python distilled

Prefer composition over inheritence. 

With inheritence, as yourself:

    Is the object I am building a more specialized version of the parent I am considering?

    Or is the object merely USING it as a component in building something else.

"""


class StackStrange(list):
    def push(self, item):
        self.append(item)


a_list = [1, 2, 3]
strange_stack = StackStrange(a_list)
strange_stack.push(4)
strange_stack.push(5)
strange_stack.push(6)
print(strange_stack)
# so far so good, but wait. What is this???? A stack that can sort and reassign???
strange_stack[2] = 100
strange_stack.sort(reverse=True)
print(strange_stack)
# The object 'Stack' would make more sense when composition is used.
# When the new class uses a List but hides the implementation details of that list,
#  to users, that class would feel more like a stack.
class Stack:
    def __init__(self, *, container=None):
        if container is None:
            container = list()
        self._list = container

    def push(self, item):
        self._list.append(item)

    def __repr__(self):
        return "{}".format(self._list)


my_stack = Stack(container=a_list)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print(my_stack)

# tip to make it faster: turn it into an array
