// go build -buildmode=c-shared -o main.so main.go
package main

import (
	"C"
)
import "fmt"

//export bar
func bar(StringFromPython *C.char) *C.char {
	s := C.GoString(&StringFromPython)

	fmt.Println(s)

	return C.CString("Go says hi!")
}

func main() {}
