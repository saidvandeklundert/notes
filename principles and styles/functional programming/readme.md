## Functional programming

In functional programming, the aim is to write 'pure functions'. A pure function is a function that does not have any side-effects. The function has (optional) parameters and returns an output. Nothing else outside of the function has its state altered in any way.

### Pure functions:
- do not mutate things outside of the function
- internal mutations are not visible outside of the function
- do not mutate arguments
- do not throw errors or exceptions (can cause errors though, out of memory for instance)
- always return a value
- when called with the same argument, will always return the same value


### Higher order functions:
- gets another argument as a function and/or
- returns a function as a result

### Closures:
- We have a nested function (funcion defined inside a function)
- the nested function refers to a value defined in the enclosing function.
- the enclosing function returns the nested function


Functional programming is a programming paradigm, a style of programming, where we mainly use immutable data structures. We try to avoid side effects by doing all of our computation using the evaluation of (mathematical) functions.


### Currying:
Curry functions are always unary functions which take one argument per application.

Currying is translating a function that takes multiple arguments into a sequence of functions, each accepting one argument.

### Function composition:

Easily put, combining functions. Combining pure functions to build chains of functions where the result of one function is passed as the argument of the next function. The result of the last function is the result of the whole chain.

### Reduce:

Reducing a collection to a single element is called fold or reduce. 

In Kotlin:
`Fold`: takes an initial value and uses it as the accumulated value on the first step. The output can be a different type than the input.
`Reduce`: uses the first and the second elements as operation arguments on the first step. Reduces a collection to a single element of the type of the collection.


### Crorecursion and recursion:

Corecursion is composing computation steps by using the output of one step as the input
of the next one, starting with the first step. Recursion is the same operation but starts
with the last step. Let’s take as an example a list of characters that you want to join into
a string representation.
