import rust
from timeit import default_timer as timer


# count occurrences of a word in a string:
def count_occurences(contents: str, needle: str) -> int:
    total = 0
    for line in contents.splitlines():
        for word in line.split(" "):
            if word == needle or word == needle + ".":
                total += 1
    return total


text = (
    """🐍 searches through the words. Here are some additional words for 🐍.\nSome words\n"""
    * 100_000
)


res = count_occurences(text, "words")
print("count_occurences for 'words' in Python:", res)

rust_res = rust.count_occurences(text, "words")
print("count_occurences for 'words' in Rust:", rust_res)

start = timer()
res = count_occurences(text, "🐍")
elapsed = round(timer() - start, 10)
print(f"count_occurences for '🐍' in Python took {elapsed}. Result: {res}")

start = timer()
rust_res = rust.count_occurences(text, "🐍")
elapsed = round(timer() - start, 10)
print(f"count_occurences for '🐍' in Rust took {elapsed}. Result: {rust_res}")
print(f"Rust is {elapsed // res} times faster than Python")

"""
import timeit

timeit.timeit(
    "count_occurences(text, '🐍')", globals=globals(), number=1_000
)  # 1.3907543999957852
timeit.timeit(
    "count_occurences(text, '🐍')", globals=globals(), number=10_000
)  # 15.825483900029212

timeit.timeit(
    "rust.count_occurences(text, '🐍')", globals=globals(), number=10_000
)  # 15.825483900029212


# another approach, reading the file directly:
FILE_NAME = "C:\Temp\some_example.txt"


def count_occurences_in_file(filename: str, needle: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
    total = 0
    for line in contents.splitlines():
        for word in line.split(" "):
            if word == needle or word == needle + ".":
                total += 1
    return total


count_occurences_in_file(FILE_NAME, "speed")
timeit.timeit(
    "count_occurences_in_file('C:\Temp\some_example.txt', 'speed')",
    globals=globals(),
    number=10,
)  # 19.869251399999484

timeit.timeit(
    "count_occurences_in_file('C:\Temp\_6MB.txt', 'speed')",
    globals=globals(),
    number=10,
)  # 1.729457299981732

timeit.timeit(
    "count_occurences_in_file('C:\Temp\_90MB.txt', 'speed')",
    globals=globals(),
    number=10,
)  # 24.62653050001245

timeit.timeit(
    "count_occurences_in_file('C:\Temp\_723MB.txt', 'speed')",
    globals=globals(),
    number=1,
)  # 19.273160899989307

timeit.timeit(
    "rust.count_occurences_in_file('C:\Temp\_6MB.txt', 'speed')",
    globals=globals(),
    number=10,
)  #  1.0187502999906428
timeit.timeit(
    "rust.count_occurences_in_file('C:\Temp\_90MB.txt', 'speed')",
    globals=globals(),
    number=10,
)  # 15.291973400046118
timeit.timeit(
    "rust.count_occurences_in_file('C:\Temp\_723MB.txt', 'speed')",
    globals=globals(),
    number=1,
)  # 11.830814599990845


# small words
timeit.timeit(
    "count_occurences_in_file('C:\Temp\_6MB.txt', 'do')",
    globals=globals(),
    number=10,
)  # 1.7269608000060543

timeit.timeit(
    "rust.count_occurences_in_file('C:\Temp\_6MB.txt', 'do')",
    globals=globals(),
    number=10,
)  # 1.027798300026916

# large words
timeit.timeit(
    "count_occurences_in_file('C:\Temp\_6MB.txt', 'Gutenberg')",
    globals=globals(),
    number=10,
)  # 1.7358080000267364

timeit.timeit(
    "rust.count_occurences_in_file('C:\Temp\_6MB.txt', 'Gutenberg')",
    globals=globals(),
    number=10,
)
"""
