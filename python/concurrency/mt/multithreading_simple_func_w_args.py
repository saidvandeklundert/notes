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


def example_threadpool():
    """
    Example where a function that requires an arg
     is passed to a ThreadPoolExecutor.
    In this case, the 'max_workers' is configurable.
    """
    print("Starting ThreadPoolExecutor")
    futures = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        argument_list = ["a", "b", "c"]
        for argument in argument_list:
            futures.append(executor.submit(io_bound_function, argument))
    print("Done threading the io_bound_function")
    return futures


if __name__ == "__main__":
    futures = example_threadpool()
    for item in futures:
        print(item.result())
"""
Starting ThreadPoolExecutor
io_bound_function called with argument a
io_bound_function called with argument b
io_bound_function called with argument c
io_bound_function with argument b ended
io_bound_function with argument a ended
io_bound_function with argument c ended
Done threading the io_bound_function
a
b
c
"""
