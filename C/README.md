###

From [wiki](https://en.wikipedia.org/wiki/Imperative_programming)
```
In computer science, imperative programming is a programming paradigm that uses statements that change a program's state. In much the same way that the imperative mood in natural languages expresses commands, an imperative program consists of commands for the computer to perform. Imperative programming focuses on describing how a program operates.

The term is often used in contrast to declarative programming, which focuses on what the program should accomplish without specifying all the details of how the program should achieve the result.
```

From Modern C:
```
In many ways, C is a permissive language; programmers are allowed to shoot themselves in the foot or other body parts if they choose to, and C will make no effort to stop them. 
```
### Grammer and stuff

`Constant expression`: an expression that evaluates to a constant that is computed at compile time. A constant expression only involves constants. 

`Declarations`: All identifiers in a program have to be declared. Keywords of the C language are predefined and need no declaration. 

Example declaration of an array:

```c
double array_name[5];
```

Declarations are bound to the scope in which they appear.

`Identifiers`: names in the C program. Examples are variables, functions, arrays, structures, unions, labels, etc.

`Definition`: specifies objects. Declarations specify identifiers. Objects and functions must have exactly one definition.

`Object`: things that we deal with in our program.

`Functions`: methods that we use to deal with things.

`Initializing an object`: 

```c
size_t i = 0;
```

`Statements`: instructions that tell the compiler what to do with identifiers that have been declared so far. From KR, a statement 'specifies the computing operation to be done'. 

`Include files`:

`Header files`: file containing C function declarations and macro definitions that can be shared between several source files. Example on how to use one:
```c
#include <stdio.h>
```
The C library is interfaced via several header files.

Input and Output can be found in `stdio.h`. String things are in `string.h` and there are many more available.

Putting in a header file is akin to copying the code into the source file.

The following form is for system header files:
```c
#include <file>
```

The following form is for your own program header files:
```c
#include "file"
```

Example header
```c
#ifndef FOO_H_   /* Include guard */
#define FOO_H_

int foo(int x);  /* An example function declaration */

#endif // FOO_H_
```

`Scope`: part of a program where an identifier is visible.

The C standard: https://stackoverflow.com/questions/81656/where-do-i-find-the-current-c-or-c-standard-documents

`Cast`: explicitly converting one datatype into another. Also known as type casting or type-conversion. Type conversions can be implicit (performed by the compiler) or explicit (use of the cast operator). A cast operator consists of a type name, in parentheses:

```c
int people = 4;
double x = (double)people;
```

`Operators`: +, != etc.
`Operands`: things that operators are applied to.


`Abstract state machine`: the compiler can compute away a lot of nonesense at compile time to make the program faster at runtime. Programs execute as if following the abstract state machine. Abstract state machines cheat wherever they can and only respect the observable states of the abstract state machine.

Another thing worth noting is that type determines optimization opportunities.
`Variables`: store values that can be used during the computation.
`Values`: All values are numbers or translate to numbers.

```
This property really concerns all values a C program is about, whether these are the characters or text we print, truth values, measures that we take, or relations that we investigate. Think of these numbers as mathematical entities that are independent of your program and its concrete realization.
```

`Data`: From MC
```
The data of a program execution consists of all the assembled values of all objects at a given moment. The state of the program execution is determined by:
- The executable
- The current point of execution
- The data
- Outside intervention, such as IO from the user

We don’t want the result of a computation to depend on the executable (which is platform specific) but ideally to depend only on the program specification itself. An important step to achieve this platform independence is the concept of types.
```
`Types`: All values have a type that is statically determined. The operations that are possible on a value are determined by it's type. In effect, the type of a value is the thing that determines the result of operations.

A type’s binary representation is observable and determines the results of all operations.

`Errors`: Generally, there are three different ways to generate or convey errors in C:
- return a special value that indicates an error
- return a special value that indicates a function was successful
- return a positive number on succes and a negative number on failure

Example on how error checking could be implemented in C:
```c
if (puts("hello world") == EOF) {
  perror("can't output to terminal:");
  exit(EXIT_FAILURE);
}
```

`Opaque types`: types specified through functional interfaces.

`String constant` or `string literal`: 0 or more characters surrounded by double quotes. 

### print formatters


`integers`: `d` `u`
`bit pattern`: `x`
`integer characters`: `c`
`string characers`: `s`
`address`: `p`
`floating points`: `g`

### Control

C has five conditional control statements: `if`, `for`, `do`, `while`, and `switch`. 

#### if and if else

```c
if (i > 10) {
    b = i - 10;
}
```

Also possible:
```c
   if (arg == 'a') {
     puts("a");
   } else if (arg == 'b') {
     puts("b");
   } else if (arg == 'c') {
     puts("c");
   } else {
     puts("something else, anything really");
   }
```

When numericals are evaluated, the value 0 is a logical false and the rest is true.

#### Switch case

This is basically and if/else if/else block written differently:

```c
   switch (arg) {
     case 'a': puts("a");
               break;
     case 'b': puts("b");
               break;
     case 'c': puts("c");
               break;
     default: puts("something else, anything really");
   }
```

The `switch` statement is fall through. If a case is missing a break statement, all the cases after the matching case will be executed untill a break case is hit.

Note that `case` values must be integer constant expressions.

From the [C99 and the n1570 draft of the C2011 standard]:
```
6 An integer constant expression shall have integer type and shall only have operands that are integer constants, enumeration constants, character constants, sizeof expressions whose results are integer constants, _Alignof expressions, and floating constants that are the immediate operands of casts. Cast operators in an integer constant expression shall only convert arithmetic types to integer types, except as part of an operand to the sizeof or _Alignof operator.
```

Also this: https://coderedirect.com/questions/434275/gcc-doesnt-support-simple-integer-constant-expression


switch labels must be constant expressions, they have to be evaluated at compile time. If you want to branch on run-time values, you must use an if.

#### Iterations

We can use`for` to iterate something. The syntax in this case is the following:
```
for (clause1; condition2; expression3) statement-or-block
```

Example:
```c
    for (size_t i = 0; i < 5; ++i)
    {
        some_func(i);
    }
```

We can also use `while`:
```
while (condition) statement-or-block
   do statement-or-block while(condition);
```
We can `do while` and we can `while do`.


The `break` statement can be used to stop both `for` as well as `while` loop.

The `continue` statement skips the rest of a block and continues the iteration.

As an artifact of the past, `for(;;)` is sometimes written instead of `while(true)`.

### Data types

C programs primarily reason about values and not about their representation.

All basic C types are kinds of numbers, though not all can be used for arithmetic.

Vlues have a type and a binary representation.



There are 4 main type classes:
- unsigned integers
- signed integers
- real floating-point numbers
- complex floating-point numbers:

Basic data types, as described by KR:
- char: byte that can hold a charater
- int: integer typically reflecting the natural size of the integers on the host machie
- float: sinle precision floating point
- double: double-precision floating point

There is also [C types](https://en.wikipedia.org/wiki/C_data_types) on wikipedia. There it says that 'The C language provides the four basic arithmetic type specifiers char, int, float and double, and the modifiers signed, unsigned, short, and long'.

`int`: variable that can be used to contain integral values only
`float`: numbers that contain decimal places
`double`: same as float but with roughly twice the precision. Used when the range of a float is not sufficient.
`size_t`: unsigned integer type used to represent the sizes of objects. Size is based on the architecture of the platform
`bool`: unsigned, 0 or 1. 0 is false.


`constants`: fixed value that remains the same for the duration of the program. The constant qualifier specifies that we do not have the right to change the object. In effect, a `const`-qualified type is read-only.

Constants are also called literals. They can be of any data type. Best practice is for them to be uppercase.

```c
const int SIDE = 10; 
// same as:
int const SIDE = 10;
```

`string literals` read-only values. Were they introduced after constants in the language, probably this would have been a better choice.

`enum`: the first value in an enum has value 0, the next 1, and so on. Enumeration constants have either an explicit or a positional value.


`bit pattern`: written like so: `'\000'`:
```c 
#define VTAB '\013'
```

```c
enum color
{ 
    RED, 
    GREEN, 
    BLUE 
};
```
#### Derived data types

##### Aggregated types:

`arrays`: combines items with the same base type.
Arrays can be fixed lenght or variable length (VLA).

VLA's cannot have initializers and VLAs can't be declared outside functions.

Array parameters behave as if the array is passed by reference.

Strings are 'special'. They are a 0-terminated array of `char`.


`structures`: combines items that may have different base types. Omitted struct initializers force the corresponding member to 0. A struct initializer must initialize at least one member. Struct parameters are passed by value. Any data type other than a VLA is allowed as a member in a structure. 

```c
//A typedef only creates an alias for a type, but never a new type.

typedef struct Person Person;
struct Person
{
    char name[25];
    int age;
};
```

Zero initialize all members:
```c
struct Point aPoint = {0};
```

Somtimes, you can also see a `static` as part of a struct definition. In some cases, this is to ensure that the struct is visible to the file in which it is declared. https://stackoverflow.com/questions/7259830/why-and-when-to-use-static-structures-in-c-programming/7259892

##### Other derived types:

`unions`: overlay items of different base types in the same memory location.

`pointers`: refer to an object in memory. They are opaque types and they are valid, null or indeterminate. Initialization or assignment with 0 makes a pointer null. Null pointers evaluate to false.

Takeways:
- pointer points to something by pointing to a location in memory. 
- the thing a pointer points to is the thing that is found at that memory location.
- pointers have specific properties for the following types:
  - structures
  - arrays
  - functions
- some pointer properties:
  - they are considered scalar values, arithmetic operations are define for them
  - they have state
  - they have a dedicated null state
- a valid pointer refers to the first element of an array of the reference type. This array can be of unknown length
- the length of an array cannot be determined from the value of the pointer, this means that pointers are not arrays
- we have to ensure that pointer variables are always null, unless they point to a valid object that we want to manipulate.
```c
char const* name = 0;
```
- when dereferenced, a pointed-to object must be of the designated type
- A pointer must point to a valid object or one position beyond a valid object or be null.
- never use NULL, it is not safe as it is not the same on every platform
- do not hide pointers in a typedef
- array-to-pointer decay: when A is an array, A[i] and *(A+i) are equivalent. Evaluation of an array A returns &A[0].
- In a function declaration, any array parameter rewrites to a pointer.
- Function pointers must be used with their exact type.
- the function call operator (...) applies to function pointers.
- Pointers can refer to objects and to functions.
- Pointers are not arrays but refer to arrays.
- Array parameters of functions are automatically rewritten as object pointers.
- Function parameters of functions are automatically rewritten as function pointers.
- Function pointer types must match exactly when they are assigned or called

Syntax:
`&` address off operator, returns a pointer type
`*` object off operator. Allow 2 things:
  - declare a pointer value
  - get the value that the pointer is pointing to
`->`: a pointer as the left operand that points to a member of the underlying struct.

```c
a -> some_struct
```

Some operations:
```c
int var = 100;  // value declaration
int  *ip;       // pointer variable declaration


ip = &var;      // store the address value of 'var' in 'ip'

printf("Getting the value of the *ip pointer: %d\n", *ip );

int* ip_2;      // second way to declare an integer pointer
int * ip_3;     // third variable declaration
```

### Functions

Example of a function:

```c
int multiply(int a, int b)
{
    return a * b;
}
```

Function syntax:


_return-type function-name (parameter declarations, if any)_
{
  _declarations_
  _statements_
  _return expression_ 
}

Typically, a return value of 0 implies normal termination. Non-zero values are indicative of some sort of error.

Typical to C is that arguments are passed by "value". Exception to this rule is when an array is used as an argument to a function. Instead of passing in the array, a pointer to the start of the array is made available inside the function.

Use `void` in case:
- the function is to be called with no parameter
- the function does not return a value

Reaching the end of the {} block of a function is equivalent to a return statement without an expression. Reaching the end of a } is only allowed for `void` functions.

The `main()` function is the default entrypoint.

The two main forms for main:
```c
int main(void);
int main(int argc, char* argv[argc+1]);
```
Use EXIT_SUCCESS and EXIT_FAILURE as return values for main.

A pure function has the following two properties:
- there are no effects other then the returned value
- the function return value depends only on the parameters

Express small tasks as pure functions whenever possible.


### memory

C is pass by value. You can (sort of) do pass by reference through the use of pointers.

`malloc`: allocate some memory

```c
b = (char *)malloc(size);
```

C does not include a garbage collector. You have to free the memory yourself using `free`:

```c
free(b);
```




### Compiling

```
gcc 01.c
gcc -o 01.exe 01.c
```


For a shared lib with Python (programm is named `add.c`):
```
gcc -c -fpic add.c
gcc -shared -o libadd1.so add.o
```

With VS 2019 MS build tools:
```
cl main.c
```

## increment and decrement operator

There is a quirck, `++i` and `i++` will increment i by 1 but there is a small difference.

The `++i` will increment _before_ the value is used whereas `i++` will increment _after_ the value is used (same applies to decrement).

```c
int n 5;
x = n++;
```
The value x will be 5 and n will be 6.
```c
int n 5;
x = ++n;
```
The value x will be 6 and n will be 6.

# to check

- valgrind
- jansson 
- cmake 

typedef struct
#define

```
Oh that’s another rule with network code - dynamic memory allocation is a massive no no
Pre-allocate and use allocated memory - dynamic allocation is extremely expensive
```


# Resources

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/

https://www.learn-c.org/


C coding style from Linus:
https://www.kernel.org/doc/Documentation/process/coding-style.rst

https://stackoverflow.com/questions/11182765/how-can-i-build-my-c-extensions-with-mingw-w64-in-python


https://github.com/bagder/libcurl-video-tutorials