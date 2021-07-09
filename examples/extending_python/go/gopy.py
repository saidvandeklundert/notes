import ctypes
import time
import os
import psutil
import json


class PyGo(ctypes.Structure):
    """Generates a struct that is passed into C to be used in Go."""

    _fields_ = [
        ("py2go", ctypes.c_char_p),
        ("go2py", ctypes.c_char_p),
    ]

    def __del__(self):
        """destructor method, calledwhen all references of the object are deleted,
        this method calls a Go func that will free the C memory on the Go side."""
        gcPyGo(self)


# import the Go library:
lib = ctypes.CDLL("./gopy.so")
goDoStuff = lib.goDoStuff
goDoStuff.argtypes = [ctypes.c_char_p]
goDoStuff.restype = PyGo
gcPyGo = lib.gcPyGo
gcPyGo.argtypes = [PyGo]


## Example information that will be send to Go:
args_d = {
    "str": "print",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": ["a", "b", "c"],
}
goArgs = json.dumps(args_d).encode("utf8")
args_d["str"] = "noprint"
goArgs_2 = json.dumps(args_d).encode("utf8")


def goDoStuffandPrint():
    """Call GoDoStuff and have the Go runtime print the arguments to screen"""
    PyGo_data = goDoStuff(goArgs)
    py2go_str = PyGo_data.py2go.decode()
    go2py_json = json.loads(PyGo_data.go2py.decode())
    print(f"send py2go\t: {py2go_str}\nreceived go2py\t: {go2py_json}\n\n------------")


def goDoStuffInSilence():
    """Call GoDoStuff"""
    _ = goDoStuff(goArgs_2)


if __name__ == "__main__":
    goDoStuffandPrint()
    
    # run the func endlessly to check for a memory leak:
    n = 0
    while n < 10000000000:
        start = time.time()
        goDoStuffInSilence()
        end = time.time()
        mem_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        if n % 10000 == 0:
            print(
                f"memory usage is {round(mem_usage,2)}\t go func took {round(end - start, 5)}\t n is {n}"
            )

        n = n + 1
