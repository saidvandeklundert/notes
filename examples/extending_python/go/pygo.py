from random import randrange, random
from ctypes import c_char_p
from ctypes import cdll
from typing import Dict
import json
import time
import sys
import os
import psutil


go_lib = cdll.LoadLibrary("./pygo.so")
go_lib.pygo.restype = c_char_p


args_d = {
    "str": "string",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": ["a", "b"],
}


def rand_args() -> Dict:
    args_d = {
        "str": "string",
        "int": randrange(100, 200),
        "float": random(),
        "mapping": {"a": "a"},
        "slice": ["aaaa" for x in range(randrange(300000, 3000000))],
    }

    return args_d


JSON_STRING = json.dumps(args_d).encode("utf8")


if __name__ == "__main__":
    # run the go func once:

    start = time.time()
    go_response = go_lib.pygo(JSON_STRING)
    end = time.time()
    go_response = go_response.decode()
    print(f"Calling Go fun took: {end - start}")
    print(go_response)

    # run the fun many times and see if how the memory is:
    n = 0
    while n < 1000:
        arg = json.dumps(rand_args()).encode("utf8")
        go_lib.pygo(arg)
        mem_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

        n = n + 1
        # time.sleep(0.1)
        print(f"arg has size {sys.getsizeof(arg)}\tmemory usage is {mem_usage}")
"""
python.\pygo.py
Calling Go fun took: 0.0034389495849609375
{"str":"Marie","int":111,"float":0,"slice":["b","b","b","b","b"],"mapping":null}
arg has size 23604190   memory usage is 241.44921875
arg has size 2717414    memory usage is 221.76171875
arg has size 19029990   memory usage is 286.875
arg has size 8382429    memory usage is 276.4921875
arg has size 15518502   memory usage is 282.87890625
arg has size 5286485    memory usage is 272.9609375
arg has size 11237877   memory usage is 278.50390625
"""