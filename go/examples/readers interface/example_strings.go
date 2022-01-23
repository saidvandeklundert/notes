package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {

	var s string = "Golang."

	r := strings.NewReader(s)
	fmt.Printf("%T\n%v\n", r, r)
	b := make([]byte, 2)
	for {
		n, err := r.Read(b)
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		fmt.Println(string(b[:n]))
		fmt.Println(string(b[:]))

	}
}
