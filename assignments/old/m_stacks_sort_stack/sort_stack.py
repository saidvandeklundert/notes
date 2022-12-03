inputs = [
    {"stack": [-5, 2, -2, 4, 3, 1]},
    {"stack": [3, 4, 5, 1, 2]},
    {"stack": [0, -2, 3, 4, 1, -9, 8]},
    {"stack": [2, 4, 22, 1, -9, 0, 6, 23, -2, 1]},
    {"stack": [3, 4, 5, 1, 2]},
    {"stack": [-1, 0, 2, 3, 4, 1, 1, 1]},
    {"stack": []},
    {"stack": [1]},
    {"stack": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]},
    {"stack": [9, 2, 8, 1]},
    {"stack": [2, 33, 44, 2, -9, -7, -5, -2, -2, -2, 0]},
    {"stack": [3, 3, 3, 3, 3, 3]},
    {"stack": [0, 0]},
    {"stack": [2, 22, 222, 3, 33, 33, 9, 2, 3, 312, -9, -2, 3]},
    {"stack": [3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3]},
    {"stack": [-5, 2, -2, 4, 3, 1]},
]


def sortStack(stack):

    return recurse(stack, [], False)


def recurse(stack, array, emptied):
    if emptied == True:
        array.sort(reverse=True)
        print(stack, array)

        if len(array) > 0:
            stack.append(array.pop())
            return recurse(stack, array, True)
        elif len(array) == 0:
            return stack
    if len(stack) > 0:
        array.append(stack.pop())
        return recurse(stack, array, False)
    if len(stack) == 0:

        return recurse(stack, array, True)


def sortStack_fast(stack):
    print(f"recurse first {stack}")
    if len(stack) == 0:
        print("happened")
        return stack

    top = stack.pop()

    sortStack_fast(stack)  # this is where the first recurse re-enters
    insertInSortedOrder(stack, top)  # this is the second recurse
    return stack


def insertInSortedOrder(stack, value):
    print(f"recurse second {stack}")
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insertInSortedOrder(stack, value)

    stack.append(top)


if __name__ == "__main__":
    for test in inputs:

        print(sortStack(**test))
        print("fast", sortStack_fast(**test))
        print(50 * "_")
