package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	// Creating channels that can transport different types of values:
	eve := make(chan int)
	odd := make(chan int)
	s_chan := make(chan string)

	// Run a func that sends values into the channels:
	go send(eve, odd, s_chan)

	// Run a func that uses 'select' to read the different values from these channels:
	receive(eve, odd, s_chan)
	elapsed := time.Since(start)
	fmt.Println("Seconds the script took to complete: ", elapsed)
}

const delaySeconds = 2

// Functions that sends different value types into the channels:
func send(e, o chan<- int, s chan<- string) {
	time.Sleep(delaySeconds * time.Second)
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			e <- i
		} else {
			o <- i
		}
	}
	time.Sleep(delaySeconds * time.Second)
	aSlice := []string{"some", "words", "were", "uttered"}
	for _, word := range aSlice {
		s <- word
	}
	time.Sleep(delaySeconds * time.Second)
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			e <- i
		}
	}
	time.Sleep(delaySeconds * time.Second)
	s <- "fin"
}

// loops over channels, using select to handle the
func receive(e, o <-chan int, s <-chan string) {
	// for instructs the function to just keep on running select
	for {
		// select blocks until one of its cases can run, then it executes that case.
		//  It chooses one at random if multiple are ready.
		select {
		case v := <-e:
			fmt.Println("Reading even from channel: ", v)
		case v := <-o:
			fmt.Println("Reading odd from channel: ", v)
		case v := <-s:
			fmt.Println("Reading string from channel: ", v)
		// Timeout is set in this case,
		//  every iteration resets the timer.
		case <-time.After(5 * time.Second):
			fmt.Println("Time is up!!")
			return // without this return, the program keeps hitting this case every 5 seconds.
		}
	}
}
