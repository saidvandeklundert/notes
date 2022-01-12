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

`Statements`: instructions that tell the compiler what to do with identifiers that have been declared so far. 

`Include files`:

`Header files`:

`Scope`: part of a program where an identifier is visible.

The C standard: https://stackoverflow.com/questions/81656/where-do-i-find-the-current-c-or-c-standard-documents

`Cast`: converting one datatype into another. Also known as type casting or type-conversion. Type conversions can be implicit (performed by the compiler) or explicit (use of the cast operator). A cast operator consists of a type name, in parentheses:

```c
int people = 4;
double x = (double)people;
```

`Operators`: +, != etc.
`Operands`: things that operators are applied to.


`Abstract state machine`: the compiler can compute away a lot of nonesense at compile time to make the program faster at runtime. Programs execute as if following the abstract state machine. Abstract state machines cheat wherever they can and only respect the observable states of the abstract state machine.

Another thing worth noting is that type determines optimization opportunities.

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

##### Other derived types:

`pointers`: refer to an object in memory. They are opaque types and they are valid, null or indeterminate. Initialization or assignment with 0 makes a pointer null. Null pointers evaluate to false.
`unions`: overlay items of different base types in the same memory location.

### Functions

Example of a function:
```c
int multiply(int a, int b)
{
    return a * b;
}
```

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



# to check

- valgrind
- jansson 
- cmake 

typedef struct
#define




# Resources

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/

https://www.learn-c.org/
