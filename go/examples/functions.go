package main

import (
	"errors"
	"fmt"
)

func main() {
	fmt.Println("Some example functions.")
	var str_value string = "word"
	echo(str_value)
	var int_value int = 100
	new_int := multiply(int_value)
	// Explaining what multiply returned:
	fmt.Printf(`
int_value now:                 %v
int_ptr:                       %v
new_int:                       %v
new_int pointer value:		   %v

`, int_value, &int_value, new_int, &new_int)
	// Old int left as is
	// Change int_value:
	multiplyExisting(&int_value)
	fmt.Printf(`
int_value now:                 %v
int_ptr:                       %v

`, int_value, &int_value)

	// Illustrate we can pass a func + arg as arg to a func:
	x_1 := returnInt(silent_multiply(int_value))
	fmt.Printf("\nreturnInt(silent_multiply(int_value)) got us: %d\n", x_1)

	// Illustrate naked return:
	_ = echoReturnString(str_value)

	// Illustrate function that uses an error:
	var shortString = "yo"
	var longString = "Hey what is up?"
	newShortString, err := insertComma(shortString)
	if err != nil {
		fmt.Println("insertComma failed:", err)
	} else {
		fmt.Printf(newShortString)
	}

	newLongString, err := insertComma(longString)
	if err != nil {
		fmt.Println("newLongString failed:", err)
	} else {
		fmt.Printf(newLongString)
	}

}

// Echo a string:
func echo(s string) {
	fmt.Printf("%s\n", s)
}

// Return an integer multiplied by 2:
func multiply(i int) int {
	i = i * 2
	fmt.Printf("multiply i value: %d", i)
	return i
}

// multiply the int passed to the func:
func multiplyExisting(i *int) {
	*i = *i * 2
	fmt.Printf("multiplyExisting i value %d", &i)
}

// Return an int:
func returnInt(i int) int {
	return i
}

func silent_multiply(i int) int {
	i = i * 2
	return i
}

// Naked return:
func echoReturnString(s string) (str string) {
	str = s
	fmt.Printf("%s\n", str)
	return
	// Due to (str string) this is the same as return str

}

// Return an error:
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
