# If a func uses yield, it defines an object known as a generator.
# A generator is a function that returns an object.
# The generator object only executes the function when you start iterating over it.
#

# Example:
def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


countdown(10)  # NOTHING happens here

for i in countdown(10):  # here we consume the generator, and here stuff happens:
    print(i)

# you can also consume it using next:
a_generator = countdown(10)
print(
    next(a_generator),
)
# do something else:
print(
    next(a_generator),
)
# next() is actually the same as calling the __next__() method:
print(a_generator.__next__())

# use a finally inside a generator, this will always run.
# usefull when the generator did not complete entirely, but is garbage collected.
# same goes for using a context manager.
# could be usefull in case the finally or context manager closes a file or some other resource.


# make a Generator restarable:
class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


x = Countdown(2)

for i in x:
    print(i)
for i in x:
    print(i)


# yield from delegates the iteration process to an outside iterator.
# next, we use it in the 'to_iterate()' function, which we can iterate to drain a generator:
def to_iterate():
    print("inside to_iterate()")
    a_generator = countdown(10)
    yield from a_generator
    yield from range(10)


# the following consumes the generators inside to_iterate() one after the other:
for i in to_iterate():
    print(i)


def gen_reader(file_name):
    for row in open(file_name, "r"):
        yield row


for row in gen_reader("flatten_list.py"):
    print(row, end="")
