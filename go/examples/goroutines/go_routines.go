package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2) // add the number of Goroutines we will use to the wait group

	// Launch a Goroutine from a closure (has access to wg defined in main)
	go func() {
		example() // Have Goroutine run example()
		wg.Done() // Done decrements the WaitGroup counter by one
	}()
	// Launch another Goroutine:
	go func() {
		example()
		wg.Done()
	}()

	wg.Wait() // Wait blocks until the WaitGroup counter is zero.

	fmt.Println("Program finished.")
}

func example() {
	time.Sleep(5 * time.Second)
	fmt.Println("waited 5 seconds")
}
