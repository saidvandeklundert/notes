package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func main() {
	start := time.Now()
	fmt.Println(runtime.GOMAXPROCS(0))
	ConcurrentExample()

	duration := time.Since(start)

	fmt.Println("\nNumber of seconds main() took: ", duration)

}

// Start 6 Go routines that wait 5 seconds. This function completes in less then 5 seconds:
func ConcurrentExample() {
	// define the wait group:
	var wg sync.WaitGroup
	fmt.Printf("\nStart ConcurrentExample Func")
	// Start the Go routine and pass the address of the wait group:
	go ConcurrentFunc(1, &wg)
	go ConcurrentFunc(2, &wg)
	go ConcurrentFunc(3, &wg)
	go ConcurrentFunc(4, &wg)
	go ConcurrentFunc(5, &wg)
	go ConcurrentFunc(6, &wg)
	// specify the number of wait groups:
	wg.Add(6)
	// Wait for all of them to finish:
	wg.Wait()
	fmt.Printf("\nFinished ConcurrentExample Func")
}

// Print a number and wait 5 seconds:
func ConcurrentFunc(Nr int, wg *sync.WaitGroup) {
	// Ensure we wrap up saying done even if we crash
	defer wg.Done()
	fmt.Printf("\nStart ConcurrentFunc %d", Nr)
	time.Sleep(5 * time.Second)
	fmt.Printf("\nFinished ConcurrentFunc %d", Nr)
}
