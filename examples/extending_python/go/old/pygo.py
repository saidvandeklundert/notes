from random import randrange, random
from ctypes import c_char_p
from ctypes import cdll
from typing import Dict
import json
import time
import sys
import os
import psutil
import gc

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
        # "slice": ["aaaa" for x in range(randrange(300, 3000))],
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
    while n < 1000000:
        # arg = json.dumps(rand_args()).encode("utf8")
        arg = json.dumps(args_d).encode("utf8")
        start = time.time()
        go_lib.pygo(arg)
        end = time.time()
        mem_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

        print(
            f"arg has size {sys.getsizeof(arg)}\tmemory usage is {round(mem_usage,2)}\t running the go func took {round(end - start, 5)}"
        )
        if n % 10000 == 0:
            n = gc.collect()
            print("WE COLLECTED GARBAGE!!!")
            print(f"We collected {n} objects")
            time.sleep(0.1)

        n = n + 1

"""
python.\pygo.py
Calling Go fun took: 0.003561735153198242
{"str":"Marie","int":111,"float":0,"slice":["b","b","b","b","b"],"mapping":null}
arg has size 22181501   memory usage is 237.85546875     running the go func took 0.5898096561431885
arg has size 3744877    memory usage is 220.296875       running the go func took 0.07614493370056152
arg has size 14417941   memory usage is 269.08203125     running the go func took 0.32314276695251465
arg has size 8336365    memory usage is 263.62890625     running the go func took 0.19823074340820312
arg has size 15527749   memory usage is 270.21875        running the go func took 0.5204751491546631
arg has size 17848981   memory usage is 272.0390625      running the go func took 0.49249863624572754
arg has size 3658462    memory usage is 258.47265625     running the go func took 0.11305069923400879
arg has size 11586350   memory usage is 265.69140625     running the go func took 0.41544032096862793
"""