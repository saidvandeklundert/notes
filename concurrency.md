## Introduction

In Python, there are 4 ways in which you can make your code run concurrently:


| method        | module           | parallel  |
| ------------- |:-------------:| -----:|
| (multi) threading | threading | no |
| multiprocessing | multiprocessing      |   yes |
| async | asyncio      |    no |
| subinterpreter| subinterpreters      |    yes |


With threading, multiple threads are executing within a single proces that is subject to the GIL. There is little overhead in terms of memory/CPU and complexity. Threading can help speed up IO-bound tasks.

When multiprocessing is used, the main or parent process starts several child processes. These processes have their own GIL and they can run in parallel, each on their own CPU. Multiprocessing can help speed up CPU-bound and IO-bound tasks. Though, if the task is purely IO-bound, the additional complexity and overhead might be worth reconsidering it.

Using asyncio is ideal for IO-bound tasks. When something is executed using asyncio, the program or function is still ubject to the GIL. It is single threaded and it runs in a single process. The async io library using cooperative multitasking. Different tasks are scheduled and fed to the event-loop. After they complete, the task will report back in with the event loop. 

Async IO != parallelism.

Subinerpreters have a GIL per interpreter and every subinterpreter can run on a separate CPU. It uses less overhead when compared to multiprocessing but is still expirimental in Python 3.9.


## Multithreading

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


## Multiprocessing

Instead of starting _threads_, multiprocessing starts new _processes_.

Multiple threads that belong to 1 process are subject to the GIL. For IO-bound operations, this is fine. For CPU-bound operations, this is not good because you cannot utilize multiple cores.

With multiprocessing, each process is running in it's own Python intepreter which is subject to it's own GIL.



```python
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
    task1 = executor.submit(io_bound_function, ('a'))
    task2 = executor.submit(io_bound_function, ('b'))
    task3 = executor.submit(io_bound_function, ('c'))
```
The above `example_process_pool()` outputs the following (on Linux):

```
>>> example_process_pool()    
>>> io_bound_function called with argument a using PID 10873
io_bound_function called with argument b using PID 10875
io_bound_function called with argument c using PID 10874
io_bound_function with argument a using PID 10873 ended
io_bound_function with argument c using PID 10874 ended
io_bound_function with argument b using PID 10875 ended
```

```python
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
    for i in range(1,11):
        futures.append(ppe.submit(io_bound_function, i))
    print([future.result() for future in futures])        
    return futures

if __name__ == '__main__':
    futures = example_process_pool()
    for item in futures:
        print(item.result())
```

The above outputs the following:

```
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
```


We can also use the context manager:

```python
from concurrent.futures import ProcessPoolExecutor
import time
from os import getpid

def io_bound_function(parameter_1, parameter_2):
    """
    Simulates an IO-bound function using time.sleep(3).
    """
    print(f"io_bound_function called with arguments {parameter_1, parameter_2} using PID {getpid()}")
    time.sleep(3)
    print(f"io_bound_function with arguments {parameter_1, parameter_2} using PID {getpid()} ended")
    return parameter_1, parameter_2

def example_process_pool_simple():    
    with ProcessPoolExecutor(max_workers=10) as executor:              
        executor.submit(io_bound_function, 'a', 'a')
        executor.submit(io_bound_function, 'b', 'b')
        executor.submit(io_bound_function, 'c', 'c')

def example_process_pool_args(): 
    arguments = [('a', 'b'), ('c', 'd'), ('e', 'f'), ]   
    with ProcessPoolExecutor(max_workers=10) as executor:              
        for arg in arguments:
            executor.submit(io_bound_function, *arg)

def example_process_pool_args_unpacked(): 
    arguments = [
            {'parameter_1' : 1, 'parameter_2' : 2},
            {'parameter_1' : 3, 'parameter_2' : 4} 
        ]        
    futures = []  
    with ProcessPoolExecutor(max_workers=10) as executor:              
        for arg in arguments:
            futures.append(
                executor.submit(io_bound_function, **arg)
                )
    return futures        

if __name__ == '__main__':
    example_process_pool_simple()
    example_process_pool_args()
    futures = example_process_pool_args_unpacked()
    for item in futures:
        print(item.result())
```


## asyncio uses cooperative multitasking




## Subinterpreters