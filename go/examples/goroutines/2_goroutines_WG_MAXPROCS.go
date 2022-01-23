// from go in action
package main

import (
	"fmt"
	"runtime"
	"sync"
)

// main is the entrypoint for all Go programs
func main() {
	// Allocate 2 logical processors for the scheduler to use
	runtime.GOMAXPROCS(2)

	// wg is used to wait for the program to finish
	// Add a count of two, one for each goroutine
	var wg sync.WaitGroup
	wg.Add(3)

	fmt.Println("Start of the Goroutines")

	// Declare an anonymous function and create a goroutine.
	go func() {
		// Schedule the call to tell main we are done
		defer wg.Done()

		// Display the Alphabet 3 times
		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'a'+26; char++ {
				fmt.Printf("%c ", char)
			}
		}
		printPrime("a")
	}()

	// Declare an anonymous function and create a goroutine.

	go func() {
		// SChedule the call to tell main we are done
		defer wg.Done()

		// display the alphabet three times.
		for count := 0; count < 3; count++ {
			for char := 'A'; char < 'A'+26; char++ {
				fmt.Printf("%c ", char)
			}
		}
		printPrime("A")
	}()

	// Declare an anonymous function and create a goroutine.

	go func() {
		// SChedule the call to tell main we are done
		defer wg.Done()

		// display the alphabet three times.
		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'A'+26; char++ {
				fmt.Printf("%c ", char)
			}
		}
		printPrime("B")
	}()

	// Wait for the goroutines to finish
	fmt.Println("Waiting for the go routines to finish.")
	wg.Wait()
	fmt.Println("Terminating program")

}

// display prime numbers for the first 5000 numbers
func printPrime(prefix string) {

next:
	for outer := 2; outer < 50000000; outer++ {
		for inner := 2; inner < outer; inner++ {
			if outer%inner == 0 {
				continue next
			}
		}

		fmt.Printf("%s:%d\n", prefix, outer)

	}
	fmt.Println("completed ", prefix)
}
