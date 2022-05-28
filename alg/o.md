Big-O: how your code slows as your code grows.

Big-O is about:
- complexity
- time complexity
- algorithmic complexity
- asymptotic complexity

`O(1)`: constant time. Does not take longer with more input.
    Dict lookup

`O(N)`: linear time. Twice as much input will take twice as much time.
    Walk through an array

`O(N²)`: Quadratic time. Performance is proportional to the squared size of the input data.
    Nested iteration over an array.

`O(N^3)`: Cubic Time. Iterate an array three times.
    
`O( log n)`: Logarithmic time. 

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