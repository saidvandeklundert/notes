from ctypes import *
from ctypes import cdll
import sys
import time
import psutil
import os
import gc

go_lib = cdll.LoadLibrary("./main.so")


s1, s2, s3, s4 = (
    "s1".encode("utf8"),
    "s2".encode("utf8"),
    "s3".encode("utf8"),
    "s4".encode("utf8"),
)


if __name__ == "__main__":
    # run the go func once:
    print("running")
    # run the fun many times and see if how the memory is:
    n = 0
    while n < 1000000:
        # arg = json.dumps(rand_args()).encode("utf8")

        start = time.time()
        go_lib.goSeveralStrings(s1, s2, s3, s4)
        # go_lib.goFuncUsingJsonArg("go_args.json".encode("utf8"))
        # go_lib.goFuncUsingJsonArgSilent()
        end = time.time()
        mem_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

        print(
            f"memory usage is {round(mem_usage,2)}\t go func took {round(end - start, 5)}\t n is {n}"
        )
        # if n % 10000 == 0:
        # n = gc.collect()
        # print("WE COLLECTED GARBAGE!!!")
        # print(f"We collected {n} objects")
        # time.sleep(0.1)

        n = n + 1