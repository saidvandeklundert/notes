"""
pip install -e src/
python3 src/test.py
"""
import samples


if __name__ == "__main__":

    i = 0
    while True:
        c_res = samples.multiplier(4, 25)
        print(c_res)
        i += 1
        if i > 100:
            break
    samples.run_struct_methods(5, 5)
