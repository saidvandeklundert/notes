package main

import "fmt"

type NamedString string

func (s NamedString) DoubleDouble() {
	fmt.Println(s + s)

}

type Person struct {
	Name string
}

// Following passes in a pointer, allowing us to change the state of the struct:
func (p *Person) ChangeName(n string) {
	p.Name = n
}

func main() {
	//
	var x NamedString
	x = "double"
	x.DoubleDouble() // doubledouble
	//
	jan := Person{Name: "Jan"}
	jan.ChangeName("Marie")
	fmt.Println(jan.Name) // Marie

}
