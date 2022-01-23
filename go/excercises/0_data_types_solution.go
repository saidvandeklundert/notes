package main

import "fmt"

func main() {
	// Basic types
	//
	// Define a string (String), an integer (Int) a float64 (Float) and a bool(Bool):
	String := "string"
	Int := 10
	Float := 15.5
	Bool := false

	fmt.Printf("%T is %v\n%T is %v\n%T is %v\n%T is %v\n", String, String, Int, Int, Float, Float, Bool, Bool)

	// Reference types:
	// Define a slice containing "a", "b", "c"
	var Slice = []string{"a", "b", "c"}

	// Define a map that maps a, b, and c to 1,2 and 3.
	Map := map[string]int{
		"a": 1,
		"b": 2,
		"c": 3,
	}

	fmt.Printf(`
%T is %v
%T is %v
`, Slice, Slice, Map, Map)
	// Create a pointer to the integer 'intPointer':
	var intPointer = &Int

	fmt.Printf(`
intPointer is a %T

The memory address of the pointer is %v
The memory address of the value is %v
The value is %v

`, intPointer, &intPointer, intPointer, *intPointer)
	// Change the value of the pointer through the pointer:
	*intPointer = 1000
	// Assign the new value to a new variable and print it:
	newInteger := *intPointer
	fmt.Println(Int, newInteger)
	// Composite or aggregation types:
	//
	// Define an empty array with room for 10 elements:
	var Array [10]string
	// Put "hello" in the second element and world in the 10th element
	Array[1] = "hello"
	Array[9] = "world"
	fmt.Println(Array)
	// Create a struct called 'Human'.
	// The fields that are required are the following:
	// name: string					Jan
	// age: integer					35
	// children: slice				Joe, Anne
	// Favorites: mapping			Color: blue, Food: pizza
	// ContactInfo: struct
	//	- email, string				jan@yolo.com
	//	- phone number, string		06121345678
	//
	type Contact struct {
		Email string
		Phone string
	}
	type Human struct {
		Name        string
		Age         int
		Children    []string
		Favorites   map[string]string
		ContactInfo Contact
	}

	Jan := Human{
		Name:     "Jan",
		Age:      35,
		Children: []string{"Joe", "Anne"},
		Favorites: map[string]string{
			"Color": "blue",
			"Food":  "pizza",
		},
		ContactInfo: Contact{
			Email: "jan@yolo.com",
			Phone: "06121345678",
		},
	}
	/*
		JansContactInfo := Contact{
			Email: "jan@yolo.com",
			Phone: "06121345678",
		}
	*/
	// Print the type, the value and the Go-syntax for this struct:
	fmt.Printf(`
	It is a %T
	The value is %v
	The syntax is %#v
	`, Jan, Jan, Jan)

	// Create and run a function that prints hello world
}
