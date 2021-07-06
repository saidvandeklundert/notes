package main

import (
	"C"
	"fmt"
	"time"
)

//export bar
func bar(a string, b *C.char) *C.char {
	c := a
	d := C.GoString(b)
	go func() {
		for {
			time.Sleep(time.Second)
			fmt.Println("a:", a)
			fmt.Println("b:", C.GoString(b))
			fmt.Println("c:", c)
			fmt.Println("d:", d)
		}
	}()
	return C.CString("hello from go")
}

func main() {}
