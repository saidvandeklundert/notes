# Go

Go was first released 2012. It was developped at Google by Robert Griesemer, Rob Pike, and Ken Thompson. Created with concurrency and parallelism in mind. Additional background information can be found [here](https://github.com/saidvandeklundert/go/blob/main/go_background.md)

## Types in Go

![Go types overview](https://github.com/saidvandeklundert/go/blob/main/img/go_types.png)


**Basic types**:
  - `String types`
  - `Numeric types`
  - `Boolean types`

**Composite types**:
- Aggregation types:
  - `arrays`
  - `structs`
- Reference types:
  - `slices`
  - `maps`
  - `channels`
  - `pointers`
  - `functions`
- Abstract type:
  - `interface`

### Additional type categories in Go:

Reading documentation, code and blogs, the following categorisations also occur:

**Value types**:
- `int`
- `float`
- `string`
- `bool`
- `structs`
- `array`

**Abstract** and **concrete** types:
- **abstract type**: interfaces
- **concrete types**: the rest

**Named**/**defined** and **unnamed**/**undefined** types:
- **named**: type declared with a name
- **unnamed**: type declared without a name by using a type literal

### Additional defitions:

In the context of types, Go oftentimes also mentions the following definitions:

**Underlying type**: Each type (T) has an underlying type. If T is one of the predeclared boolean, numeric, or string types, or a type literal, the corresponding underlying type is T itself. Otherwise, T's underlying type is the underlying type of the type to which T refers in its type declaration.

**Type inference**: variables declared without a specific type have their type inferred from the value on the right.

**Type conversion**: converting one type to another. Example would be `float64(i)`.

**Type definition**: creates a new, distinct type with the same underlying type and operations as the given type, and binds an identifier to it.

## Basic types:

There are the following basic types in Go:
- **String types**: set of string values.
- **Numeric types**: integers, floats, bytes and runes.
- **Boolean types**: true and false.

Defining basic types:

```go
// Declare string with it's 0 value
var a string

// Declare string variable with value 'word'
var Word string "word"				

// Re-assign a value to the Word variable
Word = "new word"					

// Short declare new string variable, have Go infer the type
AnotherWord := "another word"		// := can only initialize values!
```
#### String types:

`string`: a read-only slice of immutable bytes. Strings are utf-8 encoded by default. The zero value is an empty string


More on strings [here](https://github.com/saidvandeklundert/go/blob/main/strings.md).

#### Numeric types:

Numeric integer types:
`int`: integer literals without a fractional part( -2 0 88 )
`int8`: 8 bit integer
`int16`: 16 bit integer
`int32`: 32 bit integer
`int64`: 64 bit integer

All the above also have an unsigned variant ( `uint`, `uint8`, etc.). Unsigned integers can only contain positive numbers.

Numeric floating types:

Floats:
`float32`: integer literals wit a fractional part (-1.7 0. 88.8)
`float64`: integer literals wit a fractional part (-1.7 0. 88.8)

Complex numbers:
`complex64`: two float32's
`complex128`: two float64's

`byte`: can store 8 bits
`uintptr`: unsigned integer type


`aliased types`: aliased for readability:
 - `byte` == `uint8`
 - `rune` == `int32`


Idiomatic Go:
- use `byte` instead of `uint8`
- when choosing what integer to use, always use `int` unless:
  - you are writing a library function
  - you are working with a binary file format or networking protocol that has an integer of s specific size or sign


Don't use a float unless you really need to. In case you need a float, choose `float64`.

The zero value for an int is `0`.
#### Boolean types:

`bool`: pre-declared constant that can be true or false. (1 byte)

The zero value for a bool is `false`.

## Composite types:


**Aggregation types**:

- `arrays`: collection of elements that are indexable.
- `structs`: groups different (related) types

**Reference types**:

- `slices`: collection of elements that are indexable. Has a dynamic length.
- `maps`: collection of indexable key-value pairs.
- `channels`: facilitates communication between Go routines
- `pointers`: stores the memory address of a value
- `functions`: reusabe and organized block of code that performs an action

**Abstract types**:

- `interface`: collection of method signatures

#### arrays:

`arrays`: collection of elements that are indexable. 

Mostly, you interface with the `array` through the `slice`.

The `array` has a fixed length and stores elements of the same type. Array properties include the type of elements stored as well as the lenght of the array. Since the length of the array is a property, it belongs to compile time.

When arrays are copied, the value of the array is copied along with it. The 

Arrays populate contiguous memory locations.
```go
// Array with 10 empty string elements, initiaized to their zero value
var emptyArrayStr [10]string
// Array with 10 empty integer elements
var emptyArrayInt [10]int
// Array literal
var arrayStrings [3]string{"Go", "Go", "Go"}
var arrayStrings [...]string{"Go", "Go", "Go"}  			// no need to specify length when using array-literal
// Arraywith several strings and several empty string elements
var arrayStrings [10]string{"Some", "values", "stored", "in", "the", "array"}
// Shorthand assignment
arrayStringsShort := [10]string{"Some", "values", "stored", "in", "the", "array"}
//Assign strings to an array and iterate the array:
var arrayStrings = [5]string{"Iterating", "an", "array", "in", "Go"}
for index, word := range arrayStrings {
	fmt.Println(index, word)
}
//Assign the order of the strings inside the array:
var arrayStrings = [5]string{
	0: "Iterating",
	4: "Go",
	2: "array",
	3: "in",
	1: "an",
	}
for index, word := range arrayStrings {
	fmt.Println(index, word)
}

```

More on arrays [here](https://github.com/saidvandeklundert/go/blob/main/array.md).
#### slices:

`slices`: collection of elements that are indexable. Has a dynamic length.

An array cannot change it's size. A slice can change in runtime. Additionally, unlike with an array, the length is not part of the slice's type.

A slice is actually a slice header/structure that contains 3 fields:
- pointer to a backing array
- length
- capacity

The slice used in go is defined [here](https://github.com/golang/go/blob/master/src/runtime/slice.go).

Note that the slice header contains a pointer. When a slice is passed to a function, the slice header is copied and passed to the function. The backing array however is not copied. 

![Go slice code](https://github.com/saidvandeklundert/go/blob/main/img/slice.png)

These fields describe it's backing array. 

If a slice is copied, the new value will be allocated a new pointer.

When `append()` is used and the new elements do not fit in the curent backing array, Golang allocates a new backing array and copies current content over.

When you use `make` to declare the slice, you can specify the capacity for the slice. 

Slices are not comparable, you can only compare a slice to it's zero value, which is `nil`.

Example slice:

```go
// An empty slice:
var nums []int	
// An array:
var nums [5]int

// The difference: the array has the length defined
```

Very similar to arrays, but notice that the length is not defined at compile time. The lenght of the slice is not a part of it's type.

Slices can only contain one type of element.

```go
// slice literal:
letters := []string{"a", "b", "c", "d"}
```

When taking a slice of a slice, be midfull of the pitfalls involved. Both slices share the same memory and changes to one slice are reflected in the other slice. Do not modify slices after they have been sliced or if they were produced by slicing. Use a three-part slice expression to prevent append from sharing capacity between slices (`a[low : high : max]`).

Even safer is making a copy of a slice using `copy`.


#### maps:

`maps`: collection of indexable key-value pairs. The map is a hash-table and it's zero value is `nil`. 

They `key` value can be any comparable, or phrased differently, any type that supports the equality operator.

A map variable is a pointer to a map header value in memory. The map header tracks everything related to the map.

When you pass a map value to something (a function for instance), you are only passing the pointer.

When you define a map, you also define a type for the key and a type for the value. Once the type is defined, you are stuck using those types. There is no mixing after this.

Coming from Python, I have always considered the dict as an extremely flexible composite type that can be used to store or represent (almost) any value. Don't let the fact that a map is a key/value in Go fool you. Even though the map type in Go is also a key/value pair, it is a lot less flexible. In case you need a data structure that offers flexibility and that can store many different other types, struct would be a better choice.

### Struct versus Map:

Stuct:
- values can be of different types
- keys do not support indexing
- value type
- during compile time, all fields have to be known
- can store many different properties

Map:
- all keys must be of the same type
- all values must be of the same type
- reference type
- keys are indexed and we can iterate them
- represent a collection of related properties
- not all keys have to be known at compile time

### Maps and slices

Some similarities between maps and slices:
- the zero value for a map is `nil`
- you cannot compare maps
- can use `len` on a map to check the number of k/v pairs in the map
- maps automatically grow in size as you add k/v's


Examples on working with maps [here](https://github.com/saidvandeklundert/go/blob/main/maps.md).

#### structs:

`structs`: groups different (related) types

The struct allows you to define a static blueprint. The field name and field types are defined at compile time. The field values belong to runtime and can change during program execution.

Structs may store different types of data. A zero value struct has every field set to the type's zero values

Structs can contain structs as well.

In OOP, that is inheritence with an "is a" relationship. In Go, there is no inheritence. In Go, go for composition. Go allows for structs to be embeddeded into other structs. The 1 struct 'has-a' struct embedded.


| Slices and maps            | structs                    |
| -------------------------- |:--------------------------:|
| single element type        | different types of fields  |
| Dynamic number of elements | fixed number of fields     |

Since methods can be defined on types, a struct can 'equiped' with methods. To add a method to a struct, you need to create a function that takes the struct as a receiver. This is specified between the `func` keyword and the method name.

Example of a simple struct:

```go
type Person struct {
	Name string
	Age  int
}
```

The above code declares a user-defined type called Person which has an underlying type of the struct literal that comes after that.

```go
var Jan Person		
fmt.Println(Jan)		// { 0}
marie := Person{
	"marie",
	2,
}
fmt.Println(marie)		// {marie 2}
said := Person{
	Name: "Said",
	Age:  35,
}
fmt.Println(said)		// {Said 35}
// Named struct instantiation can be done without specifying all fields.
// Keys not specified will be set to their zero value:
bobba := Person{
	Name: "Bobba",
}
fmt.Println(bobba)		{Bobba 0}
```

Other things too know about structs.

Anonymous structs:

An anonymous struct is like a normal struct, but defined without a name. For this reason, it can’t be referenced elsewhere in code.

```go
newGopher := struct {
	name string
	age  int
}{
	name: "Rob",
	age:  200000,
}
fmt.Println(newGopher.name)		// Rob
fmt.Println(newGopher.age)		// 200000
```

More examples on working with structs [here](https://github.com/saidvandeklundert/go/blob/main/struct.md).

## Declaring variables

The way you declare a variable communicates something on how the variable is being used.

The most verbose way to declare a variable:
```go
var x string = "Go"
```

Declaring a variable and assigning the zero value:
```go
var x string
```

You can declare multiple variables at once with `var`:
```go
var x, y int = 1, 2
```

They can be mixed types:
```go
var x, y = 1, "Go"
```

You can also use a 'declaration' list:

```go
var (
	x    int
	y        = 2
	z    int = 3
	d, e     = 4, "Go"
	f, g string
)
```

Inside functions, you can/should use short-declaration that uses typ-inference:
```go
x := 10
x, y := 10, "Go"		// you can assign values to multiple variables as well as re-assign values to existing ones
```

Idiomatic Go is using short-declarion when possible unless you want to use a zero value of a type or when you need to make it explicit that you are creating and reassigning variables. In that case, use var to create new variables and then use the `=` to assign new values to to both old as well as new values.

As a general rule, only declare package level variables (using var) in case neccessary and only create immutable package level variables.


By convention, naming variables is done using camel case (ex. `numTries`) when a variable consists of multiple words.

The first letter indicates that it is a package level declaration. So unless something is a package level declaration, do not capitalize the first letter.
#### functions:

A composite reference data type as well as a first class citizen in Go. The latter means that a function can be passed as an argument to another function.

Go is a pass by value language. Non-reference types will be copied in memory when the are passed as a value to a function. This applies to receiver values as well as arguments. When these values are copied, they exist only in the scope of that function. In case you need to change the state of a non-reference value outside of the scope of a function, you will need to pass the pointer to that value.

Example function in Go:

```go
//function with input and output:
func multiply(a, b int)(c int) {	
	c = a * b
	return c
}
```

##### Methods

Go supports methods on user defined types.

```
Methods give us this syntactic sugar that a piece of data has behavior. - William Kennedy
```

A method belongs to a type, a function belongs to a package. A method is defined as a function with a reciever argument. The receiver argument precedes the function name:
```go
func (r receiverType) name(s string, i int)(returnString string, returnInt int){
	// We can now work with the receiver in this function
	// the receiver will be of type receiverType
	// we can work with the copy of that type like so: r.attribute
}
```

Example method:
```go
type myString string		// User defined myString that has the underlying type string

// (m myString): Receiver, in this case a value receiver
//			Repeater: function name
//					(x int): function argument
func (m myString) Repeater(x int) {
	for i := 1; i <= x; i++ {
		fmt.Println(m)
	}
}

x := myString("yo")
x.Repeater(3)
/*
yo
yo
yo
*/
```

In effect, this will allow you to run the function/method on the reciever type/object. 

The receiver can be a value receiver or a pointer receiver. If your methods modify the receiver, you _must_ use a pointer receiver. If this is not the case, you can use a value receiver.  

Tips from William Kennedy:
- use value semantics when working with built-in types 
- use value semantics when working with reference types 
  - exception is when a slice or a map is passed down the call stack and to a function that is named decode or unmarshall
- for your own structs, think about what is best suited. When in doubt, choose pointer semantics at first

Example of a pointer and a value receiver:
```go
type Person struct {
	Name string
}

// Pointer receiver:
func (p *Person) NameSetter(n string) {
	p.Name = n
}

// Value receiver:
func (p Person) NamePrinter() {
	fmt.Println(p.Name)
}

jan := Person{"Jan"}
jan.NameSetter("Said")		// Name change will persist because we used a pointer receiver
jan.NamePrinter()			// We can use the value since we do not modify the Person type in any way
/*
Said
*/
```
The above is not idiomatic Go:
- do not use getter or setter methods. Access the fields of a type directly and use methods for the business logic
- try to be consistent in the semantic that you chose, either all value or all pointer recievers

More on functions and methods [here](https://github.com/saidvandeklundert/go/blob/main/functions.md)

#### pointers:

A pointer is nothing more then a variable that contains the location in memory where a value is stored.

In other words, pointers store the memory address of a value. There is a pointer-type for every type, this includes user-defined types. Every time you declare a new type, you get a pointer-type with it. All pointers have the same 2 characteristics:
- pointers start with a `*`
- pointers are 4 bytes on 32-bit architectures and 8 bytes on 64-bit architectures

The zero value for a pointer is `nil`. Slices, maps and functions, implemented using pointers, also have a zero value of `nil`. 

Go is `pass by value`, with the main benefit being readability. When a type is passed to a function, the function will not operate on that data. Instead, it will create a copy and use that copy inside the body of the function. This gives us a certain amount of isolation and immutability. 

When we pass a pointer to a function, Go is still doing it's `pass by value` thing. However, in the case of a pointer, the value is pointing to the address in memory where the original data is found. This means it is now possible to change the value of the original data inside the function.

It is possible to pass a pointer for primitives (int, float, byte, string, rune & bool) or structs to a function. An example of when you would want to do this is when you want to change a struct and have that change persist untill after the function is completed.

There are 2 important operators for working with pointers in Go:
- `*`: indirection operator (or dereferencing operator)
- `&`: address operator

When we pass a pointer to a func, it is important to understand we need to derefence it in case we want to alter the value to which the pointer is pointing to. 

In case we do not dereference the pointer when we attempt to change it, but simply change the value, we are not touching the pointed-to value. Instead, we merely alter the value of the pointer in memory.

```go
func updateFail(p *int) {
	x := 20
	p = &x		// here we change the value of the pointer
}

func updateProper(p *int) {
	*p = 20		// here we dereference the pointer and set the value of what *p points to
}
func main() {
	x := 10
	updateFail(&x)
	fmt.Println(x)		// 10
	updateProper(&x)
	fmt.Println(x)		// 20
}
```

##### *

`*` is known as the dereferencing operator. It has two use-cases:
- It can be used to access the value stored in the address: 
```go
*integerPointer 	// returns the value that the address refers to
```
- It can be used to declare a pointer variable:
```go
var PointerInteger *int
```

##### &

When reading `&`, think 'address of'. The `&` is known as the address operator and it generates a pointer to it's operand.

```go
x := "Good morning"
ptrTox := &x
```


Another shorthand:
- turn `address` into `value` with `*address`
- turn `value` into `address` with `&value`

And:
- if `*` is used where you would declare a type, it is used to indicate we are working with a pointer
- if `*` is used as an operator, it is used to work with the value that the pointer is referencing

For function returns, always favor values over pointers. Use pointers in case state within the type is subject to change. Some additional advice from [William Kennedy](https://www.ardanlabs.com/blog/2017/05/language-mechanics-on-stacks-and-pointers.html):
```
If the word “share” doesn’t come out of your mouth, you don’t need to use a pointer. When learning about pointers, it’s important to think using a clear vocabulary and not operators or syntax. So remember, pointers are for sharing and replace the & operator for the word “sharing” as you read code.
```

Example:
```go
increment(&count)	// the & operator is saying 'I am sharing the count variable with the increment function'
```

For function parmeters, favor values over pointers. Use pointers when you want to permanently alter state in a type. Caveat may be when you are working with very big structs (Megabytes at least). In those cases, it may make sense to use pointers because copying over a large struct takes more time when compared to copying over a pointer.


Note:

Maps and slices are reference values. When you pass them to a function and the function alters them, the changes persist.

There is a subtle difference between a map and a slice that may bite. A map is a pointer to a struct. Any and all changes made to a map that is passed to a function persists.

A slice is a struct that contains a pointer to a backing array, a length and a capacity field. Changes to the backing array will persist, but if the slice grows in lenght or capacity, those changes are made to the COPY of the struct that is passed into the function!

More on pointers [here](https://github.com/saidvandeklundert/go/blob/main/pointers.md).

#### channels (and Go routines):

In the context of Go, the following terms are important:
- `Goroutines`: User-space thread managed by the Go runtime. The thread is not managed by the OS. Goroutines are used to execute tasks independently.
- `Channels`: reference type that is used for communication and synchronization between Goroutines.
- `Go scheduler`: multiplexes Goroutines onto OS threads.

`Channels`:
- are Goroutine-safe
- store and pass values between Goroutines
- provide FIFO semantics (when they are buffered)
- can cause Goroutines to block and unblock

The zero value for a channel is `nil`.

More on channels, Goroutines and concurrency [here](https://github.com/saidvandeklundert/go/blob/main/concurrency_and_parallelism.md).

## Abstract types

#### interfaces:

All types are concrete types, except the interface type. The interface type is an abstract type and unlike with a concrete type, we cannot directly use an interface type to create a value.

Interfaces can be usefull in case a method does something that can be re-used for a variety of objects. Interfaces in Go are oftentimes explained as something that is used to define a behavior, like printing, writing etc.

You can create a variable that is an interface type and that has the methods that belong to the interface. This makes the method a custom type as well as a collection of methods.

Interfaces are implicit. We do not manually define the correlation between the interface custom type and the other methods and functions.

Interfaces can be seen as a contract to help manage types. The Go compiler will check all the values and the returns involved, but (obviously) will not check if the logic that is used is sound.

More on interfaces [here](https://github.com/saidvandeklundert/go/blob/main/interfaces.md).

## Go syntax

### Variables

Typing is everything in Go. Imagine the following:
```
00001010
```

What the above byte means in a Go program can only be understood if the type has been declared.

```go
// Delare variables and set them to their 0 value:
var a string
var b int
var c float64
var d bool

// Declare and initialize variables with short declaration operator:
aa := "string"
bb := 3
cc := 3.14
dd := false

// short declaration operator sometimes referred to as 'productivity operator'
// Does inference. Productivity operator can be used inside a function only

// assign a pre-declared variable
a = "string"

// defining a literal means defining a var together with all the values:
var someString string = "word"

// variable conversion
n := 44
f := float64(n)

// anonymous, or nameless, definition:
```

## Operators

### Comparison operators:

Logical operators combine bool expressions and yield a bool value.

```go
// Logical AND operator:
true && true				// true: when all operands are true

// Logical OR operator:
false || false				// false: one must be True for the expression to be True

// Logical NOT operator:
// If the expression is True, it returns False. If the expression is False, it returns True:
!false						// true
!!false						// false
```


```go
true == true		// true
true != true		// false
```

If a value with a type is not assignable to a variable, then that value cannot be compared with it either.

```go
integer, float := 100, 10.0
integer > float				// not possible!
integer > int(float)		// true, possible since the float is converted
```
### Ordering operators:

```go
1 < 2		// true
2 > 3		// false
2 >= 2		// true
3 <= 2		// false
```

### Comparison operators:

```go
==	// equal to
!=	// not equal to
<	// less than
<=	// less than or equal to
>	// greater than
>=	// greater than or equal to
```

Note: all values of basic types are comparable if they are of the same type.

### Bitwise binary operators:

```go
&	// bitwise AND
|	// bitwise OR
^	// bitwise XOR
&^	// bit clear (AND NOT)
<<	// left shift
>>	// right shift
```

## Flow control

For flow control, Go offers the following options:
- if statement
- switch statement
- loop statement

More on flow control [here](https://github.com/saidvandeklundert/go/blob/main/flow_control.md).


## Error handling

Convention in Go is to return an error as the last return value for a function. When a function executes as expected, the error parameter is returned with a `nil` value. If an error occurs, the error value is returned instead. The other parameters of the function should, by convention, return their zero value.

The `error` in Go is defined as follows:

```go
type error interface {
	Error() string
}
```

Note that an error is an interface. As such, returning `nil` is a valid value for one and it explains the convention as to why it is used to indicate 'no error'. Namely, `nil` is the zero value for an interface.

The `error` interface method, `Error()`, specifies a `string` is returned. 

The following is an example where an error is raised inside a function:
```go
func exampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", errors.New("s was to short")
	} else {
		return s, nil
	}

}
```

We can also raise and format errors using a convenient `fmt` function, like so:

```go
func exampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", fmt.Errorf("length of s should be > 6, it was %d", len(s))
	} else {
		return s, nil
	}
}
```

More on error handling [here](https://github.com/saidvandeklundert/go/blob/main/error_handling.md).

## Type assertion and type switches:

Type assertion in Go is trying to assert the type of an interface value's underlying type. 

The assertion is written like so:
```go
x.(string)
```
When type switches are mentioned, what is meant is a `switch` statement that has various assertions defined for it's cases, like so:

```go
func typeSwitch(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Printf("Integer value is %d\n", v)
	case string:
		fmt.Printf("String value is %s\n", v)
	default:
		fmt.Printf("No case statement for %T!\n", v)
	}
}

func main() {
	typeSwitch(21)
	typeSwitch("hello")
	typeSwitch(true)
}
/*
	Integer value is 21
	String value is hello
	No case statement for bool!
*/
```

More on type assertions and type switches [here](https://github.com/saidvandeklundert/go/blob/main/type_assertion_and_type_switches.md)

## Other

`defer`: a statement that defers execution of a function until the surrounding function returns.

From Golang tour:
```go
func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```

## Testing in Go

To make a new test, crate a file that ends with `_test.go`.

Running all tests in a package, run the command `go test`.

Example test for pakage main:

```go
package main
func TestSlice(t *testing.T) {
	if len(Slice) != 3 {
		t.Errorf("Slice range expected 20, got %d", len(Slice))
	}
	if Slice[0] != "a" {
		t.Errorf("First item should be 'a', got %s", Slice[0])
	}
}

```


When it passes:
```
 go test
PASS
ok      
```

Got tests doesn't do any cleanup. In case you are creating files or altering state in one way or another, you need to make sure to clean up after yourself.
  

## Constants

Constants belong to compile time. They can only hold values that the compiler can figure out at compile time.

Constant values are effectively immutable, you cannot change the value of a constant in runtime.

Constants are declared like variables, but with the const keyword you cannot use the `:=` syntax. You must initialize a constant to a value.

Constants can be assigned the following values:
- numeric literals
- true and false
- strings
- runes
- built-in functions `complex`, `real`, `imag`, `len` and `cap`
- expressions that consist of operators and the preceding values

Untyped constants take the type from their context. Leaving a constant untyped will give you greater flexibility.

```go
// untyped constants / aka typeless constant
const u_integer = 123
const u_float = 1.2

// typed constants
const t_integer int = 123
const t_float float64 = 1.2

// expressions can be used when initializing constants:
const second = 1
const minute = 60 *second
```

## The Go runtime

The Go runtime provides a number of services:
- built-in types and functions (example, the `slice` and the `append` function)
- networking
- concurrency
- garbage collection
- memory allocation

The Go runtime is compiled into every binary. This makes it easy to distribute Go programs and avoid worries over whether or not you will be able to run a program on a system after it was compiled.

To clarify, because of the Go runtime, there is no need for a VM that runs the code (like in Java) and Go does not need to be installed on the system that executes the compiled program.

## Blocks

The following blocks can be identified in Go:
1. universe block: all Go source text.
2. package block: all Go source text for that package.
3. file block: all Go source text in the file.
4. Each "if", "for", and "switch" statement is considered to be in its own implicit block.
5. Each clause in a "switch" or "select" statement acts as an implicit block.

[Source](https://golang.org/ref/spec#Blocks).
## Shadowing

A variable is shadowing another variable when it overrides the variable in a more specific scope:

```go
x := 100
if x > 50 {
	fmt.Println(x)		
	x := 1				// Shadowing x right here
	fmt.Println(x)
}
fmt.Println(x)
/*
100
1
100
*/
```

In the previous example, x was shadowed in the `if` block. The value assigned inside the block disappears after the block is executed.

## Go Garbage collector

Garbage is data that has no more pointers pointing to it. That data should be freed up again to be reused. This is what the garbage collector does, clear out the garbage. Go has a garbage collector that does all the work for you, But it is still work that needs to be done.
## Stack and heap

[Understanding Allocations: the Stack and the Heap - GopherCon SG 2019](https://www.youtube.com/watch?v=ZMZpH4yT7M0)

Notes from C (need to find good Go resources):

heap:			variable in size, can be used as per need of developer
stack:			function calls and local variables
static/global: 	global variables
code/text: 		stores instructions

stack, static and code memory does not grow.

### Heap

[William Kennedy](https://www.ardanlabs.com/blog/2017/05/language-mechanics-on-escape-analysis.html) on heaps:
```
The heap is a second area of memory, in addition to the stack, used for storing values. The heap is not self cleaning like stacks, so there is a bigger cost to using this memory. Primarily, the costs are associated with the garbage collector (GC), which must get involved to keep this area clean. When the GC runs, it will use 25% of your available CPU capacity. Plus, it can potentially create microseconds of “stop the world” latency. The benefit of having the GC is that you don’t need to worry about managing heap memory, which historically has been complicated and error prone.

Values on the heap constitute memory allocations in Go. These allocations put pressure on the GC because every value on the heap that is no longer referenced by a pointer, needs to be removed. The more values that need to be checked and removed, the more work the GC must perform on every run. So, the pacing algorithm is constantly working to balance the size of the heap with the pace it runs at.
..


Value semantics keep values on the stack which reduces pressure on the GC. However, there are different copies of any given value that must be stored, tracked and maintained. Pointer semantics place values on the heap which can put pressure on the GC. However, they are efficient because there is only one value that needs to be stored, tracked and maintained. The key is using each semantic correctly, consistently and in balance.
```
### Stacks

[William Kennedy](https://www.ardanlabs.com/blog/2017/05/language-mechanics-on-stacks-and-pointers.html) on stacks:
```
When your Go program starts up, the runtime creates the main goroutine to start executing all the initialization code including the code inside the main function. A goroutine is a path of execution that is placed on an operating system thread that eventually executes on some core. As of version 1.8, every goroutine is given an initial 2,048 byte block of contiguous memory which forms its stack space. This initial stack size has changed over the years and could change again in the future.

The stack is important because it provides the physical memory space for the frame boundaries that are given to each individual function. 
```


### Frames

Stack is divided into frames. Function calls are alloted their own frame. 

[William Kennedy](https://www.ardanlabs.com/blog/2017/05/language-mechanics-on-stacks-and-pointers.html) on Frame Boundaries:
```
Functions execute within the scope of frame boundaries that provide an individual memory space for each respective function. Each frame allows a function to operate within their own context and also provides flow control. A function has direct access to the memory inside its frame, through the frame pointer, but access to memory outside its frame requires indirect access. For a function to access memory outside of its frame, that memory must be shared with the function. The mechanics and restrictions established by these frame boundaries need to be understood and learned first.
```

If more memory then what is available to the stack is required, the program crashes in a stack overflow.

Memory in the heap is controlled by the developper. It can be requested and released.

The stack is a consecutve block of memor

## nil

Nill is a predeclared identifier. Could be read as 'not yet initialized'. It is like Python's `None`.

Nil is the zero value for the following types:
- pointers
- slices
- maps
- interfaces
- functions
- channels

Note that an error is an interface. As such, nil is a valid value for one and it is used to represent 'no error'.


## Ardan labs gotraning repo:

[Latency numbers every programmer should know](https://github.com/ardanlabs/gotraining/tree/master/topics/go/language/arrays#industry-defined-latencies)

# Golang repo

Golang repo is found [here](https://github.com/golang/go).


Go comes with a standard library:
- [documentation](https://golang.org/pkg/)
- [source](https://github.com/golang/go/tree/master/src)



# Go to source and play from your editor

Additional information on a function will appear when you hoover over it. Clicking on the info will offer the option to follow the link to the docs:
![Go to source and play](https://github.com/saidvandeklundert/go/blob/main/img/go_to_source_and_play_1.png)

The docs offer a brief description of the function. Clicking on `Example` will reveal additional information:
![Go to source and play](https://github.com/saidvandeklundert/go/blob/main/img/go_to_source_and_play_2.png)

The full information on the `Println` func looks like this:
![Go to source and play](https://github.com/saidvandeklundert/go/blob/main/img/go_to_source_and_play_3.png)

There are three links here. First is the link to the source code, by clicking on the func name:
![Go to source and play](https://github.com/saidvandeklundert/go/blob/main/img/go_to_source_and_play_4.png)

Additionally we have `Share` and `Run`. Run will run the code in the browser and share will take you to the [Go Playground](https://play.golang.org/):
![Go to source and play](https://github.com/saidvandeklundert/go/blob/main/img/go_to_source_and_play_5.png)



Inspiriation for these notes came from:
- Learning Go
- Go in action
- `GopherCon 2017: Kavya Joshi - Understanding Channels`
- `GopherCon 2018: Kavya Joshi - The Scheduler Saga`
- ['pointers'](https://youtu.be/sTFJtxJXkaY)
- [The Go Programming Language Specification](https://golang.org/ref/spec)