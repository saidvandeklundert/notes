package main

import (
	"fmt"
	"time"
)

func main() {

	// Make the channel:
	c := make(chan int)
	fmt.Printf("%T %p", c, &c)
	go Send(c)

	for i := 1; i <= 10; i++ {
		Rec(c)
	}
	fmt.Println("Finished Send and Rec 10 values.")
}

// Send func
func Send(c chan<- int) {
	time.Sleep(5 * time.Second)
	// Send value to channel using a for loop:
	for i := 0; i < 10; i++ {
		c <- i
	}

	close(c)
}

// Receive func
func Rec(c <-chan int) {
	// Pull value off channel and print it:
	fmt.Println(<-c)
}
