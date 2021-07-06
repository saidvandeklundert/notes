// go build -buildmode=c-shared -o main.so main.go
package main

import (
	"C"
	"fmt"
	"time"
)

//export bar
func bar(a string) string {

	s := "Go says " + a
	go func() {
		for {
			time.Sleep(time.Second)
			fmt.Println(s)
		}
	}()
	return s
}

func main() {}
