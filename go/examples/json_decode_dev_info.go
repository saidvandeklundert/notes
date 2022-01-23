/*
	JSON data that is used:
	{
	"datacenter": "ams01",
	"hostname": "sr01.ams01",
	"model": "mx960",
	"neighbors": [
		"br01.ams",
		"r01.sr01.ams",
		"lr01.ams",
		"bs01.eq01.ams",
		"bs01.eq01.ams"
	],
	"os": "junos",
	"serial": "JN22CB930EFB",
	"software-version": "17.4R2-S11",
	"type": "dar",
	"uptime-seconds": "3963073",
	"vendor": "juniper"
	}

	Python example:

	with open("dev_info.json") as f:
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

type DevInfo struct {
	Datacenter      string   `json:"datacenter"`
	Hostname        string   `json:"hostname"`
	Model           string   `json:"model"`
	Neighbors       []string `json:"neighbors"`
	Os              string   `json:"os"`
	Serial          string   `json:"serial"`
	SoftwareVersion string   `json:"software-version"`
	Type            string   `json:"type"`
	UptimeSeconds   string   `json:"uptime-seconds"`
	Vendor          string   `json:"vendor"`
}

func main() {
	// 2: Open the JSON file and read the data from it:
	jsonFile, err := os.Open("dev_info.json")
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)

	// 3: Create an instance of the struct and unmarshal the JSON into the struct:
	var Device DevInfo
	if err := json.Unmarshal(byteValue, &Device); err != nil {
		fmt.Println(err)
		return
	}
	// 4: Print the data that is unmarshalled into to struct to screen:
	fmt.Println("Data stored in the PortInfo struct:\n\n", Device, "\n\n")

	// 5: Use MarshalIndent to return pretty JSON data encoding:
	out, err := json.MarshalIndent(Device, "", "\t")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Data Marshalled out of the PortInfo struct:\n\n", string(out), "\n")

}
