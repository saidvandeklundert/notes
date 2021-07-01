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


Some interesting numbers to be aware of, the [Latency numbers every programmer should know](https://github.com/ardanlabs/gotraining/tree:/master/topics/go/language/arrays#industry-defined-latencies)

```
L1 cache reference ......................... 0.5 ns ...................  6 ins
Branch mispredict ............................ 5 ns ................... 60 ins
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

Some (very) rough comparisons that can be used to describe latency (using Intetl i7):
- 0.01ns    1 CPU instruction       1 meter 
- 1ns       100 CPU instructions    100 meter 
- 100ns     1 memory reference      10 kilometer
- 3 uS      read 1MB from memory    300 kilometer
- 825 uS    read 1MB from disk      82.500 kilometer (around the world, twice)
- 2 ms      disk seek               125.000 kilometer (to the moon )
- 150ms     ping US from Europe     15 million kilometer ( 10% between earth and the sun)

Alternatively:

1 instruction is 1 second
reference memory is 2 hours and 47 minutes
disk seek is 6 years and 4 months
disk seek and read 1MB is 8 years and 11 months
ping US is 475 years

All the previous numbers are to convey the following: most likely your program is IO-bound and not CPU bound. Just the amount of time to talk to peripherals gives you IO constraints.
## Multithreading

Multithreading can offer performance improvements for I/O intensive workloads. For instance, if some I/O has high latency (like reaching out to network devices), the more beneficial it is for the CPU to do something else in the mean time.

Though IO bound operations can see good improvements, the GIL will prevent multiple threads from making use of multiple CPUs. If you need to spread workload accross multiple CPUs, Multiprocessing might be a better choice.

Code examples are found [here](https://github.com/saidvandeklundert/python/blob/main/examples/concurrency/).


## Multiprocessing

Instead of starting _threads_, multiprocessing starts new _processes_.

Multiple threads that belong to 1 process are subject to the GIL. For IO-bound operations, this is fine. For CPU-bound operations, this is not good because you cannot utilize multiple cores.

With multiprocessing, each process is running in it's own Python intepreter which is subject to it's own GIL.

Code examples are found [here](https://github.com/saidvandeklundert/python/blob/main/examples/concurrency/).
## asyncio uses cooperative multitasking




## Subinterpreters