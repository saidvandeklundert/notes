/*
	using gosnmp v1.32.0
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"time"

	g "github.com/gosnmp/gosnmp"
)

func main() {
	hostFile := os.Args[1]                           // example "/home/said/hosts.txt"
	snmpString := os.Getenv("SNMP_COMMUNITY_STRING") // Ensure env var is set using `export SNMP_COMMUNITY_STRING=xxxx`
	devices, _ := ReadHosts(hostFile)

	c := make(chan string)

	for _, targetDev := range devices {
		go GetSnmpDevInfo(targetDev, snmpString, c)
	}
	for range devices {
		result := <-c
		fmt.Println(result)
	}

	fmt.Println("\nFin.")
}

// Opens a file and returns the lines as a []string:
func ReadHosts(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var hosts []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		hosts = append(hosts, scanner.Text())
	}
	return hosts, scanner.Err()
}

// Return the pointer to a new GoSNMP struct, which is the main interface to using SNMP:
func NewSnmpConn(targetDev, snmpString string) *g.GoSNMP {
	return &g.GoSNMP{
		Target:         targetDev,
		Port:           161,
		Community:      snmpString,
		Version:        g.Version2c,
		Timeout:        1 * time.Second,
		Retries:        3,
		MaxOids:        g.MaxOids,
		MaxRepetitions: 10,
	}
}

// Retrieve the required information from a device and write that information to a channel:
func GetSnmpDevInfo(targetDev, snmpString string, c chan<- string) {
	base := NewSnmpConn(targetDev, snmpString)
	err := base.Connect()
	if err != nil {
		fmt.Printf("Error while connecting: %v", err)
	}
	defer base.Conn.Close()

	oids := []string{
		".1.3.6.1.2.1.1.1.0",
		"1.3.6.1.2.1.1.5.0",
	}

	result, err := base.Get(oids)

	if err != nil {
		String := fmt.Sprintf("Error: %v when targeting %v", err, targetDev)
		c <- String
	}

	if result != nil {
		sysInfo := string(result.Variables[0].Value.([]byte))
		hostname := string(result.Variables[1].Value.([]byte))
		response := fmt.Sprintf("%v: %v", hostname, sysInfo)
		c <- response
	} else {
		String := fmt.Sprintf("no result for %s ", targetDev)
		c <- String
	}
}
