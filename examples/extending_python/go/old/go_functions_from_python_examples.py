from ctypes import *
from ctypes import cdll
import json
import time

go_lib = cdll.LoadLibrary("./main.so")

## Sending values to Go:
print(58 * "=")

# string
go_lib.goPrintString("From the Python runtime".encode("utf8"))

# int
go_lib.goPrintInt(1000000000)

# several strings
s1, s2, s3, s4 = (
    "s1".encode("utf8"),
    "s2".encode("utf8"),
    "s3".encode("utf8"),
    "s4".encode("utf8"),
)
go_lib.goPrintSeveralStrings(s1, s2, s3, s4)

## Receiving values from Go:
print(58 * "=")

# string
go_lib.goSendString.restype = c_char_p
bytes_received_from_go = go_lib.goSendString()
go_string = bytes_received_from_go.decode()
print(f"go_string value: {go_string} type {type(go_string)}")

# bytes
go_lib.goSendBytes.restype = c_char_p
go_bytes = go_lib.goSendBytes()
print(f"go_bytes value: {go_bytes} type: {type(go_bytes)}")

# int
go_lib.goSendInt.restype = c_longlong
go_int64 = go_lib.goSendInt()
print(f"go_int64 value: {go_int64} type: {type(go_int64)}")


### Communicating values through a JSON file:
print(58 * "=")

args_d = {
    "str": "string",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": ["a", "b", "c"],
}

with open("go_args.json", "w") as f:
    json.dump(args_d, f)


start = time.time()
go_lib.goFuncUsingJsonArg("go_args.json".encode("utf8"))
end = time.time()
print(end - start)


with open("go_args.json", "r") as f:
    d = json.load(f)
jsonString = json.dumps(d).encode("utf8")
go_lib.goCallUsingJsonArg(jsonString)
jsonString = None