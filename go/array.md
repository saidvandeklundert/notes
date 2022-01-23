Arrays are stored in contigous blocks of memory. 

They are fast and mostly, you'll interface with them through slices.

Though a slice is a type of it's own, every slice actually refers to an array. This array is usually called the backing-array.

```go
// Declare integer array set to it's zero value:
var array [10]int

// Delcaring an array literal:
array := [5]int{10, 20, 30, 40, 50}

// Using ... Go will identify the length for you:
array := [...]int{10, 20, 30, 40, 50, 60}

// Iterate the array using VALUE semantics:
for i, item := range  array {
    fmt.Println(i, item) // We operate on a copy of the array
}

// Iterate the array using POINTER semantics:
for i := range array {
    fmt.Println(array[i])
}

// elipsis sets the array length based on the items assigned to it
var arrayStrings = [...]string{"Iterating", "an", "array",}

// Arrays can be multidimensional:
servers := [2][2]string{
	[2]string{"container-1", "ubi"},
	[2]string{"container-2", "centos"},
}
// Multidimensional arrays are better defined using the elipsis and declaring the type only once:
servers := [...][2]string{
	{"container-1", "ubi"},
	{"container-2", "centos"},
}
```

[arrays](https://github.com/ardanlabs/gotraining/tree/master/topics/go/language/arrays)