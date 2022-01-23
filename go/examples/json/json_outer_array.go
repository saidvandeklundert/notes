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
	Struct  SomeStruct `json:"embedded_struct"`
}

// Note that the struct fields must be capitalized for them to be eligible for serialization.

type SomeStruct struct {
	String     string
	IntSlice   []int
	Omitted    string `json:"omitted,omitempty"`
	NotOmitted string
}

func main() {
	var JSONdata []ExampleStruct
	jsonFile, _ := os.Open("outer_array_test.json")
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	_ = json.Unmarshal(byteValue, &JSONdata)
	fmt.Println(JSONdata)
	// Make the JSON pretty:
	prettyJSON, _ := json.MarshalIndent(JSONdata, "", "\t")
	fmt.Println(string(prettyJSON))
}
