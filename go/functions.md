Functions are first-class citizens in Go.



## A basic function:
- is defined with the `func` keyword
- is named
- has input parameters defined
- defines a return

If a function returns something, the `return` keyword must be used. If a function does not return anything, it can be omitted. When a function has no input parameters, we use empty parentheses (`()`). If a function does not return anything, those parentheses can be skipped.

In case multiple input parameters are of the same type, we comma separate the parameters and specify the type once. 

Examples that detail the function basics:

```go
func name() {
	// function body, the code goes here
	fmt.Printf("Running the function.")
}

//function with input and output:
func multiply(a, b int)(c int) {	
	c = a * b
	return c
}

// since c is a named result value, it is returned implicitly: 
func multiply(a, b int)(c int) {	
	c = a * b
	return					// aka naked return: returns the named return values
}

// print the function or store the result in a var:
fmt.Println(multiply(2, 6))
c = multiply(2, 6)

// Mind Go's pass by value, important when dealing with functions that change aggregate values.
// Here is a struct:
type SomeStruct struct {
	Name string
}
// Func that changes struct:
func changeSomeStruct(s SomeStruct) SomeStruct {
	s.Name = "new_name"
	return s
}
// Define struct, print it to screen, change it and print it to screen again:
s := SomeStruct{Name: "name"}
fmt.Printf("struct: %#v\n", s.Name) 	// struct: "name"
s = changeSomeStruct(s)					// pass the struct (s) value and re-assign it to s
fmt.Printf("struct: %#v\n", s.Name)		// struct: "new_name"


// Now the same with a map (map is reference type):
func changeMapping(m map[string]string) {
	delete(m, "a")
	return
}
mapping := map[string]string{"a": "a", "b": "b"}
fmt.Printf("mapping: %#v\n", mapping)		//mapping: map[string]string{"a":"a", "b":"b"}
changeMapping(mapping)
fmt.Printf("mapping: %#v\n", mapping)		// mapping: map[string]string{"b":"b"}
```



## Named and optional paramers

Go does not have named and optional parameters. You can simulate this with a struct

```go
type Kwargs struct {
	Load          bool
	Restart       bool
	Delay         int
	Configuration string
}

func Example(k Kwargs) {
	fmt.Println(k.Load, k.Restart, k.Delay, k.Configuration)
}

// Fill out the func parameters as you call the func with a struct literal:
Example(
	Kwargs{
		Load:          true,
		Restart:       false,
		Delay:         300,
		Configuration: "interface vlan 300",
	},
)
// true false 300 interface vlan 300
```

## Variadic functions

The variadic parameter must be the last or only parameter to the function, prefaced with `...`. The variable is available as a slice of the specified type:

```go
func Example(s ...string) {
	for _, v := range s {
		fmt.Println(v)
	}
}
Example("a", "b", "c")
```

## Multiple return values

```go
func Example() (string, string, error) {
	return "a", "b", nil
}
s1, s2, err := Example()
```

Note that returned values must be assigned to their own variable.

## Ignoring return values

Unused variables are illegal unless you call them `_`:
```go
func Example() (string, string, error) {
	return "a", "b", nil
}
s1, _, _ := Example()
```

## Named returns

You can name the return values. When doing so, the variables are also predeclared:
```go
func Example() (s1 string, s2 string, err error) {
	// named returns are predeclared, hence we use '=' instead of ':='
	s1 = "a"
	s2 = "b"
	err = nil
	return s1, s2, err
}
```

Be mindfull of shadowing with predeclared named returns.

When using named returns, you can also use the naked return statement to return all named return values:

```go
func NakedReturnExample() (s1 string, s2 string, err error) {
	s1 = "a"
	s2 = "b"
	err = nil
	return 
}
```

Naked (aka blank) returns are not considered idiomatic Go.

## Functions are values

Function `signature`: the parameters and return values of a function.

Since functions are values, you can use them as values in composite types. An example of what this could allow you to do is to have a map of functions.

## Anonymous functions

Defined and called inline, no name is given:

```go
func main() {
	aSlice := []string{"a", "b", "c"}
	for _, v := range aSlice {
		func(s string) {
			fmt.Println("Inside anonymous func with arg ", v)
		}(v)
	}
}
/*
Inside anonymous func with arg  a
Inside anonymous func with arg  b
Inside anonymous func with arg  c
*/
```

Two more examples:
```go
// Function literal:
func() {
	fmt.Println("inside the unnamed func")
}

// EXECUTING a function literal:
func() {
	fmt.Println("inside the unnamed func")
}() // <-()
```

## Closures, functions as a parameter and returning functions from functions

Functions declared inside of functions are closures. They allow you to limit a function's scope. The enclosing function provides an environment of it's own to the enclosed function. A way of putting it is saying that closures are statefull functions with their own environment. 

In the example closure, we can also see that a function can be passed as a parameter into a function.

```go
func enclosingFunction(envVar string) func(string) string {
	fmt.Printf("Working in the %v environment\n", envVar)
	return func(innerString string) string {
		return envVar + " " + innerString
	}
}

func main() {
	Amsterdam := enclosingFunction("Amsterdam")
	Tokyo := enclosingFunction("Tokyo")
	fmt.Println(Amsterdam("weather"))
	fmt.Println(Tokyo("weather"))
}
/*
Working in the Amsterdam environment
Working in the Tokyo environment
Amsterdam weather
Tokyo weather
*/
```

