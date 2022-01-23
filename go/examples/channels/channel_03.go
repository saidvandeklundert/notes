package main

import (
	"fmt"
)

func main() {
	// make the channel:
	c := make(chan int)

	// Launches go routine:
	go func() {
		c <- 50
	}()

	// Next line pulls the value off the channel:
	fmt.Println(<-c)
}
