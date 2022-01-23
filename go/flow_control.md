

How the computer reads the program. For flow control, Go offers the following options:
- if statement
- switch statement
- loop statement
### if

Condition expressions must evaluate to a bool.

```go

if true {...}	

if true {	
} else if true {
} else if true {
} else {	
}
// Example:
var n int = 1000
if n < 100 {
	fmt.Printf("n is < 100")
} else if n < 200 {
	fmt.Printf("n is < 200")
} else if n < 300 {
	fmt.Printf("n is < 300")
} else {
	fmt.Printf("n >= 300")
}

// Test for multiple conditions:
if word == "word" || word == "WORD"{
	fmt.Printf("word or WORD")
}
```

Simple statement, aka short statement, can be used with an if statement.

```go
// 'Normal':
n, err := strconv.Atoi(os.Args[1])
if err != nil {
	//Handle the error
	fmt.Println("Error", err)
	return
}
fmt.Println("We traversed the happy path! Converted number:", n)
// Simple statement:
if n, err := strconv.Atoi(os.Args[1]); err == nil {
	fmt.Println("We traversed the happy path! Converted number:", n)
}
// notice the separator ';', this syntax is required.
// 'err == nil' > condition expression: so if the error is nill, execute what is in the body
```

Important consideration:

- Variables declared in the simple statement are ONLY available inside the if statement (and it's branches).
- beware of shadowing. Using `:=` you might unintentionaly re-declare a new variable instead of assigning a value to an existing one. Use `=` for the latter.



### switch

There are 2 types of switch statemens:
- expression switch statement
- type switch statements


The `case` is like an `if` and the location matters. Cases are evaluated top to bottom. The default case is different, it can be compared to an `else` and it can be placed anywhere. A missing switch expression is equivalent to the boolean value true.

A case can be used to test for multiple conditions.

The values used for case conditions should be unique.

Go automatically converts switch conditions to `if` statements before running.

If constants are used, go will not convert anything. The lookup will be faster.


Basic switch:
```go
func multiply(i int) int {
	return i * 2
}

nrs := []int{1, 2, 3, 4, 5}

// Loop over slice and test item for condition:
for _, nr := range nrs {
	// x is initialized as the return of 'multiply(nr)' and 
	//   right after ;, x is defined as the expression to run the case against
	switch x := multiply(nr); x {
	case 1, 2, 3, 4:
		fmt.Println("Small")
	case 5:
		fmt.Println("5")
	case 6, 7, 8, 9:
		fmt.Println("6, 7, 8 or 9")
	default:
		fmt.Println("big")
	}
}
```

The blank switch:

```go
func someFunc() int {
	return 2
}

switch i := someFunc(); {
case i > 100:
	fmt.Println("Bigger then 100")
case i < 10:
	fmt.Println("Less then 10")
	fallthrough // ignore next case and execute that block also
case i < 100:
	fmt.Println("Less then 100")
case i == 100:
	fmt.Println("100")
default:
	fmt.Println("no match")
}
```

Short switch:

```go
switch i := 9; false {		// short assignment of i and invert the switch condition (true is default)
case i > 100:
	fmt.Println("Surprise match.")
default:
	fmt.Println("no match")
}
// "Surprise match."			< that is the output bc we set the switch condition to false.
```

Type switch example:

```go
// returns the type of the argument:
func typeSwitch(v interface{}) string {
	switch v.(type) {
	case int:
		return "int"
	case string:
		return "string"
	default:
		return "unknown"
	}
}
```

### Loop


Anatomy of a for loop:
```go
// initializer: initializes the loop, e.g. i := 1
// condition: `i <= 3`, bool expression. The loop continues as long as this remains true.
// post: example could be the incdec, e.g. i++

for init; condition; post{
    fmt.Println("yolo")
}
//Note: `i++` is the `IncDec` statement, increments the operand by the untyped constant 1.
```

## 4 kinds of for loop:

### 1: Complete, or 'full', for loop:

```go
for i := 0; i <= 3; i++ {
	fmt.Println(i)
}
/*
0
1
2
3
*/
```

Looping over a slice:

```go
hosts := []string{"1.1.1.1", "2.2.2.2", "3.3.3.3"}
for i := 0; i < len(s); i++ {
    fmt.Printf("%v ", s[i])
}
```
### 2: Condition-only for loop:

Leaving off the initializer and the post statement (increment) makes the for statement behave like a `while` loop.

```go
i := 1
for i < 5 {
	fmt.Println(i)
	i = i + 1
}
```

### 3: infinite loop:

The following goes on forever:

```go
i := 1
for {
	fmt.Println(i)
	i = i + 1
}
```

Use `break` to stop the loop when a certain condition is met. Use `continue` to skip to the next iteration of the loop.

```go
i := 1
for {
	fmt.Println(i)
	i = i + 1
	if i == 2{
		continue
	}
	if i > 5 {
		break
	}
}
```

### 4: For-range statement:

To iterate, or loop over, data structures like slices, use the `for-range` loop. Each time the for loop iterates a compound type, Go copies the value. 

```go
s := []string{"a", "b", "c"}
// loop the slice using range:
for index, value := range s {
	fmt.Println(index, value)
}
// loop the slice using range while ignoring the index:
for _, value := range s {
	fmt.Println(value)
}

// loop a map using range:
m := map[string]int{"a": 100, "b": 200, "c": 300}
for key, value := range m {
	fmt.Println(key, value)
}

// looping a string using range will iterate the RUNES!! and not the bytes:
s := "Hello こんにちは"
for i, value := range s {
	fmt.Println(i, value)
}
/* 
The previous outputs to the following: 
0 72
1 101
2 108
3 108
4 111
5 32
6 12371
9 12435
12 12395
15 12385
18 12399

	"Hello " is 1 byte per character, so we see the index increase by 1 (the index points to the byte).
	The Japanese 'Kon'nichiwa' uses code-points that do not fit in a single byte so you see the index skipping a few.
*/
```








## Other

```go
// loop using range:
for index, value := range l {
	fmt.Println(index, value)
}
// basic loop:
for i := 1; i <= 3; i++ {
	fmt.Printf("word %v\n", i)
}
// if i is already defined, it is not needed:
for ; i <= 3; i++ {
	fmt.Printf("word %v\n", i)
}
// IncDec can be moved into the loop:
for ; i <= 3; {
	fmt.Printf("word %v\n", i)
	i++
}
// For statement with single condition:
for i <= 3 {
	fmt.Printf("word %v\n", i)
	i++
}
// infinite loop:
for {
	fmt.Printf("word %v\n", i)
	i++
}
// infinite loop:
var i int
i = 1
for {
	if i > 3 {
		fmt.Printf("Give me a break\n")
		break // break a loop
	}
	fmt.Printf("word %v\n", i)
	i++
}
/* ^ gives:
word 1
word 2
word 3
Give me a break
*/

// use continue to skip an iteration:
if i%2 != 0 {
	i++			
	continue 
}
// Note 'i++', if the check is against i', we should not forget to increment it.
```

