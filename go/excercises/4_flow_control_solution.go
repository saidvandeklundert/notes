package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	// 1:
	// Define a slice containing a, b, c and d.
	// Loop over the slice and print both the index as well as the value:
	var Slice = []string{"a", "b", "c", "d"}
	for index, value := range Slice {
		fmt.Println(index, value)
	}
	// 2:
	//
	// Loop over the following array
	// 1, 2, 3, 4, 5, 6
	//
	// Iterate the array and print every value (not the index)
	// When the value is 3, skip it.
	// Be sure to exit the loop before the value reaches 6
	//
	Array := [6]int{1, 2, 3, 4, 5, 6}
	for _, nr := range Array {
		if nr == 3 {
			continue
		} else if nr >= 6 {
			break
		}
		fmt.Println(nr)
	}
	// 3:
	// Iterate a mapping called PeoplesAges
	// Print the following message: "<> is <> years old"
	// If the name is Marie or Anne, print "<> IS <> YEARS OLD."
	// If the name is Said and the age is 35, skip.
	var PeoplesAges = map[string]int{"Jan": 5, "Marie": 2, "Anne": 35, "Said": 35, "Joe": 35}
	for key, value := range PeoplesAges {
		if key == "Marie" || key == "Anne" {
			fmt.Println(key, "IS ", value, " YEARS OLD.")
		} else if key == "Said" && value == 35 {
			continue
		} else {
			fmt.Println(key, "is ", value, " years old.")
		}
	}
	// 4:
	// Use a switch to do the following:
	// - print "no match" when there is no match
	// - print "i is 4" when i is 4
	// - print "less then 2" when i is less then 2 and let the evaluation continue
	// - print "less then 3" when i is less then 3
	// - print "bigger then 5" when i is bigger then 5 and smaller then 9
	// - print "bigger then 7" when i is bigger then 7 and smaller then 9 and let the evaluation continue

	rand.Seed(time.Now().UnixNano())
	i := rand.Intn(10)
	fmt.Println(i)
	switch {
	case i > 7 && i < 9:
		fmt.Println("Bigger then 7")
		fallthrough
	case i > 5 && i < 9:
		fmt.Println("Bigger then 5")
	case i < 2:
		fmt.Println("Less then 2")
		fallthrough
	case i < 3:
		fmt.Println("Less then 3")
	case i == 4:
		fmt.Println("I is 4")
	default:
		fmt.Println("no match")
	}
	// 5:
	// Do a while loop the generates a random number.
	// If the number is above 8, the while loop should break.

	for {
		nr := rand.Intn(10)
		fmt.Println("In the while loop, number is: ", nr)
		if nr >= 9 {
			break
		} else {
			continue
		}
	}
}
