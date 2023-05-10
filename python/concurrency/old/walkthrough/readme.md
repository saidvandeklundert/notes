



## Introduction


## Summary of concurrency options in Pyton and in general:

In Python, there are 4 ways in which you can make your code run concurrently:


| method            | module         | parallel |
| ----------------- |:--------------:| --------:|
| (multi) threading | threading      | no       |
| multiprocessing   | multiprocessing| yes      |
| async             | asyncio        | no       |
| subinterpreter    | subinterpreters| yes      |

In addition to these options, there are other ways in which you can also speed up your code. Some of those options are:
- scale out, running services in parallel
- distributed systems, tied together with a message bus (for instance, 0mq)
- rewrite things in another language: C and Rust compile to machine code and are a lot faster
- use a library/tool that does the complicated parts for you:
  - https://github.com/rayon-rs/rayon
  - https://github.com/dask/dask
  - map reduce


For threading and multiprocessing:

The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

For async:

## Terms

Terms mostly from Fluent Python.

`Concurrency`: the ability to handle multiple tasks, making progress one at a time or in parrallel. A single core CPU is concurrency capable if the OS scheduler interleaves execution of pending tasks.

`Parallelism`: multiple computations at the same time. 

`Process`: instance of a computer program while it is running, using memory and a slice of CPU time. Processes can communicate via pipes, sockets or memory mapped files, all of which cary raw bytes.

Processes can spawn subprocesses, each called a child process. These are also isolated from the parent.

Processes allow preemptive multitasking: the OS scheduler preempts each running process periodically.

`Thread`: an execution unit within a single process. When a process starts, it uses a single thread, the main thread. A process can create more theads to operate concurrently by calling OS APIs. Threads within a process share the same memory space, which hold Python objects. This makes it easy to share (as well as corrupt) data.
Threads also allow preemptive mutitasking, the OS scheduler determines when code is run. 

Threads are ligher when compared to processes.

`Coroutine`: a function that can suspend itself and resume later. Coroutines support cooperative multitasking: each coroutine must explicitly cede control with the yield or await keyword, so that another may proceed concurrently (but not in parallel). This means that any blocking code in a coroutine blocks the execution of the event loop and all other coroutines—in contrast with the preemptive multitasking supported by processes and threads. On the other hand, each coroutine consumes less resources than a thread or process doing the same job.

Single process, single thread cooperative multitasking design: your code determines when it yields.


`Queue`:

`Lock`: mutex: Mutal Exclusion. Something that you can use to  avoid corruption of data. You lock access to it, then update that data, then release the lock. While a thread has the lock, other threads cannot access it.

`GIL: Global Interpreter lock`: A Mutex that ensures only one thread controls that interpreter at a time. This is severely limiting to muti-threaded applications. It does prevent race conditions with memory and reference allocations without the programmer having to put a mutex (mutual exclusion) in place everywhere.





## Interesting numbers:

