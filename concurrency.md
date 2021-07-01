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

Code examples are found [here](https://github.com/saidvandeklundert/python/blob/main/examples/concurrency/).




## Multiprocessing

Instead of starting _threads_, multiprocessing starts new _processes_.

Multiple threads that belong to 1 process are subject to the GIL. For IO-bound operations, this is fine. For CPU-bound operations, this is not good because you cannot utilize multiple cores.

With multiprocessing, each process is running in it's own Python intepreter which is subject to it's own GIL.


## asyncio uses cooperative multitasking




## Subinterpreters