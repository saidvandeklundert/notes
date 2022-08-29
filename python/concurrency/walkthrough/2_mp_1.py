# On windows, this needs to run under main
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import threading
import time
from os import getpid


def cpu_bound_function(parameter):
    """
    Simulates an CPU-bound function using time.sleep(3).
    """
    print(f"cpu_bound_function called with argument {parameter} using PID {getpid()}")
    time.sleep(3)
    print(f"cpu_bound_function with argument {parameter} using PID {getpid()} ended")
    return parameter


def example_process_pool():
    executor = ProcessPoolExecutor(max_workers=3)
    executor.submit(cpu_bound_function, ("a"))
    executor.submit(cpu_bound_function, ("b"))
    executor.submit(cpu_bound_function, ("c"))


if __name__ == "__main__":
    example_process_pool()
