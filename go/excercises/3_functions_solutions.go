package main

import "fmt"

/*  1:
Create a function called Multiple.
Take 2 integer arguments.
Return an integer that is the product of the arguments.
*/
func Multiply(a, b int) (c int) {
	c = a * b
	return c
}

/* 2:
Create a struct called Human. Give it a string field called Name.
Outfit the struct with a method that says "Hi, my name is " plus the name.

*/
type Human struct {
	Name string
}

var Jan Human = Human{
	Name: "Jan",
}

func (h Human) Print() {
	fmt.Printf("Hi, my name is %v", h.Name)
}

// Do not change anything below this, you can only uncomment:
func main() {
	c := Multiply(2, 4)
	fmt.Println(c)
	Jan.Print()
}
