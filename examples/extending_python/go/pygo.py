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

string_list = ["aaaa" for x in range(100000)]

args_d = {
    "str": "string",
    "int": 100,
    "float": 1.2,
    "mapping": {"a": "a"},
    "slice": string_list,
}


string_list = ["aaaa" for x in range(10000000)]


def rand_args() -> Dict:
    args_d = {
        "str": "string",
        "int": randrange(100, 200),
        "float": random(),
        "mapping": {"a": "a"},
        "slice": ["aaaa" for x in range(randrange(300000, 3000000))],
    }

    return args_d


if __name__ == "__main__":
    # run the go func once:
    start = time.time()
    jsonString = json.dumps(args_d).encode("utf8")
    end = time.time()
    print(f"sending JSON string of size {sys.getsizeof(string_list)}: {end - start}")

    go_response = go_lib.pygo(jsonString)
    go_response = go_response.decode()
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
sending JSON string of size 89095160: 0.009000539779663086
{"str":"Marie","int":111,"float":0,"slice":["b","b","b","b","b"],"mapping":null}
arg has size 20697965   memory usage is 312.56640625
arg has size 15976685   memory usage is 387.03125
arg has size 8676709    memory usage is 380.0
arg has size 15009140   memory usage is 385.9921875
arg has size 6453149    memory usage is 377.78125
arg has size 21978415   memory usage is 392.01171875
arg has size 5056237    memory usage is 375.828125
arg has size 19435622   memory usage is 389.3515625
arg has size 9077821    memory usage is 379.12890625
arg has size 15762750   memory usage is 385.2890625
arg has size 10173398   memory usage is 379.484375
arg has size 7635814    memory usage is 377.07421875
"""