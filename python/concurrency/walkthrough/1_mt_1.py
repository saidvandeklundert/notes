from concurrent.futures import ThreadPoolExecutor
import time


def io_bound_function(parameter):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with argument {parameter}")
    time.sleep(3)
    print(f"io_bound_function with argument {parameter} ended")
    return parameter


def example_simple():
    """
    Simple example starting a few threads.
    """
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(io_bound_function, ("a"))
        future = executor.submit(io_bound_function, ("b"))
        future = executor.submit(io_bound_function, ("c"))
    print("All tasks complete")


if __name__ == "__main__":
    example_simple()
"""
>>> example_simple()
Starting ThreadPoolExecutor
io_bound_function called with argument a
io_bound_function called with argument b
io_bound_function called with argument c
io_bound_function with argument c ended
io_bound_function with argument a ended
io_bound_function with argument b ended
All tasks complete
>>>
"""
