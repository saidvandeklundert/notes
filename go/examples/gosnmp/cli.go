/*
	using gosnmp v1.32.0
*/
package main

import (
	"fmt"
	"log"
	"os"

	g "github.com/gosnmp/gosnmp"
)

func main() {
	targets := os.Args[1:]                           // target IP, example: 10.199.14.61
	snmpString := os.Getenv("SNMP_COMMUNITY_STRING") // Ensure env var is set using `export SNMP_COMMUNITY_STRING=xxxx`

	for _, target := range targets {
		printDeviceInfo(target, snmpString)
	}

}

// Print the device hostname and system description to screen
func printDeviceInfo(target, snmpstring string) {
	g.Default.Target = target
	g.Default.Community = snmpstring
	err := g.Default.Connect()
	if err != nil {
		log.Fatalf("Connect() err: %v", err)
	}
	defer g.Default.Conn.Close()

	oids := []string{
		".1.3.6.1.2.1.1.1.0", // sysDescr
		"1.3.6.1.2.1.1.5.0",  // hostname
	}
	result, err := g.Default.Get(oids)

	if err != nil {
		fmt.Printf("Get() err: %v", err)
		return
	}

	fmt.Println("Checking host: ", target)
	for _, variable := range result.Variables {
		fmt.Printf("oid: %s, %s\n", variable.Name, string(variable.Value.([]byte)))
	}
}

/*
	Note: g.Default refers to the following struct from the gosnmp package:

	var Default = &GoSNMP{
		Port:               161,
		Transport:          udp,
		Community:          "public",
		Version:            Version2c,
		Timeout:            time.Duration(2) * time.Second,
		Retries:            3,
		ExponentialTimeout: true,
		MaxOids:            MaxOids,
	}



	Example output when running this script:

	# time go run main.go 10.100.10.59 10.0.0.1 192.168.1.1
	Checking host:  10.100.10.59
	oid: .1.3.6.1.2.1.1.1.0, Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE11, RELEASE SOFTWARE (fc3)
	Technical Support: http://www.cisco.com/techsupport
	Copyright (c) 1986-2017 by Cisco Systems, Inc.
	Compiled Sat 19-Aug-17 09:34 by prod_rel_team
	oid: .1.3.6.1.2.1.1.5.0, ms124.sr02.tok
	Checking host:  10.0.0.1
	oid: .1.3.6.1.2.1.1.1.0, Juniper Networks, Inc. qfx10008 Ethernet Switch, kernel JUNOS 15.1X53-D65.3, Build date: 2017-09-20 00:09:26 UTC Copyright (c) 1996-2017 Juniper Networks, Inc.
	oid: .1.3.6.1.2.1.1.5.0, pr01.dal
	Checking host:  192.168.1.1
	oid: .1.3.6.1.2.1.1.1.0, Arista Networks EOS version 4.20.15M running on an Arista Networks DCS-7050TX-64
	oid: .1.3.6.1.2.1.1.5.0, cs132b.tok

	real    0m0.701s
	user    0m0.500s
	sys     0m0.603s
*/
