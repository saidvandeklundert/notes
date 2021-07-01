# On windows, this needs to run under main
from concurrent.futures import ProcessPoolExecutor
import time
from os import getpid


def io_bound_function(parameter):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with argument {parameter} using PID {getpid()}")
    time.sleep(3)
    print(f"io_bound_function with argument {parameter} using PID {getpid()} ended")
    return parameter


def example_process_pool():
    ppe = ProcessPoolExecutor(max_workers=5)
    futures = []
    for i in range(1, 11):
        futures.append(ppe.submit(io_bound_function, i))
    print([future.result() for future in futures])
    return futures


if __name__ == "__main__":
    futures = example_process_pool()
    for item in futures:
        print(item.result())
"""
io_bound_function called with argument 1 using PID 9288
io_bound_function called with argument 2 using PID 16836io_bound_function called with argument 3 using PID 21132io_bound_function called with argument 4 using PID 24612io_bound_function called with argument 5 using PID 8548
io_bound_function with argument 3 using PID 21132 ended
io_bound_function with argument 2 using PID 16836 ended
io_bound_function called with argument 6 using PID 21132io_bound_function with argument 1 using PID 9288 ended
io_bound_function called with argument 7 using PID 16836io_bound_function called with argument 8 using PID 9288
io_bound_function with argument 5 using PID 8548 ended
io_bound_function with argument 4 using PID 24612 ended
io_bound_function called with argument 9 using PID 8548
io_bound_function called with argument 10 using PID 24612
io_bound_function with argument 6 using PID 21132 ended
io_bound_function with argument 7 using PID 16836 ended
io_bound_function with argument 8 using PID 9288 ended
io_bound_function with argument 10 using PID 24612 endedio_bound_function with argument 9 using PID 8548 ended
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
1
2
3
4
5
6
7
8
9
10
"""