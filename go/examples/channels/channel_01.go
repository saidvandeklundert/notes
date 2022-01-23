package main

import (
	"fmt"
)

func main() {
	// This will fail: fatal error: all goroutines are asleep - deadlock!
	// Channels block
	c := make(chan int)
	c <- 50
	fmt.Println(<-c)
}
