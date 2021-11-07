import pyo3_examples


if __name__ == "__main__":
    x = pyo3_examples.sum_as_string(5, 20)
    print(x)
    x = pyo3_examples.multiply(5, 20)
    print(x)
    print(pyo3_examples.list_sum([10, 10, 10, 10, 10, 5]))
    words_list = ["apple", "banana", "orange", "pear", "grape"]
    print(pyo3_examples.list_printer(words_list))
    array_of_strings = [
        "apple",
        "banana",
        "orange",
        "pear",
        "grape",
        "potato",
        "avocado",
        "sushi",
    ]
    print(pyo3_examples.array_printer(array_of_strings[0:6]))
