import numpy
from sys import getsizeof
array = numpy.array([0,1,2,3])
for item in array:
    print(item)


alist = [0,1,2,3]

print("small list mem size:", getsizeof(alist))
print("small array mem size:",getsizeof(array))
del array
del alist
array = numpy.array([x for x in range(100000)])
alist = [x for x in range(100000)]
print("large list mem size:",getsizeof(alist))
print("large array mem size:",getsizeof(array))

# increase array size:

array = numpy.append(array, [1,2,3])

print("fin")