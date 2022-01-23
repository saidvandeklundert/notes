package main

import "fmt"

// Define a custom type list that is a slice of strings:
type list []string

// Define a func that add the Print method to the list type
// The method should iterate and print all the values in the slice
// additionally, it should return an integer that specifies the number of items in the slice
func (l list) Print(slice []string) (i int) {
	l = append(l, slice...)
	for index, item := range l {
		fmt.Printf("value in index %v: %v\n", index, item)
	}
	return len(l)
}

func main() {
	// make a custom list that contains string values "a", "b" and "c":
	alist := list{"a", "b", "c"}
	// declare the slice that needs to be added to the list. The slice should contain "d" and "e":
	var sliceAddition = []string{"d", "e"}

	// run the iterate function and print the return to screen:
	fmt.Println(alist.Print(sliceAddition))
}
