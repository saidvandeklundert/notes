package main

import "fmt"

func main() {
	// Basic types
	//
	//
	// Define an example for each of the basic types (there are 3):

	// String:
	s := "string"
	// Integer:
	i := 10
	// Bool:
	b := false
	fmt.Println(s, i, b)

	// Define an example for each of the composite aggregate types (there are 2):

	// Array:
	array := [2]string{"a", "b"}
	// Struct:
	type Struct struct {
		Name string
	}
	StructExample := Struct{
		Name: "yolo",
	}
	fmt.Println(array, StructExample)

	// Define an example of each of the composite reference types except for channels (there are 5):

	// Slice:
	Slice := []string{"a", "b"}
	// Map:
	Map := map[string]string{
		"a": "a",
		"b": "b",
	}
	// Pointer:
	Pointer := &i
	// Func defined outside main:
	Hello()
	fmt.Println(Slice, Map, Pointer)

}
func Hello() {
	fmt.Println("Hello")
}
