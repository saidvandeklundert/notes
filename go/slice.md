The slice is the most important go to data type in Go.

The slice is a reference type.

It is designed to stay on your stack. The slice is 24 bytes in size and has only 3 fields:
- pointer to a backing array
- length
- capacity

Slices are not comparible. You can only compare a slice with `nil`, which is the slice's zero value.

```go
// Various ways to create a slice:

// Zero value slice (nil):
var aSlice []string                 // aSlice == nil: true.
// Create an array with 10 elements holding the int zero value and return the slice for it:
eSlice := make([]int, 10)           // len(eSlice): 10
eSlice := make([]int, 10, 20)		// specify a length of 10 and a backing array of 20
// Slice literal:
bSlice := []bool{true, true, false}    

var x = []int{1, 5: 4, 6, 10: 100, 15}

// Slice literal:
slice := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

len(slice)          // return lenght of the slice: 11
cap(slice)          // return the size of the slice backing array

// copy will copy the backing array as well.
// The copy function copies as many values as it can from source to destination, limited by whichever slice's length is smaller.
// Capacity is not relevant here.
newS := make([]int, 11)
copy(newS, slice)       // [0 1 2 3 4 5 6 7 8 9 10]            
newS := make([]int, 2)
copy(newS, slice)       // [0 1]
newS := make([]int, 20)         
copy(newS, slice)       // [0 1 2 3 4 5 6 7 8 9 10 0 0 0 0 0 0 0 0 0]  
// copy(to, from), the 'to' value will be a new instance with a new pointer: 


// Slicing: slice[start(including):stop(NOT including)]
// example slice: [0 1 2 3 4 5 6 7 8 9 10 0 0 0 0 0 0 0 0 0]
slice[1]            // 1
slice[2:6]          // [2 3 4 5]
slice[3:]           // [3 4 5 6 7 8 9 10]
slice[:7]           // [0 1 2 3 4 5 6]

// For the second value, consider thinking about how long of a slice you would like.
// Then add that to the start value.
// Exampe, starting at index 2, wanting a slice with a length of 4:
// 2 + 4 = 6, slice[2:6]

// You can supply a third parameter to a slice to indicate the capacity:
slice[2:6:4]

// This limits the size of the new slice. 
// If things are appended, a new backing-array is created and the 'old' slice is left intact.

// For loop a slice:
for _, nr := range slice {
	fmt.Println(nr)
}

// Appending:
Slice := []string{"a", "b"}
Slice = append(Slice, "c", "d")             // [a b c d]
SliceAddition := []string{"e", "f"}     
Slice = append(Slice, SliceAddition...)     // [a b c d e f]

// Joining (strings):
Joined := strings.Join(Slice, ", ")         // a, b, c, d, e, f (string)


// Write slice to disk:
Slice := []string{"a", "b", "c"}
func saveFile(fileName string, slice []string) {
	stringSlice := strings.Join(slice, ",")
	ioutil.WriteFile(fileName, []byte(stringSlice), 0666)
}
saveFile("test.txt", Slice)     // cat test.txt: a,b,c

// Reading the same file from disk:
byteSlice, err := ioutil.ReadFile("test.txt")
if err != nil {
	os.Exit(1)
}
text := string(byteSlice)
fmt.Println("File content:", text)
s := strings.Split(text, ",")        // strings.Split returns slice. s: []string

// Multidimensional slice:
var x [][]int

// The following appends after the 2 zero values in the slice
newS := make([]int, 2)
newS = append(newS, 10)		// [ 0, 0, 10]

// you can create a non-nill slice with capacity and 0 length:
newS := make([]int, 0, 10)
newS = append(newS, 10)		// [ 10 ]
```



## Slices as buffers

Go has a garbage collector that does all the work for you, but it is still work that needs to be done. You can save the garbage collector some work by declaring a slice of bytes once and re-use that as a buffer when we read data from a source. This avoids unneeded allocations.