"""
pip install -e src/
python3 src/test.py
"""
import c_extension
import timeit
import time

def multiplier(a:int, b:int)->int:
    return a * b

if __name__ == "__main__":    
    print(timeit.timeit("c_extension.multiplier(109580004, 109580004)", setup="from __main__ import c_extension"))    
    print(timeit.timeit("multiplier(109580004, 109580004)", setup="from __main__ import multiplier"))        
    start = time.perf_counter()
    p_func = multiplier(109580004, 109580004)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"Executing Python multiplier(109580004, 109580004): {elapsed_time:0.15f} seconds")   
    start = time.perf_counter()
    c_func = c_extension.multiplier(109580004, 109580004)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"Executing C c_extension.multiplier(109580004, 109580004): {elapsed_time:0.15f} seconds")   