package main

import (
	"fmt"
)

func main() {
	// make a channel with a buffer (only use when sure you need it):
	c := make(chan int, 1)

	// Put value onto the channel:
	c <- 50

	// Next line pulls the value off the channel:
	fmt.Println(<-c)
}
