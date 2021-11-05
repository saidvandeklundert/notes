import time
import sys


character_dict = {}

if __name__ == "__main__":
    file_name = sys.argv[1]
    start_time = time.time()
    with open(file_name, "r") as file:
        for line in file:
            for char in line:
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1

    print(character_dict)
    print("Using Python: %s seconds" % (time.time() - start_time))
    import pandas as pd

    phrase = "Mary had a little lamb"
    print(pd.Series(list(phrase)).value_counts())
