package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	// Use Read:
	f, _ := os.Open("example.txt")
	b := make([]byte, 120)
	for {
		// Call read, pass in the buffer.
		//  Read will put content in the buffer!
		//   n is the number of bytes in the buffer
		n, err := f.Read(b)

		// check for errors:
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		// Print the buffer.
		//  The [:n] makes sure that we only read the n-number of
		//   bytes that were written to the buffer
		fmt.Println(b[:n])
		fmt.Println(string(b[:n]))
	}

}
