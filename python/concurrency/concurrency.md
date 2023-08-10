## Asyncio

Asynchronous programming refers to running routines and not blocking to wait for their completion. The `io` in `asyncio` refers to dealing with non-blocking IO. 

A coroutine is a function that can be suspended and resumed. With coroutines, users have control over when the coroutine suspends the execution.

Coroutines are used to enable concurrent execution of tasks. Many coroutines can be created at the same time. Coroutines are sometimes referred to as cooperative multitasking because the user chooses when a task is suspended. Preemptive multitasking, used in multithreading, is the opposite. Here, the operating system determines when a thread is suspended and resumed. 

Coroutines are more lightweight then a thread. Many coroutines can be run in a single process with a single thread.

With `async def`, you create coroutine function. Coroutines can use couritine-specific expressions:
- await: suspend the calling corouting and schedule the specified coroutine to execute. The caller will not resume untill the specified coroutine is done.
- async for
- async with


Coroutines run on the event loop.
## Multithreading

Every program runs in a process and has at least one thread that executes the program, the main thread. We can create additional threads to run things concurrently within the same process. In Python, this can be done using the `Thread` class.

Every thread requires resources, such as a stack space etc. The costs for setting up new threads can become expensive if we are creating and running many threads in our program. A good consideration is to reuse worker threads.

The `ThreadPoolExecutor` class, which extends the abstract Executor class, defines three methods to control a thread pool:
• `submit()`: Dispatch a function to be executed and return a Future object.
• `map()`: Call a function for each item in an iterable.
• `shutdown()`: Shut down the Executor.

## Multiprocessing

There is a memory space and an interpreter per process. Multiprocessing (MP) is a lot more expensive then threading.

Where threads can share memory in a process, processes cannot so easily do that. When you want to share memory between processes, that memory has to be serialized and transmitted from one process to the other. In Python, this information is pickled by the sender and unpickled by the receiver. If you cannot picle something, you cannot share it between processes.

Sharing data between processes is expensive so best kept small. 

Recommended to use the `ProcessPoolExecutor` when:
- the task you want to run is a pure function (or close to one)
- you perorm the same task many times for an object in a collection


When `ProcessPoolExecutor()` is called without arguments, it will use a number of worker processes that matches the number of logical CPUs in the system.

Throught the `ProcessPoolExecutor`, the worker processes can be configured with an initialization function to perform something before the tasks are started. This can be used to prepare something for use across the execution of tasks, like creating folders, queues or a logging infrastructure.

Using chunks can oftentime be more efficient when using the ProcessPoolExecutor. This is because it reduces
the number of internal task objects that are created.

## Terms and terminology

Future objects: a future object is a handle on a task that is executed asynchronously. A future object can exist in 1 of three states:
- scheduled
- running
- done

When a task is cancelled, it will be put into the done state.


Methods to wait for futures to complete:
- `as_completed()`: Returns an iterator over the Future instances (possibly created by different Executor instances) given by fs that yields futures as they complete (finished or cancelled futures).
- `wait()`: Wait for the Future instances (possibly created by different Executor instances) given by fs to complete. Can be given arguments to wait for:
  - all the futures to complete (default)
  - return upon the first exception
  - return when the first future completes



### Get the result from a future object


We retrieve the result from a task by calling `result()` on a Future. This will return the result from the task or None if the task did not return a value.

When we call `result()` on a future, the function call is blocking untill the tasks completes and a result can be retrieved. If the task has already been completed, the result is retrieved immediately.





## Notes and gotchas:


You can get the results up untill the first exception when using `map` on the `ThreadpoolExecutor`. The map method returns a generator which allows to iterate through the results once ready. Unfortunately, it is not possible to resume a generator after an exception occurs. 