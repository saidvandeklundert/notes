import rust


rust.list_printer(["one", "two", "three"])

example_dict = {
    "key 1": "value 1",
    "key 2": "value 2",
    "key 3": "value 3",
    "key 4": "value 4",
}

try:
    rust.dict_printer("wrong type")
except TypeError as e:
    print(f"Caught a type error: {e}")

rust.dict_printer(example_dict)