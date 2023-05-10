# On windows, this needs to run under main
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import time
from os import getpid

CPU_COUNT = cpu_count()


def cpu_bound_function(parameter) -> None:
    """
    Simulates an CPU-bound function using time.sleep(3).
    """
    print(f"cpu_bound_function called with argument {parameter} using PID {getpid()}")
    time.sleep(3)
    print(f"cpu_bound_function with argument {parameter} using PID {getpid()} ended")


def example_process_pool():
    with ProcessPoolExecutor(max_workers=CPU_COUNT) as executor:
        for id in range(CPU_COUNT):
            executor.submit(cpu_bound_function, id)


if __name__ == "__main__":
    example_process_pool()
