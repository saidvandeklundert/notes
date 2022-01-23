/*
	JSON data that is used:
	[
		{
		"from_device_id": "pr01.dal",
		"from_port": "et-0/0/21",
		"to_device_id": "cr01a.dal",
		"to_port": "Eth4/1",
		"comments": "DESCRIPTION"
		},
		{
		"from_device_id": "pr01.dal",
		"from_port": "et-0/0/26",
		"to_device_id": "cr01b.dal",
		"to_port": "Eth4/2",
		"comments": "DESCRIPTION"
		}
	]

	Python example:

	with open("topology.json") as f:
        d = json.load(f)
	print(d)

*/
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

// 1: define the struct that will hold the JSON data:
type PortData struct {
	RemoteDevice string `json:"to_device_id"`
	RemotePort   string `json:"to_port"`
	LocalDevice  string `json:"from_device_id"`
	LocalPort    string `json:"from_port"`
	Comments     string `json:"comments"`
}

func main() {
	// 2: Open the JSON file and read the data from it:
	jsonFile, err := os.Open("topology.json")
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)

	// 3: Create an instance of the struct and unmarshal the JSON into the struct:
	var PortInfo []PortData
	if err := json.Unmarshal(byteValue, &PortInfo); err != nil {
		fmt.Println(err)
		return
	}
	// 4: Print the data that is unmarshalled into to struct to screen:
	fmt.Println("Data stored in the PortInfo struct:\n\n", PortInfo, "\n\n")

	// 5: Use MarshalIndent to return pretty JSON data encoding:
	out, err := json.MarshalIndent(PortInfo, "", "\t")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Data Marshalled out of the PortInfo struct:\n\n", string(out), "\n")

}
