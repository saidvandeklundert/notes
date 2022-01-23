package main

import (
	"fmt"
)

func main() {

	// Make the channel:
	c := make(chan int)

	// send
	go Send(c)

	// recieve
	Rec(c)

	fmt.Println("Finished Send and Rec 1 value.")

	// Do the same thing with 10 Go routines:
	for i := 1; i <= 10; i++ {
		go Send(c)
	}
	for i := 1; i <= 10; i++ {
		Rec(c)
	}
	fmt.Println("Finished Send and Rec 10 values.")
}

// Send func
func Send(c chan<- int) {
	// Send value to channel:
	c <- 50
}

// Receive func
func Rec(c <-chan int) {
	// Pull value off channel and print it:
	fmt.Println(<-c)
}
