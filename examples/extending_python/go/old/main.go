package main

/*
#include <stdio.h>
#include <stdlib.h>
*/
import "C"
import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"unsafe"
)

// Receiving values from CPython:

//export goPrintString
func goPrintString(StringFromPython *C.char) {
	s := C.GoString(StringFromPython)

	fmt.Printf("StringFromPython type: %T\ns type: %T\ns value: %v\n", StringFromPython, s, s)

}

//export goPrintSeveralStrings
func goPrintSeveralStrings(s1, s2, s3, s4 *C.char) {
	string1 := C.GoString(s1)
	string2 := C.GoString(s2)
	string3 := C.GoString(s3)
	string4 := C.GoString(s4)

	fmt.Printf("FromPython : %v %v %v %v\n", string1, string2, string3, string4)

}

//export goSeveralStrings
func goSeveralStrings(s1, s2, s3, s4 *C.char) {
	string1 := C.GoString(s1)
	string2 := C.GoString(s2)
	string3 := C.GoString(s3)
	string4 := C.GoString(s4)

	_ = string1 + string2 + string3 + string4
}

//export goPrintInt
func goPrintInt(IntFromPython C.longlong) {
	go_int64 := int64(IntFromPython)
	fmt.Printf("IntFromPython type: %T\ngo_int64 type: %T\ngo_int64 value: %v\n", IntFromPython, go_int64, go_int64)

}

// Sending values to CPython:

//export goSendString
func goSendString() *C.char {
	fmt.Println("Sending string to Python")
	s := C.CString("Go says hi!")
	return s
}

//export goSendBytes
func goSendBytes() unsafe.Pointer {
	fmt.Println("Sending bytes to Python")
	b := []byte("ABC€")
	return C.CBytes(b)
}

//export goSendInt
func goSendInt() C.longlong {
	var go_int64 int64
	go_int64 = 1984
	fmt.Println("Sending int64 to Python")
	return C.longlong(go_int64)

}

type PythonArgs struct {
	String        string            `json:"str"`
	Int           int               `json:"int"`
	Float         float64           `json:"float"`
	StringSlice   []string          `json:"slice"`
	StringMapping map[string]string `json:"mapping"`
}

// Following loads JSON from a file:

//export goFuncUsingJsonArg
func goFuncUsingJsonArg(FileName *C.char) {
	fmt.Println("Using args from JSON file: ", FileName)
	filename := C.GoString(FileName)
	jsonFile, _ := os.Open(filename)
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	JSONargs := new(PythonArgs)
	_ = json.Unmarshal(byteValue, &JSONargs)
	fmt.Printf("%v\n", JSONargs)

}

//export goFuncUsingJsonArgSilent
func goFuncUsingJsonArgSilent(FileName *C.char) {
	filename := C.GoString(FileName)
	jsonFile, _ := os.Open(filename)
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	JSONargs := new(PythonArgs)
	_ = json.Unmarshal(byteValue, &JSONargs)

}

//export goFuncUsingJsonArgSilentNoArg
func goFuncUsingJsonArgSilentNoArg() {

	jsonFile, _ := os.Open("go_args.json")
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	JSONargs := new(PythonArgs)
	_ = json.Unmarshal(byteValue, &JSONargs)

}

//export goCallUsingJsonArg
func goCallUsingJsonArg(JsonStr *C.char) {
	s := C.GoString(JsonStr)
	JSONargs := new(PythonArgs)
	_ = json.Unmarshal([]byte(s), &JSONargs)
	fmt.Printf("Received from Python type: %T\ns type: %T\n", JsonStr, s)
}

//export goCallUsingJsonArgSilent
func goCallUsingJsonArgSilent(JsonStr *C.char) {
	s := C.GoString(JsonStr)
	JSONargs := new(PythonArgs)
	_ = json.Unmarshal([]byte(s), &JSONargs)
	fmt.Println("x")
}

func main() {}
