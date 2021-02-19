

# Multithreading

Multithreading can offer performance improvements for I/O intensive workloads. For instance, if some I/O has high latency (like reaching out to network devices), the more beneficial it is for the CPU to do something else in the mean time.

Though IO bound operations can see good improvements, the GIL will prevent multiple threads from making use of multiple CPUs. If you need to spread workload accross multiple CPUs, Multiprocessing might be a better choice.

```python
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
        future = executor.submit(io_bound_function, ('a'))
        future = executor.submit(io_bound_function, ('b'))
        future = executor.submit(io_bound_function, ('c'))
    print("All tasks complete")
```

Calling the previous function outputs the following:

```
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
```

```python
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
        argument_list = [ 'a', 'b', 'c' ]
        for argument in argument_list:
            futures.append(
                executor.submit(
                    io_bound_function, argument
                )
            )     
    print("Done threading the io_bound_function")
    return futures

if __name__ == '__main__':
    futures = example_threadpool()
    for item in futures:
        print(item.result())
```

The previous function outputs the following:

```
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
```

Another example where the `io_bound_function` takes 2 parameters. In this example, the parameters are assigned as key/values in a dictionary that is then passed along with `executor.submit`:

```python
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
                {'parameter_1' : 1, 'parameter_2' : 2},
                {'parameter_1' : 3, 'parameter_2' : 4} 
            ]
        for argument in argument_dictionary:
            futures.append(
                executor.submit(
                    io_bound_function, **argument 
                )
            )     
    print("Done threading the io_bound_function")
    return futures

if __name__ == '__main__':
    futures = example_threadpool()
    for item in futures:
        print(item.result())
```


# Multiprocessing

# asyncio uses cooperative multitasking




