# On windows, this needs to run under main
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import threading
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
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(io_bound_function, ("a"))
    task2 = executor.submit(io_bound_function, ("b"))
    task3 = executor.submit(io_bound_function, ("c"))


if __name__ == "__main__":
    example_process_pool()
"""
io_bound_function called with argument a using PID 12824
io_bound_function called with argument b using PID 2752
io_bound_function called with argument c using PID 15316
io_bound_function with argument b using PID 2752 ended
io_bound_function with argument a using PID 12824 ended
io_bound_function with argument c using PID 15316 ended
"""