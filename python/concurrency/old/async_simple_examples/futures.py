import asyncio


# https://docs.python.org/3/library/asyncio-task.html#creating-tasks

# A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.
# Create a future:
fut = asyncio.Future()

# Print the state of the future:
print(fut.done())

# check the result of the future:
try:
    print(fut.result())
except asyncio.InvalidStateError:
    print("Invalid state")

# manually set the result of the future:
fut.set_result("Result is set!!")

# check the state of the future again:
print("fut.result()", fut.done())

# check the result of the future again:
print("fut.result()", fut.result())

# check if the future is cancelled:
print("fut.cancelled(): ", fut.cancelled())
