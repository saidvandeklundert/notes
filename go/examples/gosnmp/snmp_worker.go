/*
	using gosnmp v1.32.0

	Example where a worker pool is defined and used to collect information from a device.
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
	"time"

	g "github.com/gosnmp/gosnmp"
)

func main() {
	hostFile := os.Args[1]                           // example "/var/tmp/hosts.txt"
	snmpString := os.Getenv("SNMP_COMMUNITY_STRING") // Ensure env var is set using `export SNMP_COMMUNITY_STRING=xxxx`
	devices, _ := ReadHosts(hostFile)
	//devices = devices[1:100]

	p := New(1000) // Create the worker pool and set the number of workers (goroutines)
	var wg sync.WaitGroup
	wg.Add(len(devices)) // Add the number of items that the workers need to work on

	// submit the work to the pool of workers:
	for _, targetDev := range devices {
		ns := SnmpStruct{
			TargetHost: targetDev,
			SnmpString: snmpString,
		}
		go func() {
			p.Run(&ns)
			wg.Done()
		}()
	}

	wg.Wait() // wait for the workers to finish

	// shutdown the work pool and wait for all existing work to be completed
	p.Shutdown()
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

// Struct that represents the information gathered from a device:
type SnmpStruct struct {
	TargetHost string
	SnmpString string
	Hostname   string
	Sysinfo    string
}

// Task implements the Worker interface (in this example for the SnmpStruct):
func (s *SnmpStruct) Task() {
	s.GetValues()
	String := fmt.Sprintf("%s	%s		%s", s.TargetHost, s.Hostname, s.Sysinfo)
	fmt.Println(String)
	time.Sleep(time.Second)

}

// Method that gets the values we are interested in from the SnmpStruct.TargetHost:
func (s *SnmpStruct) GetValues() {
	base := NewSnmpConn(s.TargetHost, s.SnmpString)
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
		fmt.Println(err)
	}

	if result != nil {
		sysInfo := string(result.Variables[0].Value.([]byte))
		hostname := string(result.Variables[1].Value.([]byte))
		s.Hostname = hostname
		s.Sysinfo = sysInfo
	}
}

// The worker must be implemented by types that want to use the work pool

type Worker interface {
	Task()
}

// Pool provides a pool of goroutines that can execute any Worker
// tasks that are submitted
type Pool struct {
	work chan Worker
	wg   sync.WaitGroup
}

// New creates a new work pool:
func New(maxGoroutines int) *Pool {
	p := Pool{
		work: make(chan Worker),
	}

	p.wg.Add(maxGoroutines)
	for i := 0; i < maxGoroutines; i++ {
		go func() {
			for w := range p.work {
				w.Task()
			}
			p.wg.Done()
		}()
	}
	return &p
}

// Run submits work to the pool of workers:
func (p *Pool) Run(w Worker) {
	p.work <- w
}

// Shutdown waits for all the go routines to shutdown
func (p *Pool) Shutdown() {
	close(p.work)
	p.wg.Wait()
}
