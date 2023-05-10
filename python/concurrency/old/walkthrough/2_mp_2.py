from concurrent.futures import ProcessPoolExecutor
import time
from os import getpid


def cpu_bound_function(parameter_1, parameter_2):
    """
    Simulates an CPU-bound function using time.sleep(3).
    """
    print(
        f"cpu_bound_function called with arguments {parameter_1, parameter_2} using PID {getpid()}"
    )
    time.sleep(3)
    print(
        f"cpu_bound_function with arguments {parameter_1, parameter_2} using PID {getpid()} ended"
    )
    return parameter_1, parameter_2


def example_process_pool_args_unpacked():
    arguments = [
        {"parameter_1": 1, "parameter_2": 2},
        {"parameter_1": 3, "parameter_2": 4},
    ]
    futures = []
    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg in arguments:
            futures.append(executor.submit(cpu_bound_function, **arg))
    return futures


if __name__ == "__main__":

    futures = example_process_pool_args_unpacked()
    for item in futures:
        print(item.result())
