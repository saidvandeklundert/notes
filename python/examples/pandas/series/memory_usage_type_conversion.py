import pandas as pd
import random

series = pd.Series([random.randint(0, 255) for _ in range(1_000_000)])

print(series.memory_usage(deep=True))
series.info(memory_usage="deep")  # 7.6 MB

series = series.astype("uint8")
series.info(memory_usage="deep")  # 976.7 KB

# fun fact, even small python ints are 28 bytes:
# sys.getsizeof(0) >> 28

categories = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
series_strings = pd.Series([random.choice(categories) for _ in range(100_000)])

series_strings.info(memory_usage="deep")  # 5.5 MB

series_strings = series_strings.astype("category")  # 98.6KB
