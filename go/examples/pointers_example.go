/*
Figuring out how pointers work
*/
package main

import "fmt"

/*
	Struct and functions only assist in clarification.

	Follow main to see the explanation of pointers.
*/

type Person struct {
	name string
	age  int
}

func changeInt(i int) {
	i = i + 200
	fmt.Printf(`
i value in changeInt:					%v
`, i)
}

func changeIntPointer(i *int) {
	*i = *i + 200
	fmt.Printf(`
i value in changeInt:					%v
`, *i)
}

func changeSlice(s []string) {
	s[0] = "A"
	fmt.Printf(`
i value in changeSlice:					%v
`, s)
}

func main() {
	// Declaring values for the basic types:
	var int_value int = 100
	var str_value string = "word"
	var bool_value bool = false

	// Returning the memory address to screen using the & operator:
	fmt.Printf(`
int_value pointer            %v
str_value pointer:           %v
bool_value pointer:          %v
`, &int_value, &str_value, &bool_value)

	// Declaring values for composite types:
	var array_value = [...]int{1, 2, 3, 4}
	struct_value := Person{name: "Marie", age: 2}
	slice_value := []string{"a", "b", "c", "d"}
	dict_value := map[string]string{
		"r1": "juniper",
		"r2": "arista",
		"r3": "cisco",
	}

	// Returning the memory address to screen using the & operator:
	fmt.Printf(`
array_value pointer            %p
human_value pointer:           %p
slice_value pointer            %p
dict_value pointer:            %p
`, &array_value, &struct_value, &slice_value, &dict_value)

	// Returning the memory address of a type inside a composite type:
	fmt.Printf(`
array_value pointer item 0:            %v
slice_value pointer item 0:            %v
struct pointer name value:             %v
`, &array_value[0], &slice_value[0], &struct_value.name)

	// Create pointer variable using &:
	int_pointer := &int_value
	// Change the variabale value through the pointer:
	*int_pointer = 200
	// int_value now changed from 100 to 200:
	fmt.Printf(`
int_value:							%v
*int_pointer:						%v
`, int_value, *int_pointer)

	// Change int_value in a function:
	var int_value_200 int = 200
	fmt.Printf(`
int_value_200:						%v
`, int_value_200)
	// We run the function passing the value of int_value_200:
	changeInt(int_value_200)
	// We can see that the value has not changed:
	fmt.Printf(`
int_value_200 after changeInt:            		%v
`, int_value_200)
	// Now we change the value with a function that takes in the pointer to the integer:
	changeIntPointer(&int_value_200)
	// We can see that the value of int_value_200 in main has also changed:
	fmt.Printf(`
int_value_200 after changeIntPointer:			%v
`, int_value_200)

	// A slice is a reference value and we do not need to pass the pointer to a function to change it.

	// Declare the slice:
	var slice_abc = []string{"a", "b", "c", "d"}
	fmt.Printf(`
slice_abc before changeSlice:				%v
`, slice_abc)
	// pass the slice to the function:
	changeSlice(slice_abc)
	// We can see that the slice has changed in main as well:
	fmt.Printf(`
slice_abc after changeSlice:				%v
`, slice_abc)
}
