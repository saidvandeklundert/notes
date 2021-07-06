// go build -buildmode=c-shared -o main.so main.go
package main

import (
	"C"
)
import "fmt"

//export verify
func bar(StringFromPython *C.char) *C.char {
	s := C.GoString(StringFromPython)

	fmt.Println(s)

	return "Go says hi!"
}

func main() {}
