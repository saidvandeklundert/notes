package main

import (
	"errors"
	"fmt"
)

// Define a func called insertComma that takes in a string and returns a string as well as an error
// if the input string is shorter then 3, return an error stating "string is too short"
// if the input string is longer, return the input string with a comma after the 3rd character
func insertComma(s string) (string, error) {
	stringLength := len(s)
	// if the string
	if stringLength <= 3 {
		return "", errors.New("string is too short")
	}
	//Change "Hey what is up?"
	s = s[0:3] + "," + s[3:]
	//To "Hey, what is up?"
	return s, nil
}

func main() {
	// run insertComma twice, catching the error if any and print the result to screen.
	// The first time you run the function, it should succeed. The second time it should fail.
	var longString = "Hey what is up?"
	newLongString, err := insertComma(longString)
	if err != nil {
		fmt.Println("newLongString failed:", err)
	} else {
		fmt.Printf(newLongString)
	}
	var shortString = "yo"
	newShortString, err := insertComma(shortString)
	if err != nil {
		fmt.Println("insertComma failed:", err)
	} else {
		fmt.Printf(newShortString)
	}

}
