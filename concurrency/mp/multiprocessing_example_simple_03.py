from concurrent.futures import ProcessPoolExecutor
import time
from os import getpid


def io_bound_function(parameter_1, parameter_2):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(
        f"io_bound_function called with arguments {parameter_1, parameter_2} using PID {getpid()}"
    )
    time.sleep(3)
    print(
        f"io_bound_function with arguments {parameter_1, parameter_2} using PID {getpid()} ended"
    )
    return parameter_1, parameter_2


def example_process_pool_simple():
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.submit(io_bound_function, "a", "a")
        executor.submit(io_bound_function, "b", "b")
        executor.submit(io_bound_function, "c", "c")


def example_process_pool_args():
    arguments = [
        ("a", "b"),
        ("c", "d"),
        ("e", "f"),
    ]
    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg in arguments:
            executor.submit(io_bound_function, *arg)


def example_process_pool_args_unpacked():
    arguments = [
        {"parameter_1": 1, "parameter_2": 2},
        {"parameter_1": 3, "parameter_2": 4},
    ]
    futures = []
    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg in arguments:
            futures.append(executor.submit(io_bound_function, **arg))
    return futures


if __name__ == "__main__":
    example_process_pool_simple()
    example_process_pool_args()
    futures = example_process_pool_args_unpacked()
    for item in futures:
        print(item.result())
"""
io_bound_function called with arguments ('a', 'a') using PID 380
io_bound_function called with arguments ('b', 'b') using PID 13400
io_bound_function called with arguments ('c', 'c') using PID 29092
io_bound_function with arguments ('b', 'b') using PID 13400 ended
io_bound_function with arguments ('a', 'a') using PID 380 ended  
io_bound_function with arguments ('c', 'c') using PID 29092 ended
io_bound_function called with arguments ('a', 'b') using PID 13752
io_bound_function called with arguments ('c', 'd') using PID 15456
io_bound_function called with arguments ('e', 'f') using PID 15396
io_bound_function with arguments ('c', 'd') using PID 15456 ended
io_bound_function with arguments ('a', 'b') using PID 13752 ended
io_bound_function with arguments ('e', 'f') using PID 15396 ended
io_bound_function called with arguments (1, 2) using PID 30052
io_bound_function called with arguments (3, 4) using PID 1212
io_bound_function with arguments (3, 4) using PID 1212 ended
io_bound_function with arguments (1, 2) using PID 30052 ended
(1, 2)
(3, 4)
"""