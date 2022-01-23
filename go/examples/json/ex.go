package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

// The struct/embedded struct that we will turn into JSON:
type ExampleStruct struct {
	Integer int
	Float   float64
	String  string
	Bool    bool
	Slice   []string
	Map     map[string]int
	Struct  SomeStruct `json:"embedded_struct"` // name the JSON field embedded_struct
}

type SomeStruct struct {
	String     string
	IntSlice   []int
	Omitted    string `json:"omitempty"` // omit when the field is empty
	NotOmitted string
}

// Note that the struct fields must be capitalized for them to be eligible for serialization.

func main() {
	// Construct the ExampleStruct:
	Example := ExampleStruct{
		Integer: 100,
		Float:   15.12,
		String:  "Word",
		Bool:    false,
		Slice:   []string{"go", "python", "c"},
		Map: map[string]int{
			"a": 1,
			"b": 2,
			"c": 3,
		},
		Struct: SomeStruct{
			String:   "abcdefg",
			IntSlice: []int{1, 2, 3, 4},
		},
	}
	// Print the struct:
	fmt.Println(Example)
	// Marshal the struct
	Example_marshalled, _ := json.Marshal(Example) // also works with &Example
	fmt.Printf("%T %v\n", Example_marshalled, Example_marshalled)
	// Print the marshalled struct as a string(json.Marshal returns a byte-slice):
	fmt.Println(string(Example_marshalled))
	// Make the JSON pretty:
	prettyJSON, _ := json.MarshalIndent(Example, "", "\t")
	fmt.Println(string(prettyJSON))
	// Write it to a file for later use:
	_ = ioutil.WriteFile("test.json", prettyJSON, 0644) // this writes the JSON to 'test.json'
	// Alternatively, use an encoder:
	f, _ := os.Create("encoder_test.json")
	defer f.Close()
	// pass filehandler to NewEncoder and Encode the Example struct:
	_ = json.NewEncoder(f).Encode(&Example) // this writes the JSON to 'encoder_test.json'

}
