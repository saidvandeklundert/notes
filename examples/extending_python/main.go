/*

	yum install wget
	git clone https://github.com/saidvandeklundert/python.git
	wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz
	rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz
	export PATH=$PATH:/usr/local/go/bin
	go version
	yum install gcc
	go build -buildmode=c-shared -o main.so main.go


	go_python.py will asume these files are in the same directory.
*/

package main

import (
	"C"
)
import "fmt"

//export goPrint
func goPrint(StringFromPython *C.char) *C.char {
	s := C.GoString(StringFromPython)

	fmt.Println(s)

	return C.CString("Go says hi!")
}

func main() {}
