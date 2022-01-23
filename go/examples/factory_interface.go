package main

import "fmt"

// Struct that defines a human:
type human struct {
	name string
	age  int
}

// interface to human:
type Human interface {
	Introduce()
	Hello()
	TellAge()
	TellName()
}

// interface functions:

func (h *human) Introduce() {
	fmt.Printf("Hi, I am %s and I am %d years old.\n", h.name, h.age)
}

func (h *human) Hello() {
	fmt.Printf("Hello!\n")
}
func (h *human) TellName() {
	fmt.Printf("I am %s.\n", h.name)
}
func (h *human) TellAge() {
	fmt.Printf("I am %d years old.\n", h.age)
}

// :
func NewHuman(name string, age int) Human {
	return &human{name, age}
}

func main() {

	marie := NewHuman("Marie", 2)
	jan := NewHuman("Jan", 5)
	fmt.Printf("%#v is a %T\n", marie, marie) // &main.human{name:"Marie", age:2}
	// Marie says hello:
	marie.Hello()
	// Jan introduces himself
	jan.Introduce()
	// Marie tells her name and age
	marie.TellName()
	marie.TellAge()

}
