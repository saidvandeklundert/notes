package main

import "C"
import (
	"encoding/json"
)

//go build -buildmode=c-shared -o pygo.so pygo.go

type PyGoData struct {
	String        string            `json:"str"`
	Int           int               `json:"int"`
	Float         float64           `json:"float"`
	StringSlice   []string          `json:"slice"`
	StringMapping map[string]string `json:"mapping"`
}

//export pygo
func pygo(JsonStr *C.char) *C.char {
	s := C.GoString(JsonStr)
	ReceivedFromPython := new(PyGoData)
	_ = json.Unmarshal([]byte(s), &ReceivedFromPython)
	SendToPython := PyGoData{
		String:      "Marie",
		Int:         111,
		StringSlice: []string{"b", "b", "b", "b", "b"},
	}
	JsonData, _ := json.Marshal(SendToPython)
	return C.CString(string(JsonData))
}

func main() {}
