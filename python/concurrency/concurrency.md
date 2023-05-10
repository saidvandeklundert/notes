
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



Methods to wait for futures to complete:
- `as_completed()`: Returns an iterator over the Future instances (possibly created by different Executor instances) given by fs that yields futures as they complete (finished or cancelled futures).
- `wait()`: Wait for the Future instances (possibly created by different Executor instances) given by fs to complete. Can be given arguments to wait for:
  - all the futures to complete (default)
  - return upon the first exception
  - return when the first future completes