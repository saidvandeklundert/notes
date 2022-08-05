import copy
from multiprocessing.spawn import import_main_path
import time
from random import randint
import random


tests = [
    [random.randint(0, 10000000) for i in range(1000000)],
]
from in_place_begin_partition import quicksort_in_place_begin_partition
from in_place_end_partition import quicksort_in_place_end_partition
from compact import quicksort_compact
from lc_qs import sortArray_1, sortArray2
from clean_no_comments import quick_sort

if __name__ == "__main__":

    # assert in_place_arr_end_partition == not_in_place_result

    quicksort_variations = [
        quicksort_compact,
        quicksort_in_place_begin_partition,
        quicksort_in_place_end_partition,
        sortArray_1,
        sortArray2,
        quick_sort,
    ]

    results = []
    for qs in quicksort_variations:

        # print(f"running quicksort variant {qs_name}:")
        qs_input = copy.copy(tests[0])
        q_start = time.time()
        qs_return = qs(qs_input)
        q_finish = time.time()
        if qs_return is None:
            results.append(qs_input)
        elif isinstance(qs_return, list):
            results.append(qs_return)

        print(f"{qs.__name__} ran in {q_start - q_finish}\n")
    tests[0].sort()  # use buit-in sort to verify all quick sorts
    for result in results:

        assert result == tests[0]