Things to notice:
- the outer functions are executed when they are assigned to the variable
- the inner functions can access the outer functions parameters, even though they were not passed in as such
- the inner function is defined as an anonymous function

Let's look at the enclosing function:
```go
func enclosingFunction(envVar string) func(string) string {
```
- `enclosingFunction`: this is the func that is wrapped around the (anonymous) inner function
- `envVar`: this is the environment variable avaiable to the inner function
- `func(string)`: this is the call to the innner function.
- `string`: this is what the inner function returns. 

To better understand it, let's imagine wanting to change the inner function to:
- work with 2 arguments, a string and an int
- return 2 arguments, a string and an int

In that case, we could write the closure like so:
```go
func enclosingFunction(envVar string) func(string, int) (string, int) {

	return func(innerString string, temp int) (string, int) {

		return envVar + " " + innerString, temp
	}
}
func main() {
	// we did not change the outer function:
	// the inner func now takes 2 arguments
	Amsterdam := enclosingFunction("Amsterdam")
	Tokyo := enclosingFunction("Tokyo")
	fmt.Println(Amsterdam("weather", 12))
	fmt.Println(Tokyo("weather", 20))
}
/*
Amsterdam weather 12
Tokyo weather 20
*/
```

You can return a closure from a function. Following prefixer gets passed a string that the inner function uses as prefix to it's own parameter. Few things to notice in the following example:
- the inner function has access to the variables of the enclosing function
- `prefixer` is passed an argument and assigned to a variable
- the variable can then be called as a function 
- when the variable is called as a function, we run the inner function

```go
func prefixer(outer string) func(string) string {
	return func(inner string) string {
		return outer + inner
	}
}

x := prefixer("super")
fmt.Println(x("man"))			// superman
fmt.Println(x("market"))		// supermarket
```

Another example where we should note the following:
- the inner function uses the scope of the outer function.
- the scope will persist as long as the function persists.
- we assign the func to a variable
- when we call the variable, we run the inner func 


```go
func CreateCounter() func() int {
	count := 0
	return func() int {
		count += 1
		return count
	}
}
// create the counter by assigning the
// anonymous function to the counter variable:
counter := CreateCounter()
counter()           // 1
counter()           // 2
counter()           // 3

```

## defer

The `defer` statement is mostly used to ensure temporary resources are properly cleaned up. Examples include closing files and closing network connections.

```go
func CopyFile() {
	f, _ := os.Open("/tmp/dat")
	// doing the things
    defer f.Close()
}
```

You can use multiple defers. The defer statements are run in the reverse order in which they were specified.

Usefull could be understanding that you can defer a func as well as an anonymous func:
```go
func example() {
	defer func() {
		fmt.Println("running the deferred anon func")
	}()
}

example()
```

## Go is call by value

When a variable is supplied as a parameter to a function, Go `always` makes a copy of that value.

```go
type Person struct {
	Name string
}

func changePerson(p Person) {
	p.Name = "Carl"
	fmt.Println(p.Name)
}

func main() {
	jan := Person{Name: "Jan"}
	changePerson(jan)
	fmt.Println(jan.Name)

}
/*
Carl
Jan
*/
```

Notice how inside the `changePerson` function, the name was changed to `Carl`. However, after the function was run, the name of the struct inside `main()` remains the same. This is because when the variable `jan` was passed to `changePerson`, a copy of that value was passed. The original struct remains the same.

This behavior differs for `maps` and `slices` because those reference types. Those types are passed by value as well. Thing is, their value is a pointer.

## Recursion

```go
// Recursion example:
func RecEx(a, b int) (c int) {
	c = a * b
	if c < 100 {
		return RecEx(c, b)
	} else {
		return c
	}
}

RecEx(2, 2)         // 128: returns RecEx 5 x before it is > then 100, then returns c
RecEx(2, 100)       // 200: returns c immediately as it is > then 100
```

## Methods


It is possible to attach a method to almost any type (even functions!):
- can use pointer and receiver values:
  - int
  - array
  - string
  - struct
  - float64
- use receiver values:
  - slice
  - map
  - func
  - chan

The following is an example where a method is implemented on a named type:

```go
type NamedString string

func (s NamedString) DoubleDouble() {
	fmt.Println(s + s)

}
var x NamedString
x = "double"
x.DoubleDouble()		//doubledouble
```

The `(s NamedString)` in `func (s NamedString) DoubleDouble()` is called the reciever. This parameter attaches the function to the type of that parameter.

If the struct passed as a receiver is not used by the method, we can just pass the type. Structs do not need to have any fields defined. A field-less struct can be used as placeholder for methods and interfaces.

Outfitting a struct with methods is more common. Following is an example where we define a struct with a field called `Name`. Additionally, a method to change this field name is implemented:

```go
type Person struct {
	Name string
}

// Following passes in a pointer, allowing us to change the state of the struct:
func (p *Person) ChangeName(n string) {
	p.Name = n
}

jan := Person{Name: "Jan"}
jan.ChangeName("Marie")
fmt.Println(jan.Name) // Marie
```