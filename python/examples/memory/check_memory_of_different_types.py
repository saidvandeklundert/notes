# pip install Pympler
from pympler.asizeof import asizeof
from sys import getsizeof
import array
import numpy as np


alist_of_int = [x for x in range(0, 60000)]
array_of_int = array.array("i", alist_of_int)
np_array = np.array(alist_of_int)
print(asizeof(alist_of_int))
print(asizeof(array_of_int))
print(asizeof(np_array))
