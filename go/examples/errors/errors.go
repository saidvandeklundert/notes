package main

import (
	"errors"
	"fmt"
)

func exampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", errors.New("s was to short")
	} else {
		return s, nil
	}

}

func anotherExampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", fmt.Errorf("length of s should be > 6, it was %d", len(s))
	} else {
		return s, nil
	}

}

// Defining an error and storing it as a variable.
// Example taken from gzip, hence the reference to that package.
var (
	// ErrChecksum is returned when reading GZIP data that has an invalid checksum.
	ErrChecksum = errors.New("gzip: invalid checksum")
)

// This function will fail
func CheckSum() (string, error) {
	if "checksum" != "CHECKSUM" {
		err := ErrChecksum
		return "", err
	}
	return "s", nil
}

func main() {
	fmt.Println(exampleError("This will not throw an error"))
	fmt.Println(exampleError("Oops!"))
	fmt.Println(anotherExampleError("Oops!"))
	fmt.Println(CheckSum())

}
