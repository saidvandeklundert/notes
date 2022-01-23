import array
from sys import getsizeof
# https://docs.python.org/3/library/array.html
numbers_list = [x for x in range(10_000_000)]
numbers_array = array.array("L",[x for x in range(10_000_000)])

print(f"numbers_list size in bytes: {getsizeof(numbers_list)}")
print(f"numbers_array size in bytes: {getsizeof(numbers_array)}")

print("Changing numbers_array from signed long long to signed int:")
del numbers_array
numbers_array = array.array("i",[x for x in range(10_000_000)])
print(f"numbers_array size in bytes: {getsizeof(numbers_array)}")