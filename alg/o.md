Big-O: how your code slows as your input grows.

We consider two things:
`Time complexity`: how much time does it take to run a program?
`Space complexity`: how much extra space does it require to run a program?

Big-O is about:
- time complexity
- space complexity
- algorithmic complexity
- asymptotic complexity

Using Big-O allows us to separate reasoning about the efficiency of an algorithm from the programming language and/or hardware that is in use. It can tell us how much time it takes to run a function and how the runtime of the function grows as the input grows.

Applying Big-O:
1. focus on scalability (thing about a very big input to a function)
2. always consider the worst case scenario
3. remove all possible constants
4. consider different variables for different inputs
5. remove non-dominants

`O(1)`: constant time. Does not take longer with more input.
    Dict lookup

`O( log n)`: Logarithmic time. 

Everytime the input doubles, the amount of computations only increase by 1.

An algorithm is of logarithmic complexity if the processing time is proportional to the logarithm of the input elements. 

Example is binary search.

`O(N)`: linear time. Twice as much input will take twice as much time.

An algorithm is of linear complexity if the processing time or storage space is directly proportional to the number of input elements to be processed.

Example: walk through an array

`O(n log n)`: Linearithmic time.

`O(N²)`: Quadratic time. Performance is proportional to the squared size of the input data.

An algorithm is of quadratic complexity if the processing time is proportional to the square of the number of input elements.

Example: nested iteration over an array.

`O(N^3)`: Cubic Time. In the case of cubic complexity, the processing time of an algorithm is proportional to the cube of the input elements. The complexity of the following algorithm is 10*10*10 = 1,000. The three loops have a maximum of 10. The cubic complexity for a matrix update is O(n3).


`O(2^n)`: exponential time.

`O(n!)`: factorial.
    


Logarithm: the logarithm of a given number x is the exponent to which another fixed number, the base b, must be raised, to produce that number x. In CS, the base is always 2. 



When determining the efficiency of an algorithm, only consider the worst-case

Adding steps:
1. Add the notations together
2. Drop constants
3. Use different variables to represent the inputs
    Example:
    iterate array a and array b: O(a*b) and not O(N²)
4. Drop non-dominate terms.
    If you have O(N²) and O(n), the O(n) is less relevant.

Or a shorter version of this:
1. find the fastest growing term
2. take out the coefficient

## Logarithm

You can think of a logarithm as a question. For instance:

`log₂(8)` is like asking the following:


```
what do I need to power the base of 2 by in order to get to the number in the parentheses?
```

In this case, the answer is 3: 
```
2 * 2 * 2 = 8
   
2³ = 8
```


`log₁₀(100)` is like asking the following:

```
what do I need to power 10 by in order to get to 100?
```

Since the base is 10, in this case the answer is 2.

In computer science, we always asume `log₂`. This can be seen as `halfing` of the search space in binary search for instance. 


## Divide and conquer algorithms

Recursion, quick sort, binary search, fast Fourier transform, and merge sort are good examples of divide and conquer algorithms. Performance is sometimes an issue in the case of recursion. On multiprocessor machines, these algorithms can be executed on different processors after breaking them down into sub-problems.

## videos

Good video on logarithm is [here](https://www.youtube.com/watch?v=M4ubFru2O80).

[Big-O](https://www.youtube.com/watch?v=D6xkbGLQesk)
[Back to SWE Asymptotic bounding](https://www.youtube.com/watch?v=0oDAlMwTrLo)
[nedbatchelder](https://nedbatchelder.com/text/bigo.html)