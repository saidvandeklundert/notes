package main

import (
	"fmt"
	"runtime"
	"time"
)

type SSOTInterface interface {
	ApiEndpoint()
	Send(c chan<- string, device string)
	ManyCalls(c chan string, devices []string)
}

func (s *ssot) ApiEndpoint() {
	fmt.Println(s.url)
}

func SSOT(token string, url string) SSOTInterface {
	return &ssot{token, url}
}

// Struct that defines SSOT:
type ssot struct {
	token string
	url   string
}

// Send func
func (s *ssot) Send(c chan<- string, device string) {
	time.Sleep(1 * time.Second)
	// Send value to channel using a for loop:

	c <- s.url + string(device)

}

func (s *ssot) ManyCalls(c chan string, devices []string) {
	for _, device := range devices {
		go s.Send(c, device)
	}

	for i := 1; i <= len(devices); i++ {
		Rec(c)
	}
}

// Receive func
func Rec(c <-chan string) {
	// Pull value off channel and print it:
	fmt.Println(<-c)
}

func main() {
	SSOT := SSOT(`s3cr3t`, "https://api.com/")
	SSOT.ApiEndpoint()
	// Make the channel:
	c := make(chan string)

	fmt.Printf("%T %p", c, &c)
	devices := []string{"ppr01", "ppr02", "ppr03", "ppr04", "dar01", "dar02"}
	for _, device := range devices {
		go SSOT.Send(c, device)
	}
	fmt.Println("\n", runtime.NumGoroutine())
	for i := 1; i <= len(devices); i++ {
		Rec(c)
	}
	fmt.Println("Finished Send and Rec 10 values.")
	SSOT.ManyCalls(c, devices)
	fmt.Println("Finished ManyCalls.")
}