Some interesting numbers to be aware of, the [Latency numbers every programmer should know](https://github.com/ardanlabs/gotraining/tree:/master/topics/go/language/arrays#industry-defined-latencies)

```
L1 cache reference ......................... 0.5 ns ...................  6 ins
L2 cache reference ........................... 7 ns ................... 84 ins
Main memory reference ...................... 100 ns ................. 1200 ins           
Send 2K bytes over 1 Gbps network ....... 20,000 ns (20 µs) ........  240k ins
SSD random read ........................ 150,000 ns (150 µs) ........ 1.8M ins
Read 1 MB sequentially from memory ..... 250,000 ns (250 µs) .......... 3M ins
Round trip within same datacenter ...... 500,000 ns (0.5 ms) .......... 6M ins
Read 1 MB sequentially from SSD* ..... 1,000,000 ns (1 ms) ........... 12M ins
Disk seek ........................... 10,000,000 ns (10 ms) ......... 120M ins
Read 1 MB sequentially from disk .... 20,000,000 ns (20 ms) ......... 240M ins
Send packet CA->Netherlands->CA .... 150,000,000 ns (150 ms) ........ 1.8B ins
```

Some (very) rough comparisons that can be used to describe latency (using Intel i7):
- 0.01ns    1 CPU instruction       1 meter 
- 1ns       100 CPU instructions    100 meter 
- 100ns     1 memory reference      10 kilometer
- 3 uS      read 1MB from memory    300 kilometer
- 825 uS    read 1MB from disk      82.500 kilometer (around the world, twice)
- 2 ms      disk seek               125.000 kilometer (to the moon )
- 150ms     ping US from Europe     15 million kilometer ( 10% between earth and the sun)


All the previous numbers are to convey the following: most likely your program is IO-bound and not CPU bound. Just the amount of time to talk to peripherals gives you IO constraints.

### Challenges that come with concurrency

When you are trying to implement concurrency, the following topics require some thought:
- memory allocation
- scheduling
- throughput
- distribution
- deadlocks
- execution coordination
- resource starvation

## Concurrent.futures

For multithreding and multiprocessing, most of the focuss will be on using concurrent.futures. The `concurrent.futures.Executor` classes encapsulate the pattern of “spawning a bunch of independent threads and collecting the results in a queue”. Effectively, this greatly simplifies concurrent programming.

The `Executor.submit()` encapsulates the asynchronous execution of a callable. In doing so, it creates an instance of a `Future`. 
On the instance of the `Future`, you can call `result` to return the result of the call that the future represents.

## no concurrency

Run the examples without any concurrency:

```
python .\read_web_page_single_thread.py
python .\fluent_spin.py
```

## Multithreading

Multithreading can offer performance improvements for I/O-bound workloads. 

For instance, when you issue a command on a network device, it might take a second or 2 before there is any return. Using threading, you can keep the CPU busy and do a lot more concurrently.

Python ensures every thread gets to run. By default, a thread will drop the GIL after 5 ms in Python 3 (if it hasn't done so before because of waiting for I/O). This is something you can change with `sys.setswitchinterval()`.

Though IO bound operations can see good improvements, the GIL will prevent multiple threads from making use of multiple CPUs. For CPU-bound work, multithreading will not offer benefits and might even make things slower.

Examples:

```
python .\read_web_page_threading.py
python .\multithreading_1_cpu.py
python .\fluent_mt.py 
```


## Multiprocessing

Instead of starting _threads_, multiprocessing starts new _processes_.

Multiple threads that belong to 1 process are subject to the GIL. For IO-bound operations, this is fine. For CPU-bound operations, this is not good because you cannot utilize multiple cores.

With multiprocessing, each process is running in it's own Python intepreter which is subject to it's own GIL. This means that the lock will not get in the way.

It also means that sharing data between the processes is more difficult. You can make processes share data by sending bytes from one process to the other, or you can do something simpler. Like writing to and reading from a file.


Examples:

```
python .\read_web_page_mp.py
python .\multiprocessing_multiple_cpus.py
python .\fluent_mp.py 
```

## asyncio uses cooperative multitasking

Asyncio's concurrency is managed by Python and has less overhead associated with it when compared to threads.

A big downside is the age and the robustness of asyncio as it is still relatively new.

Asyncio does not depend on the OS threading mechanism. It is suited to speeding up IO-bound tasks.

Asyncio is a single-threaded and single process designed way of concurrency that uses cooperative multitasking.

![Asyncio](/img/event_loop.png "From https://eng.paxos.com/python-3s-killer-feature-asyncio")

In asyncio, the event loop keeps a queue of tasks, which are a wrapper around a construct called coroutines.

You may have also heard about Green threads. Those are user level thread that are controlled by the Python runtime.

Normal threads:

![Threads](/img/python_concurrency_threads.png "From europython in 2017")

Green threads:

![Green threads](/img/python_concurrency_ult.png "From europython in 2017")


```
python .\read_web_page_async.py
python .\async_1_cpu.py
python .\fluent_async.py
```


## When to use which one


With threading, multiple threads are executing within a single proces that is subject to the GIL. There is little overhead in terms of memory/CPU and complexity. Threading can help speed up IO-bound tasks. It is mature and very easy to use. Usually, turning a function into one that can be dispatched using the `ThreadPoolExecutor` is very straightforward.

When multiprocessing is used, the main or parent process starts several child processes. These processes have their own GIL and they can run in parallel, each on their own CPU. Multiprocessing can help speed up CPU-bound and IO-bound tasks. Though, if the task is purely IO-bound, the additional complexity and overhead might be worth reconsidering multithreading.

Using asyncio is ideal for IO-bound tasks. When something is executed using asyncio, the program or function is still subject to the GIL. It is single threaded and it runs in a single process. The async io library using cooperative multitasking. Different tasks are scheduled and fed to the event-loop. After they complete, the task will report back in with the event loop. Async cannot be used to spead up CPU-bound tasks. The benefit of asyncio is that the model is more powerfull when compared to multithreading. Python managing it's own threads (green threads) is a lot more efficient when compared to OS threads. The downside is that asyncio is a lot less mature when compared to threading and it is more difficult. It requires a lot more thought and effort to turn regular code into code that plays nice with asyncio.

Async IO cannot deliver parallelism.



## Interesting links:
- https://github.com/ArjanCodes/2022-asyncio
- Chapter 19,20 and 21 in Fluent Python: https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch19.html
- mastering concurrency with asyncio: https://learning.oreilly.com/library/view/python-concurrency-with/9781617298660/
- an intro to threading: https://realpython.com/intro-to-python-threading/
- docs on concurrent futures: https://docs.python.org/3/library/concurrent.futures.html
- docs on asyncio: https://docs.python.org/3/library/asyncio.html?highlight=asyncio#module-asyncio
- what is the gil: https://realpython.com/python-gil/
- youtube playlist Łukasz Langa (Python resident engineer, async maintainer): 
  - https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB
  - https://www.youtube.com/channel/UCRF82wX0EPwqvKMBwvB4fQg  
- nogil: https://github.com/colesbury/nogil
- python switches threads every 5 ms: https://stackoverflow.com/questions/54256847/why-does-python-switch-threads
- picture: https://eng.paxos.com/python-3s-killer-feature-asyncio
- asyncio code samples: https://github.com/concurrency-in-python-with-asyncio/concurrency-in-python-with-asyncio
- map reduce: https://pdos.csail.mit.edu/6.824/schedule.html