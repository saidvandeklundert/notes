package main

import (
	"encoding/json"
	"fmt"
)

// 1: Define the struct:
type PortData struct {
	RemoteDevice string `json:"to_device_id"`
	RemotePort   string `json:"to_port"`
	LocalDevice  string `json:"from_device_id"`
	LocalPort    string `json:"from_port"`
	Comments     string `json:"comments"`
}

func main() {
	// 2: declare the struct and put data in it:
	PortInfo := []PortData{
		{
			RemoteDevice: "cr02b.dal",
			RemotePort:   "Eth3/1",
			LocalDevice:  "pr01.dal",
			LocalPort:    "et-3/0/26",
			Comments:     "DESCRIPTION"},
		{
			RemoteDevice: "cr02b.dal",
			RemotePort:   "Eth3/1",
			LocalDevice:  "pr01.dal",
			LocalPort:    "et-3/0/26",
			Comments:     "DESCRIPTION"},
	}
	fmt.Printf("%#v", PortInfo)

	// 3: Use Marhsal to return JSON data encoding:
	regularJSON, _ := json.Marshal(PortInfo)
	fmt.Println(string(regularJSON))
	// 4: Use MarshalIndent to return pretty JSON data encoding:
	prettyJSON, _ := json.MarshalIndent(PortInfo, "", "\t")
	fmt.Println(string(prettyJSON))
}
