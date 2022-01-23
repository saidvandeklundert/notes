package main

import (
	"fmt"
	"runtime"
	"sync"
)

// wg.Add
// wg.Done
// wg.Wait

func init() {
	runtime.GOMAXPROCS(1)
}

func main() {
	var wg sync.WaitGroup
	wg.Add(2)

	fmt.Println("Start Go routines")

	// Create a goroutine from the lower case function:
	go func() {
		lowercase()
		wg.Done()
	}()

	// Create goroutine from the uppercase function:
	go func() {
		uppercase()
		wg.Done()
	}() // the last () is the execution of the literal function

	// Wait for goroutines to finish:
	fmt.Println("Waiting for the goroutines to finish")
	wg.Wait()

	fmt.Println("Terminating program")
}

func lowercase() {
	fmt.Println("aaaaaaaaaaaa")
}

func uppercase() {
	fmt.Println("AAAAAAAAAAAA")
}
