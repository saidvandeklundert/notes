import ctypes
import time
import os
import psutil
import json
from pydantic import BaseModel


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


lib = ctypes.CDLL("./gopy.so")
goDoStuff = lib.goDoStuff
goDoStuff.argtypes = [ctypes.c_char_p]
goDoStuff.restype = PyGo
gcPyGo = lib.gcPyGo
gcPyGo.argtypes = [PyGo]


## info that is send into Go:
args_d_1 = {
    "str": "print",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": ["a", "b", "c"],
}
jsonString = json.dumps(args_d_1).encode("utf8")

args_d_2 = {
    "str": "noprint",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": ["a", "b", "c"],
}
jsonString2 = json.dumps(args_d_2).encode("utf8")


def work_work():
    PyGo_data = goDoStuff(jsonString)
    py2go_str = PyGo_data.py2go.decode()
    go2py_json = json.loads(PyGo_data.go2py.decode())
    print(f"send py2go\t: {py2go_str}\nreceived go2py\t: {go2py_json}\n\n------------")


def work_work_silent():
    PyGo_data = goDoStuff(jsonString2)


if __name__ == "__main__":
    # run the go func once:
    print("running")
    work_work()
    # run the fun many times and see if how the memory is:
    n = 0
    """"""

    while n < 10000000:
        # arg = json.dumps(rand_args()).encode("utf8")

        start = time.time()

        work_work_silent()
        # go_lib.goFuncUsingJsonArg("go_args.json".encode("utf8"))
        # go_lib.goFuncUsingJsonArgSilent()
        end = time.time()
        mem_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

        if n % 10000 == 0:
            print(
                f"memory usage is {round(mem_usage,2)}\t go func took {round(end - start, 5)}\t n is {n}"
            )

        n = n + 1
