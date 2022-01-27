"""
pip install -e src/
python3 src/test.py
"""
import c_extension


if __name__ == "__main__":

    i = 0
    while True:
        c_res = c_extension.multiplier(4, 25)
        print(c_res)
        i += 1
        if i > 1_000_000:
            break
