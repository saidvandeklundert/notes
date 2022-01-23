package main

import "fmt"

//
// 1 define example structs that will all implement the same behavior
// 2 define the methods
// 3 define the interface
// 4 define instances of the structs
// 5 run the method

// 1
type Person struct {
	Name string
}

type ConfidentPerson struct {
	Person
}

type LoudPerson struct {
	Person
}

type SoftSpokenPerson struct {
	Person
}

// 2

func (cp ConfidentPerson) Speak(s string) {
	fmt.Println("Speaks with a confident voice: ", s)
}

func (lp LoudPerson) Speak(s string) {
	fmt.Println("Speaks with a loud voice: ", s)
}

func (sp SoftSpokenPerson) Speak(s string) {
	fmt.Println("Speaks with a soft voice: ", s)
}

func (cp ConfidentPerson) Greet(s string) (g string) {
	g = fmt.Sprintf("Greets with a soft voice: %s", s)
	return g
}

func (lp LoudPerson) Greet(s string) (g string) {
	g = fmt.Sprintf("Greets with a soft voice: %s", s)
	return g
}

func (sp SoftSpokenPerson) Greet(s string) (g string) {
	g = fmt.Sprintf("Greets with a soft voice: %s", s)
	return g
}

func (cp ConfidentPerson) Sleep() {
	fmt.Println("zzzzzzzzzzzzzzzzzzzz")
}

func (lp LoudPerson) Sleep() {
	fmt.Println("zzzzzzzzzzzzzzzzzzzz")
}

func (sp SoftSpokenPerson) Sleep() {
	fmt.Println("zzzzzzzzzzzzzzzzzzzz")
}

// 3
type HumanBehaviors interface {
	Speak(s string)
	Greet(s string) (g string)
	Sleep()
}

// 4
func programAgainstTheInterface(h HumanBehaviors) {
	h.Sleep()
	h.Greet("Hello.")
	h.Speak("Thus spoke the interface.")

}

func main() {
	// 5 define instances of the structs

	confidentDave := ConfidentPerson{
		Person{
			Name: "Dave",
		},
	}
	silentBob := SoftSpokenPerson{
		Person: Person{
			Name: "Bob",
		},
	}
	loudLarry := LoudPerson{
		Person{
			Name: "Larry",
		},
	}
	// 6 run the method
	// using the interface:
	confidentDave.Speak("charge")
	silentBob.Speak("talk talk talk")
	g := silentBob.Greet("Hello there.")
	fmt.Println(g)
	silentBob.Sleep()
	loudLarry.Speak("WOW THIS IS AMAZING!")

	// Assign the interface to a variable:
	var h HumanBehaviors
	h = silentBob
	h.Sleep()
	h.Greet("Hello there.")
	h.Speak("The advantage here is that you can use the interface methods.\n You can do so without being able to access or change the underlying values.")

	// Verifying that the interface is implemented:
	//fmt.Printf("%T\n%T\n%T", silentBob, confidentDave, loudLarry)
	h = silentBob
	t, ok := h.(interface{ HumanBehaviors })
	fmt.Printf("t: %v ok: %v", t, ok)
	h = confidentDave
	t1, ok1 := h.(interface{ HumanBehaviors })
	fmt.Printf("t1: %v ok1: %v", t1, ok1)
	h = loudLarry
	t2, ok2 := h.(interface{ HumanBehaviors })
	fmt.Printf("t2: %v ok2: %v", t2, ok2)
	/*

			To see this fail, comment out a method.

			For example, comment out the LoudPerson Greet method.
			 You will notice the following error as you attempt to run the script:


		.\interfaces.go:112:4: cannot use loudLarry (type LoudPerson) as type HumanBehaviors in assignment:
		        LoudPerson does not implement HumanBehaviors (missing Greet method)
	*/
	// 7
	programAgainstTheInterface(silentBob)
	programAgainstTheInterface(loudLarry)

}
