


### Complexity analysis

This is the process of determining how efficient an algorithm is. This usually involves analysing the following:
- time complexity: how fast something runs
- space complexity: how much auxiliary memory an algorithm takes up

Both are expressed using `Big O` notation. Together, they are referred to as space/time complexity.

#### Big O notation

This notation is used to describe the time and space complexity of algorithms in the worst-case scenario's.

It is an effective way of describing the behavior of an algorithm under varying circumstances and communicating it clearly without needing to get into specifics.


List of Big O notations:
```
Constant:       O(1)
Logarithmic:    O(log(n))
Linear:         O(n)
Log-linear:     O(nlog(n))
Quadratic:      O(n2)
Cubic:          O(n3)
Exponential:    O(2 ** n)
Factorial:      O(n!)
```

Constant:       O(1)

Something is O(1) if the number of operations does not depend on the size of the input.


### Memory

Endiannes: oredering of bytes when representing a number in binary.

Memory is like a canvas with a lot of memory slots. The slots are finite in nature, so the amount of memory an algorithm uses matters a lot.

Additionally, allocating and de-allocating are not expensive per-se, but when it needs to be done a lot of times, there is an associated cost.

[Latency numbers every programmer should know](https://github.com/ardanlabs/gotraining/tree/master/topics/go/language/arrays#industry-defined-latencies)

Some relevant times (gathered on a 4 Core i7-9xx processor):
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


### Logarithm

Mathematical concept defined by the following:
![Logarithm](/img/logarithm.PNG "Logarithm")


In coding, oftentimes a logarithm base of 2 is implied. 

The 'n' implied in O(log(n)) refers to the input.

When the exponent is incremented by 1, the value of n doubles. 

When a function has O(log(n)) efficiency, it means the following:
- as the input of a function can doubles (n is incremented by 1)
- the amount of steps to complete the operations is incremented only by 1

Compare this to a linear complexity algorithm. In that case, when the input doubles, the amount of operations also double.