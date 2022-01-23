Type assertion in Go is trying to assert the type of an interface value's underlying type. When type switches are mentioned, what is meant is a `switch` statement that has various assertions defined for it's cases.
## Type assertion:

A type assertion is written like so:
```go
x.(string)
```

In the previous example, `x` is the variable that refers to an interface type. Using `.(string)` on it, we assert that `x` is of the underlying type `string`. The assertion returns follwing the 'comma OK' idiom:

```go
var x interface{} = "hello"
t, ok := x.(int)
fmt.Println(t, ok)
/*
0 false
*/
```

The previous examples shows a failing assertion. The zero value for the asserted type is returned as well as a `false`.

```go
var x interface{} = "hello"
t, ok := x.(string)
fmt.Println(t, ok)
/*
hello true
*/
```

The previous example shows an assertion that matches the type of the value assigned to the interface. Here, the value of the interface is returned together with `true`.


## Type switch

A type switch is written like so:

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