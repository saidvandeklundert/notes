package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	f, _ := os.Open("show_version_short.txt")
	r := bufio.NewReader(f)

	fmt.Printf("\n%#v\n %v\n", r, r)
	// Use ReadSlice to read the file line by line:
	for {
		line, err := r.ReadSlice('\n')
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		fmt.Println("The bytes: ", line)
		fmt.Println("The string: ", string(line))
	}
	// Use Readline to read the file line by line:
	f, _ = os.Open("show_version_short.txt")
	r = bufio.NewReader(f)
	for {
		line, isPrefix, err := r.ReadLine()
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		fmt.Println("The bytes: ", line)
		fmt.Println("The string: ", string(line))
		fmt.Println("isPrefix: ", isPrefix)
	}
	// Use Read:
	f, _ = os.Open("show_version_short.txt")
	r = bufio.NewReader(f)
	// Create a buffer for n bytes
	b := make([]byte, 5)
	for {
		// Call read, pass in the buffer.
		//  Read will put content in the buffer!
		//   n is the number of bytes in the buffer
		n, err := r.Read(b)

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
