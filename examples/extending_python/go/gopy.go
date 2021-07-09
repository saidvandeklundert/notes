package main

/*
#include <stdlib.h>
struct PyGo {
  char* py2go;
  char* go2py;
};
*/
import "C"
import (
	"encoding/json"
	"fmt"
	"unsafe"
)

type PyGo struct {
	String        string            `json:"str"`
	Int           int               `json:"int"`
	Float         float64           `json:"float"`
	StringSlice   []string          `json:"slice"`
	StringMapping map[string]string `json:"mapping"`
}

// Generates a data object for Python.
//
//export goDoStuff
func goDoStuff(py2go_info *C.char) C.struct_PyGo {

	// handle JSON incoming from Python:
	s := C.GoString(py2go_info)
	Py2GoArgs := new(PyGo)
	_ = json.Unmarshal([]byte(s), &Py2GoArgs)
	if Py2GoArgs.String == "print" {
		fmt.Printf("Message from the Go runtime:\n%v\n\n-----------\n", Py2GoArgs)
	}
	// Prepare JSON that is going to be returned:
	var result C.struct_PyGo
	Go2Py := new(PyGo)
	Go2Py.String = "Hello from the Go universe"
	Go2Py_return, _ := json.MarshalIndent(Go2Py, "", "\t")
	Go2Py_returnArgs := string(Go2Py_return)

	// Place the data in the C struct so we can communicate to the Python universe
	//  and, later on, remove the memory allocation.
	result.py2go = C.CString(s)
	result.go2py = C.CString(Go2Py_returnArgs)

	return result
}

//export gcPyGo
func gcPyGo(py2go_info C.struct_PyGo) {
	/*
		This function will garbage collect the struct that was used
		 to facilitate communications between Python and Go.
	*/

	C.free(unsafe.Pointer(py2go_info.py2go))
	C.free(unsafe.Pointer(py2go_info.go2py))
}

func main() {}
