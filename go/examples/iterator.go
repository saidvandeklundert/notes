// Example of an iterator
package main

import "fmt"

type Human struct {
	name, surname, eyeColour, hairColour string
}

// Struct method: turn struct fields into an Array ( Arrays are iterable):
func (h *Human) Properties() [4]string {
	return [4]string{h.name, h.surname, h.eyeColour, h.hairColour}
}

// using generator:
func (h *Human) PropertiesGenerator() <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		out <- h.name
		if len(h.surname) > 0 {
			out <- h.surname
		}
		out <- h.eyeColour
		out <- h.hairColour

	}()
	return out
}

func main() {
	// Construct Human:
	marie := Human{"Marie", "van de Klundert", "brown", "brown"}
	// Iterate the properties of the Human Marie using the Properties func:
	for _, property := range marie.Properties() {
		fmt.Println(property)
	}
	//
	for property := range marie.PropertiesGenerator() {
		fmt.Println(property)
	}
}
