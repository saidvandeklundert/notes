package main

import "fmt"

func main() {

	c := make(chan int)

	go func() {
		c <- 50
		close(c)
	}()
	// if ok is false if there are no more values to receive and the channel is closed.

	// Next, ok is true:
	v, ok := <-c
	fmt.Println(v, ok)
	// Next, after taking everything from the channel, ok is false:
	v, ok = <-c
	fmt.Println(v, ok)
}
