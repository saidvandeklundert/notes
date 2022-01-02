import itertools

# repeat something over and over again:
iterator = itertools.repeat(5, 5)

for i in iterator:
    print(i)

# use a counter:
counter = itertools.count(1)
for i in counter:
    print(i)
    if i > 5:
        break

# cycle an iterable over and over again:
count = 0
for item in itertools.cycle([1, 2, 3]):
    print(item)
    count += 1
    if count > 10:
        break


def func1(x):
    print(f"func1: {x}")


def func2(x):
    print(f"func2: {x}")


count = 0
for function in itertools.cycle([func1, func2]):
    count += 1
    function(count)
    if count > 10:
        break