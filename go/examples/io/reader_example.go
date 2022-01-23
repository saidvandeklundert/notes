package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	fmt.Println("stringReader()")
	stringReader()
	fmt.Println("readFile()")
	readFile()
	fmt.Println("genericFileRead()")
	genericFileRead()

}

func stringReader() {
	s := strings.NewReader("The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from 'de Finibus Bonorum et Malorum' by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.")

	buf := make([]byte, 8) // this buffer is created once and reused for every call to Read
	// If we make a new slice for every call to Read, we needlessly burden the garbage collector

	for {
		n, err := s.Read(buf) // Read returns n, which is the number of bytes written to the buffer

		// the io.EOF error value indicates there is nothing left to read.
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println(err)
			break
		}
		if n > 0 {
			fmt.Println(buf[:n]) // Here we use n to read exactly the number of bytes written to the buffer.
			// without this, the last iteration would read 'old' data.
			// Here we print the same bytes from the buffer as a string:
			fmt.Println(string(buf[:n]))
		}
	}
}

func readFile() {
	f, err := os.Open("sample.txt")
	if err != nil {
		fmt.Println("Handle the error: ", err)
	}
	defer f.Close()

	buf := make([]byte, 8)

	for {
		n, err := f.Read(buf)
		if err == io.EOF {
			break
		}

		if err != nil {
			fmt.Println("Handle the error: ", err)
		}

		if n > 0 {
			fmt.Println(string(buf[:n]))
		}
	}
}

// Generic reader function:
func genericReader(r io.Reader, bs int) {
	// define buffer
	buf := make([]byte, bs)

	for {
		// read from buffer
		n, err := r.Read(buf)
		// io.EOF indicates there is nothing left to read
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println(err)
			break
		}
		// print up to n bytes of the buffer:
		if n > 0 {
			fmt.Println(string(buf[:n]))
		}
	}
}

// Using the generic reader function:
func genericFileRead() {
	f, err := os.Open("sample.txt")

	if err != nil {
		fmt.Println(err)
	} else {
		defer f.Close()
		genericReader(f, 20)
	}
}
