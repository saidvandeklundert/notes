array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [
    0,
    1,
    2,
    3,
]


# While loop to traverse the entire array:
i = 0
while i < len(array):
    print(array[i])
    i += 1
"""
0
1
2
3
"""
# While loop stopping at the second to last item:
i = 0
while i < len(array) - 1:
    print(array[i])
    i += 1
"""
0
1
2
"""
# While loop over an array doing something in case it did not break:
i = 0
while i < len(array):
    print(array[i])
    i += 1
else:
    print("traversed the whole thing")
"""
0
1
2
3
traversed the whole thing
"""
# While loop over an array in reverse order:
print("--")
i = len(array) - 1

while i >= 0:
    print(array[i])
    i -= 1

"""
3
2
1
0
"""