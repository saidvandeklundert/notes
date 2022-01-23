package main

import (
	"fmt"
)

func main() {
	// Channels can be made unidirectional.

	c := make(chan int) // Bidirectional channel

	// Launches go routine:
	go func() {
		c <- 50
	}()

	// Next line pulls the value off the channel:
	fmt.Println(<-c)
	fmt.Printf("\n%T", c)

	// Directional channels:
	rc := make(<-chan int) // Receive channel
	sc := make(chan<- int) // Send channel
	go func() {
		sc <- 50
	}()

	fmt.Printf("\n%T\n%T", rc, sc)
}
