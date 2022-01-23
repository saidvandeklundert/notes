package main

import "fmt"

// Struct that defines a Human:
type Human struct {
	Name string
	Age  int
}

// Factory function that constructs a Human and returns it by Value:
func NewHumanValue(name string, age int) Human {
	return Human{name, age}
}

// Factory function that constructs a Human and returns the pointer to it:
func NewHumanPointer(name string, age int) *Human {
	return &Human{name, age}
}

func main() {

	// Declare new human:
	jan := Human{
		Name: "Jan",
		Age:  5,
	}
	// Short declare new human:
	marie := Human{Name: "Marie", Age: 2}
	fmt.Printf("%#v\n", jan)   // main.Human{Name:"Jan", Age:5}
	fmt.Printf("%#v\n", marie) // main.Human{Name:"Marie", Age:2}

	// Check the value and the type:
	fmt.Printf("%v is a %T\n", marie, marie) // {Marie 2} is a main.Human

	// Create new human value using NewHumanValue func:
	anne := NewHumanValue("Anne", 35)
	fmt.Printf("%#v\n", anne) //	main.Human{Name:"Anne", Age:35}

	// Check the new human and it's type:
	fmt.Printf("%v is a %T\n", anne, anne) // {Anne 35} is a main.Human

	// Create new human using NewHumanPointer func:
	said := NewHumanPointer("Said", 35)
	fmt.Printf("%#v\n", said) //	&main.Human{Name:"Said", Age:35}

	// Check the value and the type:
	fmt.Printf("%v is a %T\n", said, said) // &{Said 35} is a *main.Human

	// Construct struct using new:
	p := new(Human)
	fmt.Printf("%v is a %T\n", p, p) // &{ 0} is a *main.Human
	p.Name = "Joe"
	p.Age = 80
	fmt.Printf("%v is a %T\n", p, p) // &{Joe 80} is a *main.Human
	// Construct struct using make:
	q := new(Human)
	fmt.Printf("%v is a %T\n", q, q) // &{ 0} is a *main.Human
	q.Name = "Joe"
	q.Age = 80
	fmt.Printf("%v is a %T\n", q, q) // &{Joe 80} is a *main.Human

}

/*
main.Human{Name:"Jan", Age:5}
main.Human{Name:"Marie", Age:2}
{Marie 2} is a main.Human
main.Human{Name:"Anne", Age:35}
{Anne 35} is a main.Human
&main.Human{Name:"Said", Age:35}
&{Said 35} is a *main.Human
*/
