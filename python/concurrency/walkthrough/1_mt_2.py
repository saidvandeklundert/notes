from concurrent.futures import ThreadPoolExecutor
import time


def io_bound_function(parameter_1, parameter_2):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with arguments {parameter_1} and {parameter_2}")
    time.sleep(3)
    print(f"io_bound_function with arguments {parameter_1} and {parameter_2} ended")
    return parameter_1, parameter_2


def example_threadpool():
    """
    Example where a function that requires an arg
     is passed to a ThreadPoolExecutor.
    In this case, the 'max_workers' is configurable.
    """
    print("Starting ThreadPoolExecutor")
    futures = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        argument_dictionary = [
            {"parameter_1": 1, "parameter_2": 2},
            {"parameter_1": 3, "parameter_2": 4},
        ]
        for argument in argument_dictionary:
            futures.append(executor.submit(io_bound_function, **argument))
    print("Done threading the io_bound_function")
    return futures


if __name__ == "__main__":
    futures = example_threadpool()
    for item in futures:
        print(item.result())
